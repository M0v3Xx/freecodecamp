import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/Users/move/Python/freecodecamp/fcc-forum-pageviews.csv', index_col='date')


clean_df = df[(df['value'] >= df['value'].quantile(0.025)) &
              (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot(df):
    df_copy = df.copy()
    df_copy['value'].plot(kind='line', figsize=(14,8), color='r')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.show()

def draw_bar_plot(df):
    df_copy = df.copy()
    dt = pd.to_datetime(df_copy.index)
    df_copy['year'] = dt.year
    df_copy['month'] = dt.month
    df_copy = df_copy.groupby(['year', 'month'])['value'].mean().unstack()
    df_copy.plot(kind='bar', figsize=(10, 8))
    plt.xlabel('Years')
    plt.ylabel ('Average Page Views')
    plt.legend(title='Months', labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    plt.show()

def draw_box_plot(df):
    df_copy = df.copy() 
    dt = pd.to_datetime(df_copy.index)
    df_copy['year'] = dt.year
    df_copy['month'] = dt.strftime('%b')

    fig, axes = plt.subplots(1, 2, figsize=(20, 8))
    sns.boxplot(data=df_copy, x='year', y='value', ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')


    sns.boxplot(data=df_copy, x='month', y='value', ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')


    plt.show()

draw_box_plot(clean_df)