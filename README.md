Stock Price Prediction with NeuralProphet

This repository contains a Python script for predicting stock prices using the NeuralProphet library in Python. The code is organized into a StockPredictor class that leverages the functionalities of NeuralProphet along with the Yahoo Finance API for retrieving historical stock data.
Features:

    Data Retrieval: Utilizes yfinance to download historical stock data based on user-defined parameters such as the stock symbol, start date, and end date.
    Model Training: Trains a NeuralProphet model using the downloaded historical stock data.
    Prediction and Evaluation: Generates predictions for future stock prices and evaluates the model's performance.
    Visualization: Provides a visualization of the predicted stock prices against the actual historical data using Matplotlib.

Usage:

    Initialization: Instantiate the StockPredictor class by providing the stock symbol, start date, end date, and the number of days for forecast.
    Data Retrieval: Use the get_data() method to download and preprocess the historical stock data.
    Model Training: Train the NeuralProphet model on the retrieved data using the train() method.
    Prediction and Evaluation: Generate predictions for future stock prices and evaluate the model's performance with the evaluate_model() method.
    Visualization: Plot the actual historical prices, predicted future prices, and the model's predictions using the plot() method.

Dependencies:

    Python 3.x
    NeuralProphet
    yfinance
    Matplotlib
