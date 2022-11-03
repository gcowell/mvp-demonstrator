from flask import Flask

app = Flask(__name__)

#deploy

@app.route('/')
def hello():
    return 'Hello, World!'
    
@app.route('/say-my-name')
def hello_world():
    return 'Hello, ' + request.args.get('name')
