import sys
import json 

def generateGeneralForm(form):
    name = form['name'] + '.html'
    with open(name, 'w') as fp:
        fp.write('<html lang="en">\n'+
    '<head>\n'+
        '<meta charset="UTF-8">\n'+
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'+
        '<title>Document</title>\n'+
    '</head>\n'+
    '<body>\n\n')
    dbinfo = []
    fp.write('<h2>'+form['caption']+'</h2>\n\n')
    mysql = [form['backendURL'], form['backendHost'], form['backendPort'], form['mysqlUserID'],
    form['mysqlPWD'], form['mysqlDB']]


        # for item in mysql:
        #     dbinfo.append('<p>'+item+'</p>\n')


    fp.writelines(dbinfo)
    fp.write('\n<form action="">\n')
    elements = ''
    for e in form['elements']:
            
        etype = e['etype']
        ename = e['ename']
        #datatype = e['datatype']
        caption = e['caption']
        #size = e['size']
        #maxlength = e['maxlength']
        #required = e['required']
            
        if 'textbox' == etype and e['datatype'] == 'integer': 
            elements +='\n<label for="'+ename+'">'+caption+':</label>\n<input type="number" id="'+ename+'" name="'+ename+'"'+\
                ' size="'+e['size']+'" maxlength="'+e['maxlength']+ '" required><br><br>'
        elif 'textbox' == etype and e['datatype'] == 'string':
            elements += '<label for="'+ename+'">'+caption+':</label>\n<input type="number" id="'+ename+'" name="'+ename+'"'+\
                ' size="'+e['size']+'" maxlength="'+e['maxlength']+ '" required><br><br>'
        elif etype == 'checkbox':
            elements +='\n\n<p>'+caption+'</p><br>'
            groups = e['group']
            for gro in groups:
                if 'checked' in gro:
                    elements +='\n<input type="'+etype+'" name="'+ename+'" value="'+gro['value']+'" checked>\n'+\
                            '<label for="'+ename+'">'+gro['caption']+'</label><br>'
                else:
                    elements +='\n<input type="'+etype+'" name="'+ename+'" value="'+gro['value']+'">\n'+\
                            '<label for="'+ename+'">'+gro['caption']+'</label><br>'

        elif etype == 'selectlist':
            elements +='\n\n<p>'+caption+'</p>'
            groups = e['group']
            for gro in groups:
                if gro['value'] == 'on':
                    elements +='\n<select name="'+ename+'" id="'+ename+'">'+\
                            '\n<option value="'+gro['value']+'" selected>'+gro['caption']+'</option>'
                else:
                    elements +='\n<option value="'+gro['value']+'">'+gro['caption']+'</option>\n</select>'
        elif etype == 'radiobutton':
            elements +='\n\n<p>'+caption+'</p>'
            groups = e['group']
            for gro in groups:
                elements +='\n<input type="radio" name="'+ename+'" value="'+gro['value']+'">'+\
                        '\n<label for="'+gro['value']+'">'+gro['caption']+'</label><br>'
        elif etype == 'submit':
            elements +='\n\n<button type="'+etype+'" name="'+ename+'">'+caption+'</button>'
        else:
            elements +='\n\n<button type="'+etype+'" name="'+ename+'">'+caption+'</button>'


    elements +='\n</form>'                   

    fp.write(elements)
    fp.close()
    

def generateDisplayForm(form):
    display = '''
<html>
    <head>
        <title>'''+form["name"]+'''</title>
    </head>
<body>
    <h2>'''+form["caption"]+'''</h2>
    <input type="button" id="display" value="Display Content" onclick="displayContent()"/>
    <br>
    <div id="display_table"></div>
</body>
<script src="'''+form["name"]+'''.js"></script>
</html>
    '''
    f = open(form["name"]+"_display.html","w+")
    f.write(display)
    f.close()

def generateJS(form):
    elements = []
    variable = "var ename=["
    value = ""
    for e in form["elements"] :
        if e["etype"]!="submit" and e["etype"]!="reset" :
            elements.append(e["ename"])
            value = value +'"'+e["ename"]+'",'
    variable = variable + value + "]"
    display = '''
function displayContent(){
    var dtable = document.createElement('table');
    dtable.setAttribute('id','dtable');
    dtable.setAttribute('border',2);
    var tr = dtable.insertRow(-1);
    ename.forEach(function(e){
        var th = document.createElement('th');
        th.innerHTML = e;
        tr.appendChild(th);
    });
    var div = document.getElementById('display_table');
    div.appendChild(dtable);
}
    '''
    f = open(form["name"]+".js","w+")
    f.write(variable+display)
    f.close()

# def generatePython(form):
#     #insert and display
#     insertform()
#     displayform()
    
# def generateSQL(form):
#     #insert and select queries
#     insertquery()
#     displayquery()

# def insertform():

# def displayform():

# def insertquery():

# def displayquery():

def main():
    input = sys.argv[1]
    with open(input,'r') as fp:
        form = json.load(fp)
    generateGeneralForm(form)
    generateDisplayForm(form)
    generateJS(form)
    # generateSQL(form)
    # generatePython(form)
    
main()