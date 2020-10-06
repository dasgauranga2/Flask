from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    # link to a html file
    return render_template('basic.html')

if __name__ == '__main__':
    app.run()