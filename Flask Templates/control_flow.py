from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    username = "Gauranga"
    my_list = [1,2,3,4,5]
    
    return render_template('control_flow.html',my_list=my_list,username=username)

if __name__ == '__main__':
    app.run(debug=True)