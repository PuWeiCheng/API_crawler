# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:11:06 2022

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
data=pd.read_csv('video_Details(JR Lee Radio).csv',encoding='utf_8_sig')
top_video_like =data.sort_values(by='Like', ascending=False).head(10)

#print(top_video)
##前十名觀看量影片
ax1 = sns.barplot(x='Like',y='Title',data = top_video_like)
ax1.set_title("喜歡數前十名")
ax1.set_xlabel('喜歡數') 
ax1.set_ylabel('標題') 

