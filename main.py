from flask import Flask,jsonify
from fun import sum,machinelearning

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/calculate/<int:n>')
def calculate(n):
    return jsonify(sum(n,2))

@app.route('/ml')
def some():
    a = machinelearning()
    return jsonify(a)




app.run(debug=True)