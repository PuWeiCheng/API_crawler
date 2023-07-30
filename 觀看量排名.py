# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 10:47:50 2022

@author: wayne
"""

from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

##中文呈現
#plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
#plt.rcParams['axes.unicode_minus'] = False #windows
plt.rcParams["font.family"] = 'Arial Unicode MS' #mac
##讀取檔案
data=pd.read_csv('video_Details(曉涵哥來了).csv',encoding='utf_8_sig')
top_video_views =data.sort_values(by='Views', ascending=False).head(10)

#print(top_video)
##前十名觀看量影片
ax1 = sns.barplot(x='Views',y='Title',data = top_video_views)
ax1.set_title("觀看量前十名")
ax1.set_xlabel('觀看量') 
ax1.set_ylabel('') 
