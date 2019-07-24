from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods = ['GET', 'POST'])
def results():
    userdata = dict(request.form)
    print(userdata) #What is userdata??
    word = userdata['word']
    print(word) #What is word??
    a = model.reverseit(word) ##going to model file
    ##calling reverseit
    ##passing in word that we stored
    ##storing the return value from that function as reversed
    print(a)
    return render_template('results.html', reversed = a)