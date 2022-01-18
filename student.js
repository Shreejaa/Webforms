var ename=["sno","firstname","lastname","courses","status","semester",]
function insertData(){

var jsondata = {
	"sno":document.getElementById("sno").value,
	"firstname":document.getElementById("firstname").value,
	"lastname":document.getElementById("lastname").value,
	"status":document.getElementById("status").value,
}
var radioelement = document.querySelector('input[name="semester"]:checked')
if(radioelement!=null){
	jsondata['semester']=radioelement.value;
}else{
	jsondata['semester']=''
}

var checkbox=[];
var checked1=document.querySelectorAll('input[type="checkbox"]:checked');
for(var e of checked1){
	checkbox.push(e.value);
}
jsondata["courses"]=checkbox;
var url='http://localhost:5000/webforms/insert/'
    $.ajax({
        url:url,
        type:"POST",
        data: JSON.stringify(jsondata),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        beforeSend: function(request) {
            request.setRequestHeader("Access-Control-Allow-Origin","*")
            request.setRequestHeader("Access-Control-Allow-Methods","POST");
        },
        success: function(response){
            if(response.ok){
                document.getElementById("result").innerHTML="<p>Data:"+JSON.stringify(response.data)+"  is inserted in database</p>";
                alert("Data:"+JSON.stringify(response.data)+"  is inserted in database");
                console.log(response);
            }else{
                alert(response.error);
            }
        },
        error: function(error){
                alert("ERROR "+JSON.stringify(error))
            },
    }).fail(function (jqXHR, textStatus, errorThrown) {
        alert("Connection Refused, Please try again!")
    });
    
}

function displayContent(){
    var dtable = document.createElement('table');
    dtable.setAttribute('id','dtable');
    dtable.setAttribute('class','table');
    dtable.setAttribute('border',2);
    var tr = dtable.insertRow(0);
    ename.forEach(function(e){
        var th = document.createElement('th');
        th.innerHTML = e;
        tr.appendChild(th);
    });
    
var url =  'http://localhost:5000/webforms/display/'
        $.ajax({
        url: url,
        type: 'GET',
        beforeSend: function(request) {
            request.setRequestHeader("Access-Control-Allow-Origin","*")
            request.setRequestHeader("Access-Control-Allow-Methods","GET");
        },
        success: function(response){
            if(response.ok){
                Object.keys(response.data).forEach(function(key){
                var value = response.data[key];
                console.log(key)
                document.getElementById("display_table").innerHTML+="<p><b>"+key+"</b></p>";
                var dtable = document.createElement('table');
                    dtable.setAttribute('id',key);
                    dtable.setAttribute('class','table');
                    dtable.setAttribute('border',2);
                    dtable.setAttribute('style','width:auto');
                    var tr = dtable.insertRow(0);
                Object.keys(value[0]).forEach(function(head){
                    var th = document.createElement('th');
                    th.innerHTML = head;
                    tr.appendChild(th);
                
                })
                i=1
                for(var v of value){
                    var tr = dtable.insertRow(i);
                    i+=1;
                    Object.keys(v).forEach(function(innerKey){
                        var td = document.createElement('td');
                        td.innerHTML = v[innerKey];
                        tr.appendChild(td); 
                    })
                }
                    var div = document.getElementById('display_table');
                    div.appendChild(dtable);
                
                }) 
            }else{
                alert(response.error);
            }
        },
        error: function(error){
                alert("ERROR "+JSON.stringify(error))
            },
    }).fail(function (jqXHR, textStatus, errorThrown) {
        alert("Connection Refused, Please try again!")
    });
    document.getElementById("display").disabled = 'true';
}
    