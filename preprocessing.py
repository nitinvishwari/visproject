import pandas as pd
from datetime import datetime

data = pd.read_csv("static/data/covid_us.csv")

for i in range(0,len(data)):
    a = data.iloc[i]['submission_date']
    t = datetime.strptime(a, "%m/%d/%Y")
    target_time = t.strftime("%Y-%m-%d")
    #print(target_time)
    # use 'loc' to locate and change the original data
    data.loc[i,'submission_date'] = str(target_time)  # not rewrite PM/AM back

data.to_csv('static/data/covid_us.csv')
