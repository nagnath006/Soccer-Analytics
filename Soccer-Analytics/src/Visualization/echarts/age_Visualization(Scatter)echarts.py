import pandas as plt
import sqlite3
from echarts import Echart,Legend,Bar,Axis,Line,Radar,Toolbox,Pie,Map
con = sqlite3.connect("database.sqlite",isolation_level=None)
cur = con.cursor() 	 	
age_set = {}
name = '%iniesta%'
#today = date.today()
cur.execute('select short_passing,long_passing,strength,vision,dribbling,balance,positioning from Player inner join Player_Attributes on Player.player_api_id = Player_Attributes.player_api_id where player_name like ? group by player_name',(name,))

i = list(cur.fetchone())
iniesta_attrib = {"short_passing":i[0],"long_passing":i[1],"strength":i[2],"vision":i[3],"dribbling":i[4],"balance":i[5],"positioning":i[6]}
#labels = ["short_passing","long_passing","strength","vision","dribbling","balance","positioning"]
p_val = list(iniesta_attrib.values())
p_key = list(iniesta_attrib.keys())
print p_val
xv = plt.DataFrame({'val':p_val,'keyt':p_key})
chart = Echart('Andres Iniesta', 'Mid Fielder Attributes')
#chart.use(Bar('Out of 100', p_val))
chart.use(Line('Out of 100', p_val))
chart.use(Legend(['Andres Iniesta']))
chart.use(Axis('category', 'bottom', data=p_key))
chart.plot()
