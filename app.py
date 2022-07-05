from flask import Flask,redirect,url_for
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hello world!!!'
@app.route('/admin')
def welcome1():
    return 'Hello admin!!'

@app.route('/pass/<int:score>')
def success(score):
    return 'The person has passed and got '+str(score) +'marks'

@app.route('/fail/<int:score>')
def fail(score):
    return 'The person had failed and got '+str(score) +'marks'

@app.route('/results/<int:score>')
def results(score):
    result=""
    if score <50:
        result='fail'
    else:
        result='pass'

    return result

if __name__ == '__main__':
    app.run(debug =True)