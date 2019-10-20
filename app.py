from flask import Flask, render_template,request
from string import Template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/concar.html')
def concar():
    return render_template('concar.html')
@app.route('/ilearn.html')
def ilearn():
    return render_template('ilearn.html')




if __name__ == '__main__':
    app.run(debug=True,use_reloader=True,threaded=True)
