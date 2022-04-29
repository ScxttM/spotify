import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
import scipy.stats as stats

df2010 = pd.read_csv('2010.csv')
df2011 = pd.read_csv('2011.csv')
df2012 = pd.read_csv('2012.csv')
df2013 = pd.read_csv('2013.csv')
df2014 = pd.read_csv('2014.csv')
df2015 = pd.read_csv('2015.csv')
df2016 = pd.read_csv('2016.csv')
df2017 = pd.read_csv('2017.csv')
df2018 = pd.read_csv('2018.csv')
df2019 = pd.read_csv('2019.csv')
df2020 = pd.read_csv('2020.csv')
df2021 = pd.read_csv('2021.csv')
df2022 = pd.read_csv('2022.csv')

frames = [df2010, df2011, df2012, df2013, df2014, df2015, df2016, df2017, df2018, df2019, df2020, df2021, df2022]
result = pd.concat(frames)
result.rename(columns={'Unnamed: 0': 'Rank'}, inplace=True)
# result = result.reset_index()
result.to_csv('result.csv', index=False)