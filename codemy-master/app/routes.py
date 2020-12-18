from flask import render_template , request,redirect , url_for
from app import app
from app import worker




@app.route("/" , methods = ["GET" , "POST"])
def index():

    if request.method == 'GET':
        return render_template("index.html" , code = "" , href = "")

    if request.method == 'POST':
            name = worker.saveCode( request.form["data"])  
            return '{}'.format(name)



@app.route("/<id>" , methods = ["GET" , "POST"])
def code(id):
    result = worker.loadCode(id)
    
    if result:
        return render_template("index.html" , code = result , href = id )
    else:
        return render_template("index.html" , code = "" , href = '')    





