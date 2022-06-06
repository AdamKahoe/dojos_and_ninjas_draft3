from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.models_ninja import Ninja
from flask_app.models.models_dojo import Dojo

@app.route('/ninjas')
def ninjas():
    dojos= Dojo.get_all()
    return render_template('ninja.html',dojos=dojos)


@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/')