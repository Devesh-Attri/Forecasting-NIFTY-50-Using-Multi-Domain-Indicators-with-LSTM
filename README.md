# 📈 NIFTY 50 Forecasting using LSTM with Economic & Environmental Indicators

This project implements an LSTM-based deep learning model to forecast NIFTY 50 index prices by integrating financial, economic and environmental indicators. It combines stock market data with macroeconomic factors (like GDP, inflation) and climate variables (like air quality and temperature) to enhance prediction accuracy.

## 📁 Project Structure

```
├── air_quality_combine.py         # Script for air quality data processing
├── air_quality_extracted_csv/     # Folder with extracted air quality CSV files
├── Dataset/                       # Contains combined datasets for modeling
├── eda.ipynb                      # Exploratory Data Analysis notebook
├── model.ipynb                    # ARIMA and initial LSTM model notebook
├── new_model.ipynb                # Final improved LSTM model notebook
├── nifty50_combine.py             # Script to process NIFTY 50 & technical indicators
├── sample_labels.csv              # Example label or indicator data
├── test_plot.png                  # Generated test plot (forecast visualization)
├── newplot.png                    # Additional visualization output
├── .venv/                         # Python virtual environment (optional)
```

## 📊 Data Sources

- 📈 **NIFTY 50 & Indicators:** Yahoo Finance  
- 🌐 **Macroeconomics:** RBI, World Bank, IMF (GDP, Inflation, Interest Rates)  
- 🌍 **Environment:** NASA, NOAA, Germanwatch (CO₂, Temp Anomalies, AQI)

## 🚀 How to Run the Project

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Devesh-Attri/Forecasting-NIFTY-50-Using-Multi-Domain-Indicators-with-LSTM.git
   cd nifty50-lstm-forecasting
   ```

2. **Set up environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\\Scripts\\activate on Windows
   pip install -r requirements.txt
   ```

3. **Run notebooks in order:**
   - `eda.ipynb` → for exploration & preprocessing  
   - `model.ipynb` → ARIMA + initial LSTM  
   - `new_model.ipynb` → final integrated LSTM

## 🧠 Key Features

- Combines market, macroeconomic & environmental factors for forecasting  
- Uses ARIMA as a classical baseline model  
- Implements LSTM with dropout for uncertainty estimation  
- Visual comparison of actual vs predicted prices with confidence bands

## 📌 Results

- **RMSE:** ~1264.87  
- **MAE:** ~1018.85  
- Plots demonstrate strong alignment of LSTM predictions with real trends

## 📌 Improvements Ahead

- Integrate real-time sentiment and social data  
- Experiment with Transformer models  
- Expand dataset to include more global indices


## 🙌 Acknowledgements

Thanks to open data providers: Yahoo Finance, World Bank, NASA, RBI and NOAA.
