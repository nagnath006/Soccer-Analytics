import pandas as pd
from bokeh.layouts import row,gridplot
from bokeh.io import show, output_file,vplot
from bokeh.plotting import figure

name = str(input("Enter TeamName : "))
df = pd.read_csv("E0.csv")

def GetHomeWin_percentage(TeamName):
    output_file("layout_grid.html")
    '''To Get the Hometea winning rate'''
    input_team_Home = df[df.HomeTeam == TeamName]
    win_rate_Home = (float(len(input_team_Home[input_team_Home.FTR == "H"]))/float(len(input_team_Home))) * 100
    teams_Home = list(input_team_Home["AwayTeam"])
    goals_Home = list(input_team_Home["FTHG"])
    p = figure(x_range=teams_Home, plot_height=325, width = 624, title= TeamName + " " + "Home Winrate is {}%".format(win_rate_Home),x_axis_label="Teams", y_axis_label= "No of goals scored by" + " " + TeamName)
    p.background_fill_color = "beige"
    p.title.text_font_size = '15pt'
    p.background_fill_alpha = 0.5
    p.vbar(x=teams_Home,top = goals_Home, width=0.5)
    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    # Away Scene
    
    input_team_Away = df[df.AwayTeam == TeamName]
    win_rate_Away = (float(len(input_team_Away[input_team_Away.FTR == "A"]))/float(len(input_team_Away))) * 100
    teams_Away = list(input_team_Away["HomeTeam"])
    goals_Away = list(input_team_Away["FTAG"])
    p1 = figure(x_range=teams_Away, plot_height=325, width = 624, title= TeamName + " " + "Away Winrate is {}%".format(win_rate_Away),x_axis_label="Teams", y_axis_label= "No of goals scored by" + " " + TeamName)
    p1.background_fill_color = "beige"
    p1.title.text_font_size = '15pt'
    p1.background_fill_alpha = 0.5
    p1.vbar(x=teams_Away,top = goals_Away, width=0.5)

    p1.xgrid.grid_line_color = None
    p1.y_range.start = 0
    

    #Yellow Cards Away
    
    #input_team_Away = df[df.AwayTeam == TeamName]
    PerMatch = (float(sum(list(input_team_Away["AY"])))/float(len(input_team_Away))) 
    #teams_Away = list(input_team_Away["HomeTeam"])
    goals_Away1 = list(input_team_Away["AY"])
    p2 = figure(x_range=teams_Away, plot_height=325, width = 624, title= TeamName + " " + "Yellow card permatch (as Away) {}%".format(PerMatch),x_axis_label="Teams", y_axis_label= "No of YellowCards got by" + " " + TeamName)
    p2.background_fill_color = "yellow"
    p2.title.text_font_size = '12pt'
    p2.background_fill_alpha = 0.5
    p2.vbar(x=teams_Away,top = goals_Away1, width=0.5)

    p2.xgrid.grid_line_color = None
    p2.y_range.start = 0

    #yellow cards Home

    PerMatch = (float(sum(list(input_team_Home["AY"])))/float(len(input_team_Home))) 
    goals_Away2 = list(input_team_Home["AY"])
    p3 = figure(x_range=teams_Home, plot_height=325, width = 624, title= TeamName + " " + "Yellow card permatch (as Home) {}%".format(PerMatch),x_axis_label="Teams", y_axis_label= "No of YellowCards got by" + " " + TeamName)
    p3.background_fill_color = "yellow"
    p3.title.text_font_size = '12pt'
    p3.background_fill_alpha = 0.5
    p3.vbar(x=teams_Away,top = goals_Away2, width=0.5)

    p3.xgrid.grid_line_color = None
    p3.y_range.start = 0
    grid = gridplot([[p, p1], [p3, p2]])

    # show the results
    show(grid)
    
    return win_rate_Home



GetHomeWin_percentage(name)
#GetAwayWin_Percentage(name)




