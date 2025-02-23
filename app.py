from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the pickled model
with open('SVRModel.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        # Get form data
        input1 = float(request.form['input1'])
        input2 = float(request.form['input2'])
        input3 = float(request.form['input3'])
        input4 = float(request.form['input4'])
        input5 = float(request.form['input5'])
        state = request.form['state']
        
        # Create input array for prediction
        input_data = np.array([[input1, input2, input3, input4, input5]])
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        
        # Return prediction as JSON
        return jsonify({'prediction': prediction})
    
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
