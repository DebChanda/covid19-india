import requests_html as req
import pandas as pd

session = req.HTMLSession()
r = session.get("https://covidout.in")
text = r.html.text

data = text.split("\n")[-1][27:]
df = pd.read_json(data)[['case_id', 'confirmed_on', 'discharged_on', 'state', 'status']]
print(df.tail(10))

