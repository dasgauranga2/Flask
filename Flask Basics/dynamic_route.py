from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():

    return '<h1>Hello World</h1>'

@app.route('/info')
def info_page():

    return '<h1>Another page</h1>'

@app.route('/profile/<name>')
def profile_page(name):

    return f'<h1>Page for {name.upper()}</h1>'


if __name__ == '__main__':
    app.run()