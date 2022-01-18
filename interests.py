from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
import mysql.connector as mysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route ('/webforms/insert/', methods=['POST'])
def insert():
	sql1 = "INSERT INTO interests values(" + request.json['sid'] + ",'" + request.json['sname'] + "','" + request.json['degree'] + "')"

	db = mysql.connect(
	 host="localhost",
	 database="project3",
	 user="root",
	 passwd="Adventure@25",
	 auth_plugin='mysql_native_password'
	)
	cursor = db.cursor(dictionary=True)
	try:
		cursor.execute(sql1)
		for l in request.json['pls']:
			sql2 = "INSERT INTO pls values(" + request.json['sid'] + ",'" + l + "')"
			cursor.execute(sql2)

		for h in request.json['hobbies']:
			sql3 = "INSERT INTO hobbies values(" + request.json['sid'] + ",'" + h + "')"
			cursor.execute(sql3)
		db.commit()
		cursor.close()
		db.close()
		result = {"ok": True,"data":request.json}
		return jsonify(result)
	except Exception as e:
		db.rollback()
		cursor.close()
		db.close()
		result = {"ok": False,"error":e.__str__()}
		return jsonify(result)


@app.route('/webforms/display/',methods=['GET'])
def get_interests():
	db = mysql.connect(
	 host="localhost",
	 database="project3",
	 user="root",
	 passwd="Adventure@25",
	 auth_plugin='mysql_native_password'
	)
	query1 = "select sid,sname,degree from interests"
	cursor = db.cursor(dictionary=True)
	try:
		cursor.execute(query1)
		records = cursor.fetchall()
		interests=[]
		for record in records:
			interests.append({'sid':record['sid'],'sname':record['sname'],'degree':record['degree']})
		pls=[]

		query2 = "select * from pls"
		cursor.execute(query2)
		record2 = cursor.fetchall()

		for record in record2:
			pls.append({'sid':record['sid'],'pls_value':record['pls_value']})
		hobbies=[]
		query3 = "select * from hobbies"
		cursor.execute(query3)
		record3 = cursor.fetchall()

		for record in record3:
			hobbies.append({'sid':record['sid'],'hobbies_value':record['hobbies_value']})
		data = {'interests':interests,'pls':pls,'hobbies':hobbies}
		result = {"ok": True,"data":data}
		return jsonify(result)
	except Exception as e:
		cursor.close()
		db.close()
		result = {"ok": False,"error":e.__str__()}
		return jsonify(result)

if __name__== '__main__':
	app.run(host='localhost',debug=True)