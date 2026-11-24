import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/Users/move/Python/freecodecamp/medical_examination.csv')

columns = ['age', 'height', 'weight', 'sex', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio']

def get_card(p_id):
    row = df[df['id']==p_id].iloc[0]
    output = {
        'Feature': ['Age', 'Height', 'Weight', 'Gender', 'Systolic Blood Pressure', 'Diastolic Blood Pressure', 'Cholesterol', 'Glucose', 'Smoking', 'Alcohol Intake', 'Physical Activity', 'Presence or absence of cardiovascular disease','Overweight'],
        'Variable Type': ['Objective Feature', 'Objective Feature', 'Objective Feature', 'Objective Feature', 'Examination Feature', 'Examination Feature', 'Examination Feature', 'Examination Feature', 'Subjective Feature', 'Subjective Feature', 'Subjective Feature', 'Target Variable', 'Subjective Feature'],
        'Variable': [row[x] if x not in ['cholesterol', 'gluc'] else (1 if row[x] == 0 else 1) for x in columns] + [1 if row['weight'] / ((row['height'] / 100) ** 2) > 25 else 0],
        'Value Type': ['int (days)', 'int (cm)', 'float (kg)', 'categorical code', 'int', 'int', '1: normal, 2: above normal, 3: well above normal', '1: normal, 2: above normal, 3: well above normal', 'binary', 'binary', 'binary', 'binary', 'binary']
    }
    return output   
df1 = pd.DataFrame(get_card(87876), columns=['Feature', 'Variable Type', 'Variable', 'Value Type'])
print(df1.to_string(index=False))

def draw_cat_plot(df):
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = df_cat.groupby(['cardio']).size().reset_index(name='total')
    chart = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar')
    fig = chart.fig
    fig.savefig('catplot.png')
    return fig


def draw_heat_map(df):
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))
                 ]
    corr = df_heat.corr()
    return sns.heatmap(corr)

