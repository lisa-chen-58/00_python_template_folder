from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.item import Item

# Home Route
@app.route("/")
def index():
    # displays 8x8 checkerboard
    return render_template("index.html")

# INSERT ROUTES

# gets all the items and returns them in a list of item objects .
@app.route('/items')
def items():
	return render_template('results.html',items=Item.get_all())

# gets all the items and returns them in a list of item objects .
@app.route('/create/item',methods=['POST'])
def create_item():
	data = {
        "name" : request.form['name'],
        "bun" : request.form['bun'],
        "meat" : request.form['meat'],
        "calories" : request.form['calories']
	}
	Item.save(data)
	return redirect('/items')