# Flask demo...
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/steve')
def hello_steve():
    return 'Hello Steve!'
    
if __name__ == '__main__':
    app.run()