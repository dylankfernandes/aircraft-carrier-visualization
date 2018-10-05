import quandl
import pandas as pd
import csv
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
api_key = open('../../practice/api-key.txt', 'r').read()

df = pd.read_html('https://en.wikipedia.org/wiki/List_of_aircraft_carriers')

countries = df[1].iloc[:-1, 0]
totals = df[1].iloc[:-1,-1]

fig = plt.figure()
plt.bar(countries, totals)
plt.show()

print(countries)