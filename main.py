from flask import Flask,render_template,request
from flask import flash, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms
from wtforms import validators
from models import db
from models import Empleados

from pizza import Pizza
from models import Pizzas

app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()
 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
 
 
@app.route("/")
def inicio():
        create_form = forms.UserForm(request.form)
        return render_template("pizzeria.html", form = create_form)


@app.route('/index',methods=['GET', 'POST'])
def index():
     create_form=forms.UserForm2(request.form)
     if request.method=='POST':
          emp=Empleados(nombre=create_form.nombre.data,
                       direccion=create_form.direccion.data,
                       telefono=create_form.telefono.data,
                       email=create_form.email.data,
                       sueldo=create_form.sueldo.data)
          db.session.add(emp)
          db.session.commit()
     return render_template('index.html', form=create_form)

@app.route("/ABC_Completo",methods=["GET","POST"])
def ABC_Completo():
     create_form=forms.UserForm2(request.form)
     empleado=Empleados.query.all()

     return render_template("ABC_Completo.html",form=create_form,empleado=empleado)

@app.route('/eliminar',methods=['GET','POST'])
def eliminar():
     create_form=forms.UserForm2(request.form)
     if request.method=='GET':
        id=request.args.get('id')
        # select *from empleados where id== id
        emp = db.session.query(Empleados).filter(Empleados.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data=emp.nombre
        create_form.direccion.data=emp.direccion
        create_form.telefono.data=emp.telefono
        create_form.email.data=emp.email
        create_form.sueldo.data=emp.sueldo

     if request.method=='POST':
        id=create_form.id.data
        emp= Empleados.query.get(id) 
        #delete from empleados where id=id
        db.session.delete(emp)
        db.session.commit()
        return redirect(url_for('ABC_Completo'))
     return render_template('eliminar.html',form=create_form)   

@app.route('/modificar',methods=['GET','POST'])
def modificar():
     create_form=forms.UserForm2(request.form)
     if request.method=='GET':
        id=request.args.get('id')
        # select *from empleados where id== id
        emp = db.session.query(Empleados).filter(Empleados.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data=emp.nombre
        create_form.direccion.data=emp.direccion
        create_form.telefono.data=emp.telefono
        create_form.email.data=emp.email
        create_form.sueldo.data=emp.sueldo

     if request.method=='POST':
        id=create_form.id.data
        emp = db.session.query(Empleados).filter(Empleados.id==id).first()   
        emp.nombre=create_form.nombre.data
        emp.direccion=create_form.direccion.data
        emp.telefono=create_form.telefono.data
        emp.email=create_form.email.data
        emp.sueldo=create_form.sueldo.data
        db.session.add(emp)
        db.session.commit()
        return redirect(url_for('ABC_Completo'))
     return render_template('modificar.html',form=create_form) 
 
 
'''Pizzas'''


pizzas = []
@app.route("/pizzas", methods=["GET","POST"])
def agregar(): 
    create_form = forms.UserForm(request.form)
    if request.method=="POST":
        
        nombre = create_form.nombre.data
        direccion = create_form.direccion.data
        telefono = create_form.telefono.data
        cantidad = create_form.cantidad.data
        tamanio = create_form.tamanio.data
        ingredientes = create_form.ingredientes.data
        
        cuenta = 0
        if create_form.tamanio.data == 'Chica':
            cuenta = (create_form.cantidad.data * 40) + (create_form.cantidad.data * 10)
        elif create_form.tamanio.data == 'Mediana':
            cuenta = (create_form.cantidad.data * 80) + (create_form.cantidad.data * 10)
        elif create_form.tamanio.data == 'Grande':
            cuenta = (create_form.cantidad.data * 120) + (create_form.cantidad.data * 10)
        else:
            cuenta = 0

        agregar = Pizza(len(pizzas),nombre, direccion, telefono, cantidad, tamanio, ingredientes, cuenta)
        pizzas.append(agregar)
    return render_template("index2.html",form=create_form, pizzas = pizzas)

@app.route("/quitar", methods=["GET","POST"])
def quitar():
    return render_template("quitar.html",pizzas=pizzas)

@app.route("/quitarPizza", methods=["GET","POST"])
def quitarPizza():
    create_form = forms.UserForm(request.form)
    if request.method=="GET":
        i = request.args.get("index")
        pizzas.pop(int(i))
        return redirect(url_for('agregar'))
    return render_template("index2.html",form = create_form, pizzas=pizzas)

@app.route("/total", methods=["GET","POST"])
def total():
    total = 0

    for p in pizzas:
        total += p.cuenta
    return render_template("total.html",total=total)

@app.route("/continuar", methods=["GET","POST"])
def continuar():
    create_form=forms.UserForm(request.form)
    if request.method=="GET":
        
        for p in pizzas:
            orden = Pizzas(nombre =p.nombre,direccion = p.direccion,telefono = p.telefono,cantidad = p.cantidad,tamanio = p.tamanio,ingredientes = p.ingredientes)
            db.session.add(orden)
            db.session.commit()
        pizzas.clear()
        return redirect(url_for('agregar'))
    return render_template("index2.html", form= create_form)

@app.route("/cancelar", methods=["GET","POST"])
def cancelar():
    return render_template("cancelar.html",pizzas=pizzas)

@app.route("/actualizarLista", methods=["GET","POST"])
def actualizarLista():
    create_form = forms.UserForm(request.form)
    if request.method=="GET":
            i = request.args.get("index")
            pizza = pizzas[int(i)]
            create_form.id.data= i
            create_form.nombre.data= pizza.nombre
            create_form.direccion.data= pizza.direccion
            create_form.telefono.data= pizza.telefono
            create_form.cantidad.data = pizza.cantidad
            create_form.tamanio.data = pizza.tamanio
            create_form.ingredientes.data = pizza.ingredientes
        
    return render_template("modificar_pizza.html", form = create_form, pizzas=pizzas, i = i)


@app.route("/actualizar", methods=["GET","POST"])
def actualizar():
    
    create_form = forms.UserForm(request.form)
    if request.method=="POST":
        
        nombre = create_form.nombre.data
        direccion = create_form.direccion.data
        telefono = create_form.telefono.data
        cantidad = create_form.cantidad.data
        tamanio = create_form.tamanio.data
        ingredientes = create_form.ingredientes.data
        
        cuenta = 0
        if create_form.tamanio.data == 'Chica':
            cuenta = (create_form.cantidad.data * 40) + (create_form.cantidad.data * 10)
        elif create_form.tamanio.data == 'Mediana':
            cuenta = (create_form.cantidad.data * 80) + (create_form.cantidad.data * 10)
        elif create_form.tamanio.data == 'Grande':
            cuenta = (create_form.cantidad.data * 120) + (create_form.cantidad.data * 10)
        else:
            cuenta = 0

        modificar = Pizza(len(pizzas) - 1,nombre, direccion, telefono, cantidad, tamanio, ingredientes, cuenta)
        pizzas[int(create_form.id.data)] = modificar
        return redirect(url_for('cancelar'))
    return render_template("cancelar.html",form = create_form, pizzas = pizzas)


@app.route("/buscar", methods=["GET","POST"])
def buscar():
    create_form = forms.UserForm(request.form)
    if request.method=="POST":
        buscar = int(create_form.fecha.data)
        pizzas = Pizzas.query.filter(db.extract('month', Pizzas.created_date) == buscar).all()


    return render_template("pizzeria.html", form = create_form, pizzas = pizzas)


if __name__== "__main__":
    csrf.init_app(app)
    db.init_app(app)
    
    with app.app_context():
         db.create_all()
    app.run()