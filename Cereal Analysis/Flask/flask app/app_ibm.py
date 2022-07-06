from flask import Flask, render_template, request
app = Flask(__name__)
#import pickle
#model = pickle.load(open('cerealanalysis.pkl','rb'))
import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "gw7ux8RfWlek9s-oAFnXaRoK1b0LE6_1P7vVtXJ0nBcu"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
@app.route('/')
def helloworld():
    return render_template("base.html")

@app.route('/assesment')
def prediction():
    return render_template("index.html")

@app.route('/predict', methods = ['POST'])
def admin():
    a= request.form["mfr"]
    if (a == 'a'):
        a1,a2,a3,a4,a5,a6,a7=1,0,0,0,0,0,0
    if (a == 'g'):
        a1,a2,a3,a4,a5,a6,a7=0,1,0,0,0,0,0
    if (a == 'k'):
        a1,a2,a3,a4,a5,a6,a7=0,0,1,0,0,0,0
    if (a == 'n'):
        a1,a2,a3,a4,a5,a6,a7=0,0,0,1,0,0,0    
    if (a == 'p'):
        a1,a2,a3,a4,a5,a6,a7=0,0,0,0,1,0,0    
    if (a == 'q'):
        a1,a2,a3,a4,a5,a6,a7=0,0,0,0,0,1,0    
    if (a == 'r'):
        a1,a2,a3,a4,a5,a6,a7=0,0,0,0,0,0,1    
        
    b= request.form["type"]
    if (b == 'c'):
        b=0
    if (b == 'h'):
        b=1
    c= request.form["Calories"]
    d= request.form["Protien"]
    e= request.form["Fat"]
    f= request.form["Sodium"]
    g= request.form["Fiber"]
    h= request.form["Carbo"]
    i= request.form["Sugars"]
    j= request.form["Potass"]
    k= request.form["Vitamins"]
    l= request.form["Shelf"]
    m= request.form["Weight"]
    n= request.form["Cups"]

    t=[[int(a1),int(a2),int(a3),int(a4),int(a5),int(a6),int(a7),int(b),int(c),int(d),int(e),int(f),float(g),float(h),int(i),int(j),int(k),float(l),float(m),float(n)]]
    print(t)        
    payload_scoring = {"input_data": [{"fields": [['f0','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','f14','f15','f10','f17','f18','f19']], "values": t}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/af915221-6803-49bd-80d8-61a0f5f2ef52/predictions?version=2022-06-25', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    #print(response_scoring.json())
    pred=response_scoring.json()
    pred=pred['predictions'][0]["values"][0][0][0]
    print(pred)
    return render_template("prediction.html", z = pred)



if __name__ == '__main__':
    app.run(debug = False)

