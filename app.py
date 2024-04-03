#import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import random
#Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    print(prediction)
    output = int(prediction[0])
    output=random.choice([0, 1, 2, 3,4,5])
    print(output, type(output))
    
    # if output == 0:
    #     prediction_pos = "Atrial fibrillation"
    #     return render_template('index.html', prediction_pos = prediction_pos)
    # elif output == 1:
    #     prediction_neg = "Ventricular tachycardia"
    # elif output == 2:
    #     prediction_pos = "Ventricular fibrillation"
    #     return render_template('index.html', prediction_pos = prediction_pos)
    # elif output == 3:
    #     prediction_neg = "Atrial flutter"
    # elif output == 4:
    #     prediction_pos = "Bradycardia"
    #     return render_template('index.html', prediction_pos = prediction_pos)
    # elif output == 5:
    #     prediction_neg = "Sinus tachycardia"                        
    #     return render_template('index.html', prediction_neg = prediction_neg)
    return render_template('result.html', prediction=output)
if __name__ == "__main__":
    app.run(debug=False)