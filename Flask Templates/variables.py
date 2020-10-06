from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    string = "Gauranga Das"
    phones = ["Apple","Samsung"]
    # variables passed to the html page
    return render_template('variables.html',string=string,phones=phones)

if __name__ == '__main__':
    app.run()