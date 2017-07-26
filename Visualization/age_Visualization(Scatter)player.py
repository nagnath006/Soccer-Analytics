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

con = sqlite3.connect("database.sqlite",isolation_level=None)
cur = con.cursor() 	 	
age_set = {}
name = '%iniesta%'
#today = date.today()
cur.execute('select short_passing,long_passing,strength,vision,dribbling,balance,positioning from Player inner join Player_Attributes on Player.player_api_id = Player_Attributes.player_api_id where player_name like ? group by player_name',(name,))

i = list(cur.fetchone())
iniesta_attrib = {"short_passing":i[0],"long_passing":i[1],"strength":i[2],"vision":i[3],"dribbling":i[4],"balance":i[5],"positioning":i[6]}
#labels = ["short_passing","long_passing","strength","vision","dribbling","balance","positioning"]
df = plt.DataFrame.from_records([iniesta_attrib])
p_val = list(iniesta_attrib.values())
p_key = list(iniesta_attrib.keys())
print p_val
xv = plt.DataFrame({'val':p_val,'keyt':p_key})
y_v = df.columns
p = Scatter(xv,x='keyt',y='val',color='Brown',
               title="Iniesta",width=800,height=600)

output_file("iniesta.html")			
show(p)



 
