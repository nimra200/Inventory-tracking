from flask import Flask,render_template,request,redirect
from models import db,PartModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
@app.before_first_request
def create_table():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data/create", methods = ["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("createitem.html")
    if request.method == "POST":
        part_id = request.form["part_id"]
        name = request.form["name"]
        quantity = request.form["quantity"]
        inventory_item = PartModel(part_id, name, quantity)
        db.session.add(inventory_item)
        db.session.commit()
        return redirect('/data')

@app.route("/data")
def retrieveDataList():
    inventory_items = PartModel.query.all()
    return render_template("datalist.html", inventory_items=inventory_items)
    
@app.route("/data/<int:id>/update", methods=["GET", "POST"])
def update(id):
    part = PartModel.query.filter_by(part_id=id).first()
    if request.method == "POST":
        if part:
            db.session.delete(part)
            db.session.commit()

            name = request.form["name"]
            quantity = request.form["quantity"]
            part_id = request.form["part_id"]
            part = PartModel(part_id=part_id, name=name, quantity=quantity)

            db.session.add(part)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Part with id = {id} doesn't exist"

    return render_template("update.html", part = part)

@app.route("/data/<int:id>")
def display(id):
    return render_template("itemdata.html", part = PartModel.query.filter_by(part_id = id).first())

@app.route("/data/<int:id>/delete", methods = ["GET", "POST"])
def delete(id):
    part = PartModel.query.filter_by(part_id = id).first()
    if request.method == "POST":
        if part:
            db.session.delete(part)
            db.session.commit()
            return redirect("/data")
        abort(404)
    return render_template("delete.html")

app.run(host='localhost', port=5000)