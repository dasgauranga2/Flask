from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('form.html')

@app.route('/result')
def result_page():
    # get information from html forms
    first_name = request.args.get('first')
    last_name = request.args.get('last')

    return render_template('result.html',first_name=first_name,last_name=last_name)

if __name__ == '__main__':
    app.run(debug=True)