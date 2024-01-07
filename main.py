import stock_forcaster as sf
import streamlit as st

st.title("Stock Forecaster")

with st.sidebar:
    with st.form(key="my_form"):
        stock_symbol = st.text_input(label="stock symbol")
        start_date = st.date_input(label="start date",
                                   value="today",
                                   key="start_date")
        end_date = st.date_input(label="start date",
                                   value="today",
                                   key="end_date")
        forcasting_period = st.number_input(label="forecasting period",
                                            value=365,
                                            key="forcasting_period")
        submit_button = st.form_submit_button(label="submit")
        
if submit_button:
    predictor = sf.StockPredictor(stock_symbol, start_date, end_date, forcasting_period)
    
    status_text = st.empty()
    
    status_text.text("The data is being downloaded")
    predictor.get_data()

    
    status_text.text("The model is being trained")
    predictor.train()
    
    status_text.text("The model is being evaluated")
    predictor.evaluate_model()
    
    status_text.empty()
    
    plot = predictor.plot()
    
    st.success("The prediction is completed and the graph is plotted")
    st.pyplot(plot)

