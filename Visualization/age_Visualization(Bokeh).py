import pandas as plt
import sqlite3
from bokeh.charts import Bar, output_file, show,Area,Scatter
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, LabelSet
from bkcharts import *
from datetime import datetime,date
from dateutil import parser
from bokeh.io import save

con = sqlite3.connect("database.sqlite")
cur = con.cursor() 	 	
age_set = {}
today = date.today()
for i in cur.execute('select player_name,birthday from player LIMIT 50'):
    x =  str(i[0]).split(' ')
    formatted_date = parser.parse(i[1])
    age= today.year - formatted_date.year - ((today.month, today.day) <    

(formatted_date.month,formatted_date.day))
    age_set[i[0]] = age
#series_dict = dict((k, plt.Series(v)) for k, v in age_set.iteritems())
df = plt.DataFrame({'Name': age_set.keys(),'Age':age_set.values()})
#source = ColumnDataSource(df)
p = Bar(df,values='Age',label='Name',xscale='categorical',title="test chart",width=1024,height=768,color='Brown')
#p = Area(df,legend="top_left",xlabel='Name' ,ylabel='Age')
#p = figure(plot_width=400,plot_height=800)
#p.circle(age_set.keys(),age_set.values(),size=10)
output_file("bar.html")

show(p)

