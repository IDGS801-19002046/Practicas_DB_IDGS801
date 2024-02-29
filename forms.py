from wtforms import Form, StringField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, Email, NumberRange

class UserForm2(Form):
    id = IntegerField('id', [
        NumberRange(min=1, max=20, message='valor no válido')
    ])
    
    nombre = StringField('nombre', [
        DataRequired(message="El campo es requerido"),
        Length(min=4, max=30, message='Ingresa un nombre válido')
    ])

    direccion = StringField('dirección', [
        DataRequired(message="El campo es requerido"),
        Length(min=4, max=50, message='Ingresa una dirección válida')
    ])
    
    telefono = StringField('teléfono', [
        DataRequired(message="El campo es requerido"),
        Length(min=4, max=10, message='Ingresa un teléfono válido')
    ])

    email = StringField('email', [
        DataRequired(message='El campo es requerido'),
        Email(message='Ingresa un email válido')
    ])

    sueldo = FloatField('sueldo', [
        DataRequired(message='El campo es requerido'),
        Length(min=4, max=50, message='Ingresa un sueldo válido')
    ])
