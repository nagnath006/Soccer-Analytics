import pandas as plt
import sqlite3
import matplotlib.pyplot as pyp
import matplotlib.pylab as plt
from matplotlib import colors
from datetime import datetime,date
from dateutil import parser

con = sqlite3.connect("database.sqlite")
cur = con.cursor() 	 	
age_set = {}
today = date.today()
for i in cur.execute('select player_name,birthday from player LIMIT 30'):
    x =  str(i[0]).split(' ')
    formatted_date = parser.parse(i[1])
    age= today.year - formatted_date.year - ((today.month, today.day) < (formatted_date.month,formatted_date.day))
    age_set[str(i[0])] = age
pyp.bar(range(len(age_set)),age_set.values(),align='center',color='red')
pyp.xticks(range(len(age_set)),age_set.keys(),rotation='vertical')
pyp.ylabel("AGE");
for a,b in zip(range(len(age_set)),age_set.values()):
    plt.text(a, b, str(b))
pyp.show()