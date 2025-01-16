from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from pdf_modifier import modify_pdf
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.config['UPLOAD_FOLDER'] = './uploads/'

class CPFInutForm(FlaskForm):
    cpf = StringField('CPF: ', validators=[DataRequired()])
    position = SelectField('Posição: ',
                           choices=[
                               ('top-left', 'Superior Esquerdo'),
                               ('top-right', 'Superior Direito'),
                               ('bottom-left', 'Inferior Esquerdo'),
                               ('bottom-right', 'Inferior Direito')
                           ])
    color = StringField('Cor: ', validators=[DataRequired()])


@app.route('/', methods=['GET', 'POST'])
def home():
    return "home page"