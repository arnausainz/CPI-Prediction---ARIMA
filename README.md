# CPI Prediction - ARIMA
A concise time-series project that models and forecasts inflation using an ARIMA model in Python. It loads historical CPI data, fits the model, and produces 6-step-ahead forecasts with confidence intervals. Demonstrates skills in econometrics, Python, and data visualization.

1-. Objective: Predicting Macroeconomic TrendsThe primary goal is to leverage robust statistical modeling to predict the future path of inflation, specifically the Sticky Price Consumer Price Index less Food and Energy from the U.S. Federal Reserve (FRED).

2.- Methodology: Data Retrieval and ARIMA Modeling. 

The analysis follows the standard process for time-series forecasting:

Data Acquisition: The script uses the fredapi Python library to connect to the official Federal Reserve Economic Data (FRED) database and retrieve the historical series for the chosen Core Inflation index, starting from January 2000.

Model Selection and Fitting: The ARIMA(1,1,1) model is selected. The parameters (p, d, q) = (1, 1, 1) indicate:
(p=1) AutoRegressive (AR): The model uses one lagged observation of the time series.
(d=1) Integrated (I): The time series is differentiated once to achieve stationarity.
(q=1) Moving Average (MA): The model uses one lagged forecast error.

The model is fitted to the historical data using statsmodels. The resulting summary (result.summary()) is printed for diagnostic checks (e.g., checking for heteroscedasticity).

3.-Forecasting: The fitted model is used to generate a short-term forecast for the next 6 steps (6 months, given the series frequency).

4.- Key Results and Visualization

The script concludes by producing a clear, actionable visualization of the forecastThe model generates the mean prediction (pred_mean) for the next six periods.
Confidence Interval: A 95% confidence interval (pred_ci) is generated, illustrating the uncertainty associated with the forecast.

Visualization: 

A plot is created showing: 

The historical Core Inflation Index (blue line).
The 6-Month Prediction (red line).
The Confidence Interval (shaded pink area).
The FED's 2% Inflation Goal (horizontal red line) as a critical benchmark.
