import requests_html as req
import pandas as pd
import numpy as np

session = req.HTMLSession()
r = session.get("https://covidout.in")
text = r.html.text

data = text.split("\n")[-1][27:]
main_data = pd.read_json(data)[4:]
main_data['dayno'] = pd.to_datetime(main_data['confirmed_on']).dt.dayofyear

def return_info():
    numbers = np.cumsum(main_data.dayno.value_counts().sort_index().values)
    dates = np.unique(main_data['confirmed_on'].values)
    days = np.unique(main_data['dayno'].values - main_data['dayno'].values.min() + 1)
    return numbers, days, dates

return_info()