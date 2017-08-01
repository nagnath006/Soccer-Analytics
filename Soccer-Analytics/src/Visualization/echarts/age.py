import pandas as plt
import sqlite3
from datetime import datetime,date
from dateutil import parser
from echarts import Echart,Legend,Bar,Axis,Line,Radar
con = sqlite3.connect("database.sqlite",isolation_level=None)
cur = con.cursor() 	 	
age_set = {}
today = date.today()
for i in cur.execute('select player_name,birthday from player LIMIT 100'):
    x =  str(i[0]).split(' ')
    formatted_date = parser.parse(i[1])
    age= today.year - formatted_date.year - ((today.month, today.day) <    

(formatted_date.month,formatted_date.day))
    age_set[i[0]] = age
df = plt.DataFrame({'Name': age_set.keys(),'Age':age_set.values()})
p_val = list(age_set.values())
p_key = list(age_set.keys())
chart = Echart('Players Age Analysis')
#chart.use(Bar('Out of 100', p_val))
chart.use(Line('Out of 100', p_val))
chart.use(Legend(['Age Analysis']))
chart.use(Axis('category', 'bottom', data=p_key))
chart.plot()
