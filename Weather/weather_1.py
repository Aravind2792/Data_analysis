# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 23:12:35 2020

@author: Achu
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#%%
df_b=pd.read_csv('A:/Work/udacity/data_analysis/course-1/bangalore.csv')    
df_g=pd.read_csv('A:/Work/udacity/data_analysis/course-1/global.csv')
df_i=pd.read_csv('A:/Work/udacity/data_analysis/course-1/india.csv')
df_c=pd.read_csv('A:/Work/udacity/data_analysis/course-1/copenhagen.csv')
df_d=pd.read_csv('A:/Work/udacity/data_analysis/course-1/durban.csv')
df_t=pd.read_csv('A:/Work/udacity/data_analysis/course-1/toronto.csv')
df_r=pd.read_csv('A:/Work/udacity/data_analysis/course-1/rio.csv')
df_s=pd.read_csv('A:/Work/udacity/data_analysis/course-1/sydney.csv')




df_b.head(5)
df_b.isna().sum()
df_b['avg_temp'].fillna(df_b['avg_temp'].mean(),inplace=True)
df_b['avg_temp']=df_b['avg_temp'].astype('float64')
df_b['rolling_mean']=df_b.iloc[:,3].rolling(window=10).mean()

df_g.isna().sum()
df_g['rolling_mean']=df_g.iloc[:,1].rolling(window=10).mean()
df_g2=df_g[df_g['year']>=1796]

df_i.isna().sum()
df_i['avg_temp'].fillna(df_i['avg_temp'].mean(),inplace=True)
df_i['avg_temp']=df_i['avg_temp'].astype('float64')
df_i['rolling_mean']=df_i.iloc[:,3].rolling(window=10).mean()

df_c['avg_temp'].fillna(df_c['avg_temp'].mean(),inplace=True)
df_c['avg_temp']=df_c['avg_temp'].astype('float64')
df_c['rolling_mean']=df_c.iloc[:,3].rolling(window=10).mean()

df_d['avg_temp'].fillna(df_d['avg_temp'].mean(),inplace=True)
df_d['avg_temp']=df_d['avg_temp'].astype('float64')
df_d['rolling_mean']=df_d.iloc[:,3].rolling(window=10).mean()


df_t['avg_temp'].fillna(df_t['avg_temp'].mean(),inplace=True)
df_t['avg_temp']=df_t['avg_temp'].astype('float64')
df_t['rolling_mean']=df_t.iloc[:,3].rolling(window=10).mean()

df_r['avg_temp'].fillna(df_r['avg_temp'].mean(),inplace=True)
df_r['avg_temp']=df_r['avg_temp'].astype('float64')
df_r['rolling_mean']=df_r.iloc[:,3].rolling(window=10).mean()

df_s['avg_temp'].fillna(df_s['avg_temp'].mean(),inplace=True)
df_s['avg_temp']=df_s['avg_temp'].astype('float64')
df_s['rolling_mean']=df_s.iloc[:,3].rolling(window=10).mean()
#%%
plt.figure(1)
plt.subplot(111)
plt.plot(df_b['year'][9:],df_b['rolling_mean'][9:],'red')
plt.xlabel('year',fontsize=15)
plt.plot(df_g2['year'][9:],df_g2['rolling_mean'][9:],'green')
plt.xlabel('Year',fontsize=15)
plt.ylabel('Rolling avg temperature (in deg cel)',fontsize=15)
plt.title('Bangalore vs Global rolling average temperature trend',fontsize=15)
plt.legend(['Banglore','Global'],loc='right',fontsize=10)
plt.yticks(np.arange(0,30,7))
#%%
plt.figure(2)
plt.subplot(121)
plt.plot(df_b['year'],df_b['avg_temp'])
plt.xlabel('year',fontsize=25)
plt.ylabel('Average temperature (in deg cel)',fontsize=25)
plt.title('Bangalore temperature trend',fontsize=25)

plt.subplot(122)
plt.plot(df_g['year'],df_g['avg_temp'])
plt.xlabel('year',fontsize=25)
plt.ylabel('Average temperature (in deg cel)',fontsize=25)
plt.title('Global temperature trend',fontsize=25)

plt.figure(3)
plt.scatter(df_i['year'][9:],df_i['rolling_mean'][9:])
plt.xlabel('year')
plt.ylabel('Rolling avg temperature (in deg cel)')
plt.title('India temperature trend')

plt.figure(4)
plt.subplot(121)
plt.hist(df_i['avg_temp'],linewidth=1.2,edgecolor = 'black')
plt.xlabel('Temperature (in deg cel)')
plt.ylabel('Frequency')
plt.title('India temperature frequency')

plt.subplot(122)
plt.hist(df_b['avg_temp'],linewidth=1.2,edgecolor = 'black')
plt.xlabel('Temperature (in deg cel)')
plt.ylabel('Frequency')
plt.title('Banglore temperature frequency')


plt.figure(5)
plt.subplot(121)
plt.hist(df_g['avg_temp'])
plt.xlabel('Temperature  (in deg cel)')
plt.ylabel('Frequency')
plt.title('Global temperature frequency')
#%%
plt.figure(6)
plt.subplot(231)
plt.plot(df_b['year'][9:],df_b['rolling_mean'][9:])
plt.xlabel('Years')
plt.ylabel('Rolling avg Temperature  (in deg cel)')
plt.title('Bangalore temperature frequency')

plt.subplot(232)
plt.plot(df_s['year'][9:],df_s['rolling_mean'][9:])
plt.xlabel('Years')
plt.ylabel('Rolling avg Temperature  (in deg cel)')
plt.title('Sydney temperature frequency')


plt.subplot(233)
plt.plot(df_d['year'][9:],df_d['rolling_mean'][9:])
plt.xlabel('Years')
plt.ylabel('Rolling avg Temperature  (in deg cel)')
plt.title('Durban temperature frequency')

plt.subplot(234)
plt.plot(df_c['year'][9:],df_c['rolling_mean'][9:])
plt.xlabel('Years')
plt.ylabel('Rolling avg Temperature  (in deg cel)')
plt.title('Copenhagen temperature frequency')

plt.subplot(235)
plt.plot(df_t['year'][9:],df_t['rolling_mean'][9:])
plt.xlabel('Years')
plt.ylabel('Rolling avg Temperature  (in deg cel)')
plt.title('Toronto temperature frequency')

plt.subplot(236)
plt.plot(df_r['year'][9:],df_r['rolling_mean'][9:])
plt.xlabel('Years')
plt.ylabel('Rolling avg Temperature  (in deg cel)')
plt.title('Rio de Janeiro temperature frequency')

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.35,
                    wspace=0.35)

plt.show()

from scipy import stats
slope1=stats.linregress(df_b['year'],df_b['avg_temp'])
slope2=stats.linregress(df_g['year'],df_g['avg_temp'])
slope3=stats.linregress(df_i['year'],df_i['avg_temp'])
slope4=stats.linregress(df_s['year'],df_s['avg_temp'])
slope5=stats.linregress(df_d['year'],df_d['avg_temp'])
slope6=stats.linregress(df_c['year'],df_c['avg_temp'])
slope7=stats.linregress(df_t['year'],df_t['avg_temp'])
slope8=stats.linregress(df_r['year'],df_r['avg_temp'])



print('The rate of change through the years for bangalore is',slope1.slope, 
      'The rate of change through the years for Global temperature is',slope2.slope,
      'The rate of change through the years for India temperature is',slope3.slope)
print('The rate of change through the years for Sydney temperature is',slope4.slope)
print('The rate of change through the years for Durban temperature is',slope5.slope)
print('The rate of change through the years for Copenhagen temperature is',slope6.slope)
print('The rate of change through the years for Toronto temperature is',slope7.slope)
print('The rate of change through the years for Rio De Janeiro temperature is',slope8.slope)



#%%

bang_50=df_b[df_b['year']>1970]
syd_50=df_s[df_s['year']>1970]
dur_50=df_d[df_d['year']>1970]
cop_50=df_c[df_c['year']>1970]
tor_50=df_t[df_t['year']>1970]
rio_50=df_r[df_r['year']>1970]
tot_50=df_g[df_g['year']>1970]

slope1a=stats.linregress(bang_50['year'],bang_50['avg_temp'])
slope2a=stats.linregress(syd_50['year'],syd_50['avg_temp'])
slope3a=stats.linregress(dur_50['year'],dur_50['avg_temp'])
slope4a=stats.linregress(cop_50['year'],cop_50['avg_temp'])
slope5a=stats.linregress(tor_50['year'],tor_50['avg_temp'])
slope7a=stats.linregress(rio_50['year'],rio_50['avg_temp'])
slope8a=stats.linregress(tot_50['year'],tot_50['avg_temp'])


print('The rate of change through the years for Bangalore temperature is',slope1a.slope)
print('The rate of change through the years for Sydney temperature is',slope2a.slope)
print('The rate of change through the years for Durban temperature is',slope3a.slope)
print('The rate of change through the years for Copenhagen temperature is',slope4a.slope)
print('The rate of change through the years for Toronto temperature is',slope5a.slope)
print('The rate of change through the years for Rio De Janeiro temperature is',slope7a.slope)
print('The rate of change through the years for Global temperature is',slope8a.slope)

#%%
plt.figure(7)
plt.subplot(231)
plt.plot(bang_50['year'],bang_50['rolling_mean'])
plt.xlabel('Years')
plt.ylabel('Rolling avg Temperature (in deg cel)')
plt.title('Bangalore Temperature ')

plt.subplot(232)
plt.plot(syd_50['year'],syd_50['rolling_mean'])
plt.xlabel('Years')
plt.ylabel('Rolling avg Temperature (in deg cel)')
plt.title('Sydney temperature')


plt.subplot(233)
plt.plot(dur_50['year'],dur_50['rolling_mean'])
plt.xlabel('Years')
plt.ylabel('Rolling avg Temperature (in deg cel)')
plt.title('Durban temperature ')

plt.subplot(234)
plt.plot(cop_50['year'],cop_50['rolling_mean'])
plt.xlabel('Years')
plt.ylabel('Rolling avg Temperature (in deg cel)')
plt.title('Copenhagen temperature ')

plt.subplot(235)
plt.plot(tor_50['year'],tor_50['rolling_mean'])
plt.xlabel('Years')
plt.ylabel('Rolling avg Temperature (in deg cel)')
plt.title('Toronto temperature ')

plt.subplot(236)
plt.plot(rio_50['year'],rio_50['rolling_mean'])
plt.xlabel('Years')
plt.ylabel('Rolling avg Temperature (in deg cel)')
plt.title('Rio de Janeiro temperature frequency')

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.35,
                    wspace=0.35)

plt.show()
#%%
print('The max temp in bangalore through the years',max(df_b.avg_temp))
print('The min temp in bangalore through the years',min(df_b.avg_temp))
print('The max temp in global through the years',max(df_g.avg_temp))
print('The min temp in Global through the years',min(df_g.avg_temp))
print('The avg temperature for India through the years',df_g['avg_temp'].mean())
print('The avg temperature for bangalore through the years',df_b['avg_temp'].mean())

print('The max temp in Sydney through the years',max(df_s.avg_temp))
print('The min temp in Sydney through the years',min(df_s.avg_temp))
print('The max temp in Durban through the years',max(df_d.avg_temp))
print('The min temp in Durban through the years',min(df_d.avg_temp))
print('The avg temperature for Sydney through the years',df_s['avg_temp'].mean())
print('The avg temperature for Durban through the years',df_d['avg_temp'].mean())

print('The max temp in Copenhagen through the years',max(df_c.avg_temp))
print('The min temp in Copenhagen through the years',min(df_c.avg_temp))
print('The max temp in Toronto through the years',max(df_t.avg_temp))
print('The min temp in Toronto through the years',min(df_t.avg_temp))
print('The avg temperature for Copenhagen through the years',df_c['avg_temp'].mean())
print('The avg temperature for Toronto through the years',df_t['avg_temp'].mean())

print('The max temp in Rio through the years',max(df_r.avg_temp))
print('The min temp in Rio through the years',min(df_r.avg_temp))
print('The avg temperature for Rio through the years',df_r['avg_temp'].mean())
#%%

import statistics as st
b_med=stats.mode(df_b.avg_temp)
s_med=stats.mode(df_s.avg_temp)
d_med=stats.mode(df_d.avg_temp)
c_med=stats.mode(df_c.avg_temp)
t_med=stats.mode(df_t.avg_temp)
r_med=stats.mode(df_r.avg_temp)
g_med=stats.mode(df_g.avg_temp)

b_std=st.stdev(df_b.avg_temp)
s_std=st.stdev(df_s.avg_temp)
d_std=st.stdev(df_d.avg_temp)
c_std=st.stdev(df_c.avg_temp)
t_std=st.stdev(df_t.avg_temp)
r_std=st.stdev(df_r.avg_temp)
g_std=st.stdev(df_g.avg_temp)




