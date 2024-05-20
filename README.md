# Easy Diagnose - Heart Disease Prediction

## Overview
Easy Diagnose is a web application built for predicting heart disease based on user input parameters. It provides a user-friendly interface developed using Streamlit, allowing users to sign up, log in, and receive heart disease predictions based on their input.

## Features
- **User Authentication:** Users can sign up or log in to access the prediction functionality.
- **Input Parameters:** Users can enter relevant medical parameters for heart disease prediction.
- **Prediction Results:** The application provides a prediction result based on the input parameters.
- **Model:** The prediction model is trained using the Random Forest method on the Heart Disease dataset from UCI Machine Learning Repository.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/HeartDiseasePrediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd HeartDiseasePrediction
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the Streamlit server:
   ```bash
   streamlit run app.py
   ```
2. Access the application in your web browser using the provided URL (typically `http://localhost:8501`).

## Data Source
The heart disease prediction model is trained using the [Heart Disease dataset](https://archive.ics.uci.edu/dataset/45/heart+disease) from the UCI Machine Learning Repository. The data preprocessing and model training details are included in the codebase.
