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
	sql1 = "INSERT INTO student values(" + request.json['sno'] + ",'" + request.json['firstname'] + "','" + request.json['lastname'] + "','" + request.json['status'] + "','" + request.json['semester'] + "')"

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
		for l in request.json['courses']:
			sql2 = "INSERT INTO courses values(" + request.json['sno'] + ",'" + l + "')"
			cursor.execute(sql2)

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
def get_student():
	db = mysql.connect(
	 host="localhost",
	 database="project3",
	 user="root",
	 passwd="Adventure@25",
	 auth_plugin='mysql_native_password'
	)
	query1 = "select sno,firstname,lastname,status,semester from student"
	cursor = db.cursor(dictionary=True)
	try:
		cursor.execute(query1)
		records = cursor.fetchall()
		student=[]
		for record in records:
			student.append({'sno':record['sno'],'firstname':record['firstname'],'lastname':record['lastname'],'status':record['status'],'semester':record['semester']})
		courses=[]

		query2 = "select * from courses"
		cursor.execute(query2)
		record2 = cursor.fetchall()

		for record in record2:
			courses.append({'sno':record['sno'],'courses_value':record['courses_value']})
		data = {'student':student,'courses':courses}
		result = {"ok": True,"data":data}
		return jsonify(result)
	except Exception as e:
		cursor.close()
		db.close()
		result = {"ok": False,"error":e.__str__()}
		return jsonify(result)

if __name__== '__main__':
	app.run(host='localhost',debug=True)