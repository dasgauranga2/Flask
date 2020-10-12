from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    # field for entering a string
    breed = StringField("Dog breed")
    # field for submitting the form
    submit = SubmitField("Submit")

@app.route('/',methods=['GET','POST'])
def index():

    breed = False
    form = InfoForm()
    # check if the form is submitted
    if form.validate_on_submit():
        
        breed = form.breed.data
        form.breed.data = ''

    # link to a html file
    return render_template('basic.html',form=form,breed=breed)

if __name__ == '__main__':
    app.run(debug=True)