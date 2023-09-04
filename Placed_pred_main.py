import numpy as np
from flask import Flask, render_template,request
app = Flask(__name__)
import requests

# Key used for deployment from IBM Watson Studio
API_KEY = "GfdAUA-8lXHUJHu0Mg9PSfJFPwB_gNGPSSysPmeQ9nZm"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
@app.route('/')
def helloworld():
    y=""
    return render_template('index.html',y=y)

@app.route('/login',methods = ['POST'])
def login():
    a = request.form["ag"]
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

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"fields": [[int(a),g,s,int(x),float(cg),int(b)]], "values": t}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/0c224bcc-f336-43b9-9ae5-73cee9ad4acb/predictions?version=2021-05-01', json=payload_scoring,headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    predictions = response_scoring.json()
    output = predictions['predictions'][0]['values'][0][0]
    print(output)
    if output==1:
        a="High chances of getting Placed"
    else:
        a="Low chances of getting Placed"

    return render_template('index.html', y=a)

if __name__ == '__main__':
    app.run()   