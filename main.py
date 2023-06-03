from flask import Flask, jsonify, render_template, request
from project_app.utils import Titanic
# Creating instance here
# 'app' is standard variable
app = Flask(__name__)

# @app.route("/") --> USED TO GET HOME API
# @app.route("/furniture") --> You will get 'Furniture' Page here

@app.route("/")
def hello_flask():
    print("Welcome to Product Sales Prediction")
    return render_template("index.html")


@app.route("/predict_charges",methods=["POST","GET"])
def get_sur():
    if request.method =="GET":
        print("We are in a GET Method")
                
    
        Pclass=float(request.args.get("Pclass"))
        Gender=request.args.get("Gender")
        Age=float(request.args.get("Age"))
        SibSp=float(request.args.get("SibSp"))
        Parch=float(request.args.get("Parch"))
        Fare=float(request.args.get("Fare"))
        Embarked=request.args.get("Embarked")

    
    else:
        print("error in if block")
        


    tat_pri=Titanic(Pclass,Gender,Age,SibSp,Parch,Fare,Embarked)
    charges=tat_pri.get_predicted()
    if charges == 1:
        charges_text = "Yes,Survived"
    else:
        charges_text = "Notsurvived"
    
    return render_template("index.html",prediction=charges_text)

print("__name__-->",__name__)
if __name__=="__main__":
    #app.run(host="0.0.0.0",post=5000,debug=false)
    app.run()



