# Rainfall Prediction Project

This project aims to predict rainfall in millimeters using a Support Vector Regressor (SVR) machine learning model. The backend is built with Flask, providing an API endpoint for making predictions.

## Features

- Predict rainfall in millimeters based on input parameters
- RESTful API built with Flask
- Support Vector Regressor model for accurate predictions
- Easy-to-use interface for making predictions

## INCULSIONS 
1. extended_rainfall_dataset.csv: Dataset used for the prediction
2. Rainfall_Prediction.ipynb: The python notebook file that was used for:
        -Data Loading and Exploration
        -Data Preprocessing and Feature Engineering
        -Exploratory Data Analysis (EDA)
        -Model Selection and Training
        -Model Evaluation and Interpretation
        -Conclusion and Future Work  
4. static\styles.css: Holds the designing for the prediction website.
5. templates\index.html: Holds the html structure of the prediction website.
6. SVRModel.pkl: The pickle file of the model trained.
7. requirements.txt: The data of the required modules to be installed before executing the file.
8. app.py: The flask application, which holds the backend of the prediciton website.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Pacman-ot/Rain_Predictor.git
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask server:
   ```
   python app.py
   ```

## API Endpoint

### POST /predict

Make a rainfall prediction.

**Input Parameters:**

The model takes the following input parameters:

- Soil Moisture (%)
- Solar Radiation (W/m^2)
- Cloud Cover (%)
- Humidity (%)
- Temperature (°C)

**Request Body:**

```json
{
  "temperature": 22.5,
  "humidity": 75,
  "cloud_cover": 60,
  "solar_radiation": 250.0,
  "soil_moisture": 30.5,
}
```

**Response:**

```json
{
  "predicted_rainfall": 33.96
}
```

## Model Input Details

The Support Vector Regressor model uses the following features to predict rainfall:

1. **Soil Moisture (%)**: The amount of water present in the soil, expressed as a percentage.
2. **Solar Radiation (W/m^2)**: The amount of solar energy reaching the Earth's surface, measured in watts per square meter.
3. **Cloud Cover (%)**: The percentage of the sky covered by clouds.
4. **Humidity (%)**: The amount of water vapor present in the air, expressed as a percentage.
5. **Temperature (°C)**: The air temperature measured in degrees Celsius.

These parameters provide a comprehensive set of meteorological and environmental factors that influence rainfall, allowing the model to make accurate predictions.


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Overview
```

This README.md file provides a comprehensive overview of your rainfall prediction project. It includes information about the project's features, installation instructions, usage guidelines, and contribution information. 

You can customize this README further based on your specific project requirements, such as adding more detailed information about the SVR model, data sources, or any additional features you might implement.
