import pandas as plt
import sqlite3
from bokeh.charts import Bar, output_file, show,Area,Scatter
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, LabelSet,Slider
from bkcharts import *
from datetime import datetime,date
from dateutil import parser
from bokeh.io import save
from bokeh.layouts import row, widgetbox

con = sqlite3.connect("database.sqlite")
cur = con.cursor() 	 	
age_set = {}
today = date.today()
for i in cur.execute('select player_name,birthday from player LIMIT 500'):
    x =  str(i[0]).split(' ')
    formatted_date = parser.parse(i[1])
    age= today.year - formatted_date.year - ((today.month, today.day) <    

(formatted_date.month,formatted_date.day))
    age_set[i[0]] = age
df = plt.DataFrame({'Name': age_set.keys(),'Age':age_set.values()})

p = Scatter(df, y='Age',color='Brown',
                  title="PlayerAge", xlabel="Name",
                  ylabel="Age",width=1024,height=768)
age_slider = Slider(start=15, end=50, value=1, step=1,
                    title="AGE")	
#show(vform(age_slider))
layout = row(
    p,
    widgetbox(age_slider)
)
		
output_file("bar.html")			
show(layout)

