from flask import Flask,render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import (StringField,BooleanField,DateTimeField,
                    RadioField,SelectField,TextField,TextAreaField,
                    SubmitField)

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    
    breed = StringField("Enter breed",validators=[DataRequired()])
    neutered = BooleanField("Are you neutered")
    mood = RadioField('Choose mood : ',
                        choices=[('mood_one','Happy'),('mood_two','Excited')])
    food = SelectField('Pick favourite food : ',
                        choices=[('chi','Chicken'),('bf','Beef')])

    feedback = TextAreaField()
    submit = SubmitField('SUBMIT')

@app.route('/',methods=['GET','POST'])
def index():

    form = InfoForm()
    
    if form.validate_on_submit():
        # session is used to store the data 
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food.data
        session['feedback'] = form.feedback.data
        # redirect to another url
        # session is automatically passed
        return redirect(url_for('result'))

    return render_template('page1.html',form=form)

@app.route('/result')
def result():

    return render_template('page2.html')


if __name__ == '__main__':
    app.run(debug=True)