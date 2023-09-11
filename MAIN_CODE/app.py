import numpy as np
from flask import Flask, render_template,request
app = Flask(__name__)
import pickle

model =pickle.load(open('placed.pkl','rb'))

@app.route('/')
def helloworld():
    y=""
    return render_template('index.html',y=y)

@app.route('/login',methods = ['POST'])
def login():
    a =request.form["ag"]
    g = request.form["gen"]
    if(g=="m"):
        g=1
    else:
        g=0
    s = request.form["str"]
    if(s == "ecc"):
        s=3
    elif (s== "cse"): 
        s=1
    elif (s== "it"): 
        s=4
    elif (s== "mec"): 
        s=5
    elif (s== "ece"): 
        s=2
    else:
        s=0
    x = request.form["intr"]
    cg = request.form["cgpa"]
    b = request.form["bck"]

    t = [[int(a),g,s,int(x),float(cg),int(b)]]
    print(t)  
    output = model.predict(t) 
    print(output)
    if output[0]==1:
        a="High chances of getting Placed"
    else:
        a="Low chances of getting Placed"

    return render_template('index.html', y=a)

if __name__ == '__main__':
    app.run()