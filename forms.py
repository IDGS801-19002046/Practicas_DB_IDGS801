from wtforms import Form, StringField, IntegerField, FloatField
from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import EmailField,Form, StringField, IntegerField, RadioField, SelectField
# from wtforms.validators import DataRequired, Length, Email, NumberRange
from wtforms import validators

class UserForm(Form):
    id = IntegerField('id', [validators.DataRequired(message="El campo es requerido")])
    nombre = StringField('Nombre', [
        validators.DataRequired(message="El nombre es requerido"),
                                   validators.Length(min=5,max=25, message="Ingresa un nombre valido")
                                   ])
    direccion = StringField('Direccion',
                            [validators.DataRequired(message="El campo es requerido"),
                             validators.Length(min=5,max=100, message="Ingresa una direccion valida")
                                   ])
    telefono = StringField('Telefono', [
                                    validators.DataRequired(message="El campo es requerido"),
                                   validators.Length(min=5,max=100, message="Ingresa un numero valido")])
    cantidad = IntegerField('Numero Pizzas', [
                                    validators.DataRequired(message="El campo es requerido")])
    tamanio = RadioField('Tamaño Pizza', choices=[('Chica', 'Chica $40'), ('Mediana', 'Mediana $80'), ('Grande', 'Grande $120')],
                             validators=[validators.DataRequired(message="El campo es requerido")])
    ingredientes = RadioField('Ingredientes', choices=[('Jamon', 'Jamon $10'), ('Piña', 'Piña $10'), ('Champiñones', 'Champiñones $10')],
                             validators=[validators.DataRequired(message="Debe seleccionar al menos un ingrediente para la pizza")])
    opciones = [('1', 'Enero'), ('2', 'Febrero'), ('3', 'Marzo'),  ('4', 'Abril'),  ('4', 'Mayo'),  ('6', 'Junio'),  ('7', 'Julio'),  ('8', 'Agosto'),  ('9', 'Septiembre'), ('10', 'Octubre'),  ('11', 'Noviembre'),  ('12', 'Diciembre')]
    fecha = SelectField('Selecciona la opcion de un mes', choices=opciones)

