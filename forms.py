"""
Here we will create python class that will be representative of forms and convert it into 
automatically into html forms within our template.

Import descritpion
StringField: do not import from flask_wtf it comes with wtforms with python
"""

from flask_wtf import FlaskForm 
from wtforms import StringField
from wtforms.validators import DataRequired,Length, Email

# Now lets create a registration form with Flask wtf extension
class RegisterForm(FlaskForm):

    # Inside string field we have Username as unique name for unser name 
    # validators is to make datashould be required and length should be minand max 
    username = StringField("Username",
    validators=[DataRequired(),Length(min=2,max=20)])

    email = StringField("Email",validators=[DataRequired(),Email()])
