from flask_sqlalchemy import SQLAlchemy

import datetime
db=SQLAlchemy()

class Empleados(db.Model):
    __tablename__='empleados2'
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    direccion=db.Column(db.String(50))
    telefono=db.Column(db.String(10))
    email=db.Column(db.String(50))
    sueldo=db.Column(db.Float)
    

class Pizzas(db.Model):
    __tablename__='local_pizzeria'
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    direccion=db.Column(db.String(50))
    telefono=db.Column(db.String(50))
    cantidad=db.Column(db.Integer)
    tamanio=db.Column(db.String(50))
    ingredientes=db.Column(db.String(50))
    created_date=db.Column(db.DateTime,
                           default=datetime.datetime.now)
  
    