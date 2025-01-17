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

class CPFInputForm(FlaskForm):
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
    form = CPFInputForm()

    if form.validate_on_submit():
        if 'file' not in request.files:
            flash("O arquivo não foi incluído.")
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash("O arquivo não foi selecionado.")
            return request(request.url)
        
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER', filename]))

    return render_template('index.html', form=form)