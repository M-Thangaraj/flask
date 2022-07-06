from flask import Flask,redirect,url_for,render_template, request
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')
@app.route('/admin')
def welcome1():
    return 'Hello admin!!'
@app.route('/pass/<int:score>')
def success(score):
    return render_template('result.html',result =score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',result ='Fail')

@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks <50:
        result='fail'
    else:
        result='success'

    return redirect(url_for(result,score=marks))

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    print('In')
    # print(request.method)
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        total_score=(science+maths)/2
        print(total_score)
    # res=""
    # if total_score >=50:
    #     res="success"
    # else:
    #     res="fail"
    return redirect(url_for("success", score=total_score))

if __name__ == '__main__':
    app.run(debug =True)