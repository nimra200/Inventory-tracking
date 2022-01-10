from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PartModel(db.Model):
    __tablename__ = "inventory_table"

    id = db.Column(db.Integer, primary_key=True)
    part_id = db.Column(db.Integer(), unique = True)
    name = db.Column(db.String())
    quantity = db.Column(db.Integer())


    def __init__(self, part_id, name, quantity):
        self.part_id = part_id
        self.name = name
        self.quantity = quantity
               
    def __repr__(self):
        return f"Part: {self.name}; Part ID: {self.part_id}; Quantity: {self.quantity}"

