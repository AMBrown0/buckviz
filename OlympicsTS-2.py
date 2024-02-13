# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:02:34 2020

@author: andy
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from numpy import mean
%matplotlib inline
pd.set_option('display.max_columns', None)      # show all columns in the console

# download file 'athlete_events.csv' from Moodle or Kaggle 
# read the dataset as a pandas DataFrame
olympics = pd.read_csv('./data/athlete_events.csv')

olympics_win = olympics.dropna(subset=['Medal'])
olympics_win_gb=olympics_win[olympics_win['Team'] == 'Great Britain']
olympics_win_groups=olympics_win.groupby(['Season','Medal'])
olympics_win_gb_yr_grp=olympics_win_gb.groupby(['Year']).count()

x=olympics_win_gb_yr_grp.index
y=olympics_win_gb_yr_grp.Medal.values
plt.figure(figsize=(16,5), dpi=1024)

#plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
plt.show()


#Drop the index and convert to columns
oly=olympics_win_gb_yr_grp.reset_index()
x=oly['Year']
y=oly['Medal']
plt.plot(x, y, color='tab:red')

#plot_df(df, x=df.index, y=df.value, title='Monthly anti-diabetic drug sales in Australia from 1992 to 2008.')    


#plt.plot(x, y, color='tab:red')
#plt.plot('year', 'No. Medals', data=olympics_win_gb_yr_grp, marker='o', 
#markerfacecolor='darkgreen', color='green', linewidth=2)
#plt.title("number of passengers in July between 1949 and 1960")
#plt.xlabel('Year');
#plt.ylabel('number of passengers');