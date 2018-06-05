import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from bokeh.models import ColumnDataSource, DataRange1d, Plot, LinearAxis, Grid
from bokeh.models.glyphs import HBar
from bokeh.io import curdoc, show

name = str(input("Enter TeamName : "))
df = pd.read_csv("E0.csv")

def GetHomeWin_percentage(TeamName):
    '''To Get the Hometea winning rate'''
    input_team = df[df.HomeTeam == TeamName]
    win_rate = (float(len(input_team[input_team.FTR == "H"]))/float(len(input_team))) * 100
    plt.barh([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],list(input_team["FTHG"]),align='center')
    plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], list(input_team ["AwayTeam"]))
    plt.xlabel(TeamName + " " + "Goals")
    plt.title(TeamName + " " + "Home Winrate is {}%".format(win_rate))
    plt.show() 
    return 

GetHomeWin_percentage(name)




