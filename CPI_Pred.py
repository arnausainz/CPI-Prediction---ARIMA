import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from fredapi import Fred
from datetime import datetime
from statsmodels.tsa.arima.model import ARIMA

#FED API 
fred = Fred(api_key='WRITE YOUR FED API KEY')

#Choose the start date
START = datetime(2000,1,1)

#From the FED we download the Serie: Sticky Price Consumer Price Index less Food and Energy
CPI ='CORESTICKM159SFRBATL' 
CPI = fred.get_series(CPI)

#We transform CPI into a DF and we cut it to the start date we want
CPI = CPI.to_frame('CPI')
CPI = CPI.loc[START:]

#Let's adjust the ARIMA, model (p,0,q)
model = ARIMA(CPI, order=(1,1,1))  
result = model.fit()

#Let's print the results
print(result.summary())

#After looking at the values, there are a few burdens in the model, as heteroskedasticity.
#Despite of the burdens it is still useful for a short-term prediction, so let's continue.

pred = result.get_forecast(steps=6)
pred_mean = pred.predicted_mean
pred_ci = pred.conf_int()

#Let's Plot the Results
plt.figure(figsize=(8,6))
plt.plot(CPI['CPI'], color='#035593', linewidth=3, label='Core Inflation Index')
plt.plot(pred_mean.index, pred_mean, label='Prediction', color='red')
plt.fill_between(pred_ci.index, pred_ci.iloc[:,0], pred_ci.iloc[:,1], color='pink', alpha=0.3)
plt.title('Core Inflation Index Prediction - 6 Months - ARIMA(1,1,1)', size = 15)
plt.axhline(2, color='r',linewidth=1, label='FED Inflation Goal')
plt.legend()
plt.savefig("CPI Prediction - 6 Months.png", dpi=300, bbox_inches='tight')
plt.show
