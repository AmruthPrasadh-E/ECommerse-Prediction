from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__, template_folder="templates")

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict',methods=['POST'])
def predict():
#prediction=model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                              #data=np.array([car_model,company,year,driven,fuel_type]).reshape(1, 5)))
    sessionlen=request.form.get('sessionlen')
    timapp=request.form.get('timapp')
    timweb=request.form.get('timweb')
    member=request.form.get('member')
    #car_model=request.form.get('car_models')

   # int_features=[int(x) for x in request.form.values()]
    final=[np.array('sessionlen','timeapp','timeweb','member')]
    prediction=model.predict(pd.D)
    return render_template('index.html',pred = float(prediction*10000) )
if __name__ == '__main__':
    app.run(debug=True)