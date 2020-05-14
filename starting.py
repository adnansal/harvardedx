import datetime
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def index():
    now=datetime.datetime.now()
    new_year = now.month ==1 and now.day ==1
    new_year=True
    return render_template("index.html",new_year=new_year)

@app.route('/loops')
def loop():
    names=['Raju','Mike','Manish']
    return render_template("loop.html",names=names)

@app.route('/hello',methods=['POST'])
def hello():
    name=request.form.get("name")
    return render_template("hello.html",name=name)

@app.route('/forms')
def form():
    return render_template("forms.html")



