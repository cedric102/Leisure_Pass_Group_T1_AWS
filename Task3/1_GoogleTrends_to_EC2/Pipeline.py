from pytrends.request import TrendReq
from apscheduler.schedulers.blocking import BlockingScheduler
import pandas as pd

pytrends = TrendReq(hl='en-US')

keyword=[]
dataset = []

kw_list = ["Elon Musk" ,
        "Joe Biden" ,
        "Taylor Swift" ,
        "Godzilla" ,
        "Black Panther"]

def check_trends():
    pytrends.build_payload( kw_list ,
                            cat='0' ,
                            timeframe='now 1-H' ,
                            geo='' ,
                            gprop='' )

    data = pytrends.interest_over_time()

    dataset.append(data)
    result = pd.concat(dataset, axis=0)

    with open('trends.csv' , 'a') as fd :
        fd.write(result.to_csv())
    print( data )

check_trends()

scheduler = BlockingScheduler()
scheduler.add_job( check_trends , 'interval' , hours = 1 )
scheduler.start()
