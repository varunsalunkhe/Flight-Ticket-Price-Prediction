from flask import Flask, render_template, request, url_for, redirect, session,jsonify
# import pymongo
# import bcrypt
import pandas as pd
import numpy as np
import joblib
import traceback
# from logger.logger import log


model= joblib.load("model.pkl")
print("model added.")
# log.addLog("INFO","model loaded")

first_half_columns=joblib.load("first_half_columns.pkl")
print("first added.")
# log.addLog("INFO","columns loaded")

sec_half_columns= joblib.load("sec_half_columns.pkl")
print("sec added.")
# log.addLog("INFO","columns loaded")

all_cols= joblib.load("all_cols.pkl")
print("model added.")
# log.addLog("INFO","columns loaded")

app=Flask(__name__)


# def dayy(date):
#     dat=[]
#     a= pd.to_datetime(date, format= "%d-%m-%Y").day
#     b= pd.to_datetime(date, format= "%d-%m-%Y").month
#     dat.append(a)
#     dat.append(b)
#     return dat

# def timer(tt):
#     t=[]
#     c= pd.to_datetime(tt).hour
#     d= pd.to_datetime(tt).minute
#     t.append(c)
#     t.append(d)
#     return t

@app.route('/')
def index():
    return render_template("index.html")



@app.route("/predict" , methods=["GET","POST"])




def predict():
    if model:
        try:
        # email = session["email"]
        # data= [str(i) for i in request.form.values()]
            print("model added.")

            tess2 = request.json
            f_half = tess2[:4]
            new_input1 = pd.DataFrame(np.array(f_half).reshape(1,-1), columns= first_half_columns)
            new_input1= pd.get_dummies(new_input1)
            final1=new_input1.reindex(columns=all_cols , fill_value=0)


            new_input2=[]
            for i in range(4,8):
                if i==4:
        
                    new_input2= new_input2 + dayy(tess2[i])
                else:
                    new_input2=new_input2+timer(tess2[i])


            new_input2= pd.DataFrame(np.array(new_input2).reshape(1,-1),columns= sec_half_columns)

            final= pd.concat([final1,new_input2], axis = 1)

            prediction = model.predict(final)
            return jsonify({"Prediction ": str(prediction)})

        except:
            print("fu")
            return jsonify({"trace ": traceback.format_exc()})

            

        # if output == 0:
        #     return render_template('dashboard.html', mushroom ="The mushroom is Poisonous.",email = email)
        # else:
        #     return render_template('dashboard.html', mushroom ="The mushroom is Edible.",email = email)
    else:
        # return render_template("login.html")
        return ("no model is here to use")

def dayy(date):
    dat=[]
    a= pd.to_datetime(date, format= "%d-%m-%Y").day
    b= pd.to_datetime(date, format= "%d-%m-%Y").month
    dat.append(a)
    dat.append(b)
    return dat

def timer(tt):
    t=[]
    c= pd.to_datetime(tt).hour
    d= pd.to_datetime(tt).minute
    t.append(c)
    t.append(d)
    return t



if __name__ == "__main__":
    app.run(debug=True)