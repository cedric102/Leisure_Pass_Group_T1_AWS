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


# pytrends.build_payload( ["Godzilla"] , cat='0', timeframe='today 5-y' , geo='' , gprop='' )

def check_trends():
#    print(keyword)
    pytrends.build_payload( kw_list ,
                            cat='0' ,
                            timeframe='now 1-H' ,
                            geo='' ,
                            gprop='' )

    data = pytrends.interest_over_time()

    print( data.iloc[0] )
#    dataset = []
    dataset.append(data)
    result = pd.concat(dataset, axis=0)

    with open('trends.csv' , 'a') as fd :
        fd.write(result.to_csv())
#    result.to_csv('trends.csv')

#    for i in data :
#        for j in i :
#            print( j )
    print( data )

# for kw in kw_list :
# keyword.append(kw)
check_trends()
scheduler = BlockingScheduler()
scheduler.add_job( check_trends , 'interval' , hours = 1 )
scheduler.start()
check_trends()
# keyword.clear()

# aws s3 cp ~/june2018/results s3://myBucket/june2018/results --recursive --endpoint arn:aws:s3:eu-west-2:384962687271:accesspoint/accesspoint

