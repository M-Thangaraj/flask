from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hello world!!!'
@app.route('/admin')
def welcome1():
    return 'Hello admin!!'

if __name__ == '__main__':
    app.run(debug =True)