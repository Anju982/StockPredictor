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

st.markdown("""
    <style>
    .reportview-container .main .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 2rem;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f5f5f5;
        color: black;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="footer">
        <p>Copyright © 2024 Anjana Urulugastenna. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)

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

