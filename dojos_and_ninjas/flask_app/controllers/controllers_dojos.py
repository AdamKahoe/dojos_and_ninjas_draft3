from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.models_dojo import Dojo


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojo = Dojo.get_all()
    return render_template("index.html",dojo = dojo)

@app.route('/dojo/new')
def new():
    return render_template("dojo.html")

@app.route('/create/dojo',methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('dojo.html', dojo=dojos.get_one_with_ninjas(data))