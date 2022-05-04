import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
import scipy.stats as stats

df2010 = pd.read_csv('tables-f/2010f.csv')
df2011 = pd.read_csv('tables-f/2011f.csv')
df2012 = pd.read_csv('tables-f/2012f.csv')
df2013 = pd.read_csv('tables-f/2013f.csv')
df2014 = pd.read_csv('tables-f/2014f.csv')
df2015 = pd.read_csv('tables-f/2015f.csv')
df2016 = pd.read_csv('tables-f/2016f.csv')
df2017 = pd.read_csv('tables-f/2017f.csv')
df2018 = pd.read_csv('tables-f/2018f.csv')
df2019 = pd.read_csv('tables-f/2019f.csv')
df2020 = pd.read_csv('tables-f/2020f.csv')
df2021 = pd.read_csv('tables-f/2021f.csv')
df2022 = pd.read_csv('tables-f/2022f.csv')

frames = [df2010, df2011, df2012, df2013, df2014, df2015, df2016, df2017, df2018, df2019, df2020, df2021, df2022]
result = pd.concat(frames)
result.rename(columns={'Unnamed: 0': 'Rank'}, inplace=True)
# result = result.reset_index()
result.to_csv('result-f.csv', index=False)