
from neuralprophet import NeuralProphet
import yfinance as yf
import matplotlib.pyplot as plt

class StockPredictor:  # noqa: E999
    
    def __init__(self, stock_symbol, start_date, end_date, forecast_days):
        self.stock_symbol = stock_symbol
        self.start_date = start_date
        self.end_date = end_date
        self.forecast_days = int(forecast_days)
        self.model = NeuralProphet()
        
    def get_data(self):
        self.data = yf.download(self.stock_symbol,
                                start=self.start_date,
                                end=self.end_date,)
        self.data = self.data.reset_index()
        self.stocks=self.data[["Date","Close"]]
        self.stocks.columns = ["ds","y"]
        
    def train(self):
        self.model.fit(self.stocks)
        
    
    def evaluate_model(self):
        future = self.model.make_future_dataframe(self.stocks,
                                                  periods=self.forecast_days)
        
        self.forecast = self.model.predict(future)
        print(self.forecast.columns)
        self.forecast['yhat1'] = self.forecast['yhat1'].clip(lower=0)
        self.actual_prediction = self.model.predict(self.stocks)
        self.actual_prediction['yhat1'] = self.actual_prediction['yhat1'].clip(lower=0)
        
    def plot(self):
        plt.figure(figsize=(20, 10))
        plt.title("Prediction of "+self.stock_symbol)
        plt.plot(self.actual_prediction["ds"], self.actual_prediction["yhat1"], label="Actual Prediction", c = 'red')
        plt.plot(self.forecast["ds"], self.forecast["yhat1"], label="Prediction_future", c = 'blue')
        plt.plot(self.stocks["ds"], self.stocks["y"], label="Actual", c = 'green')
        plt.legend()
        return plt