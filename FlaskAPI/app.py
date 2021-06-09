# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 13:15:08 2021

@author: ajy00
"""

import numpy as np
from flask import Flask, request, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('model.sav', 'rb'))

model1= ['Acura', 'Alfa', 'Aston', 'Audi', 'BMW', 'Bentley', 'Buick', 'Cadillac', 'Chevrolet', 'Chrysler', 'Dodge', 'FIAT', 'Ferrari', 'Ford', 'GMC', 'Genesis', 'Honda', 'Hyundai', 'INFINITI', 'Jaguar', 'Jeep', 'Kia', 'Land', 'Lexus', 'Lincoln', 'MINI', 'Maserati', 'Mazda', 'Mercedes-Benz', 'Mitsubishi', 'Nissan', 'Porsche', 'RAM', 'Rolls-Royce', 'Scion', 'Subaru', 'Tesla', 'Toyota', 'Volkswagen', 'Volvo']
transmission1 = ['Automatic', 'Manual']
exterior = ['Black', 'Blue', 'Gray', 'Red', 'Silver', 'White']
engine = ['H4', 'H6', 'I2', 'I3', 'I4', 'I5', 'I6', 'V10', 'V12', 'V6', 'V8', 'W12']
drivetrain = ['All-Wheel Drive', 'Four-Wheel Drive', 'Front-Wheel Drive', 'Rear-Wheel Drive']
fuel = ['Biodiesel', 'Diesel', 'Electric', 'Flex Fuel Vehicle', 'Gasoline', 'Hybrid']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [x for x in request.form.values()]
    #Conversion of year to age
    features[0] = 2021- int(features[0])
    # 1(mileage), 2(gas_mileage),3(num_features) no change
    for i in range(1,4):
        features[i]= int(features[i])
    # 4(description_len),5(color_imputed==1) add later
    #6 to 45 model
    model_num = model1.index(features[4])
    #46(Automatic), 47 (manual)
    transmission_num = transmission1.index(features[5])
    # 48 to 53 exterior color
    exterior_num = exterior.index(features[6])
    #54 to 58 interior color set black (55 ==1)
    #59 to 70 engine
    engine_num = engine.index(features[7])
    #71 to 74 drivetrain
    drivetrain_num = drivetrain.index(features[8])
    #75 to 80 fueltype
    fuel_num = fuel.index(features[9])
    
    # delete imputed things from features 
    features = features[:-6]
    print(features)
    #append zeroes
    for j in range(1,78):
        features.append(0)    
    #replace mean value ==2883 for description len
    features[4] = 2883
    # feature[5] no change for exterior imputed == 0
    #replacing 1 for features input
    features[6+model_num]=1
    features[46+transmission_num]=1
    features[48+exterior_num]=1
    features[54]=1 #interior color ==black fix
    features[59+engine_num]=1
    features[71+drivetrain_num]=1
    features[75+fuel_num]=1
    
    final_features = np.array(features)
    prediction = model.predict(final_features.reshape(1,-1))

    output = round(prediction[0])-4000
    #output= print(final_features)

    return render_template('index.html', prediction_text='Car price should be ${}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)