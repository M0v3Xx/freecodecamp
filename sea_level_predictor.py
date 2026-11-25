import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv('/Users/move/Python/freecodecamp/epa-sea-level.csv')


fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue')

regression_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
x_pred_all = np.arange(1880, 2051)
y_pred_all = regression_all.intercept + regression_all.slope * x_pred_all
ax.plot(x_pred_all, y_pred_all, color='red', label='Regression Line (All Data)')

regression_2000th = linregress(df[df['Year'] >= 2000]['Year'], df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
x_pred_2000th = np.arange(2000, 2051)
y_pred_2000th = regression_2000th.intercept + regression_2000th.slope * x_pred_2000th
ax.plot(x_pred_2000th, y_pred_2000th, color='g', label='Regression Line (2000 and later)')

plt.title('Rise in Sea Level')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.savefig('sea_level_plot.png')
