import numpy as np
import pandas as pd

df = pd.read_csv('/Users/move/Python/freecodecamp/adult.data.csv')


def race_count(df):
    unique_count = df['race'].value_counts()
    return unique_count
print('How many people of each race are represented in this dataset? ')
df_1 = pd.DataFrame(race_count(df))
print(df_1)

def avg_age_men(df):
    avg_age = df[df['sex']=='Male']['age'].mean()
    return round(avg_age, 0)
print('What is the average age of men?')
print(avg_age_men(df))

def bs_degree(df):
    percentage = (len(df[df['education']=='Bachelors']) / len(df)) * 100
    return percentage
print("What is the percentage of people who have a Bachelor's degree?")
print(bs_degree(df))

def fifty_k(df):
    h_education = df[df['education'].isin(['Bachelors','Masters','Doctorate'])]
    fifty_k_p = round((h_education[h_education['salary'] == '>50K']['education'].value_counts() / h_education['education'].value_counts()) * 100, 2)
    return fifty_k_p
print("What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?")
df_4 = pd.DataFrame(fifty_k(df))
print(df_4)

def no_edu(df):
    no_education = df[~df['education'].isin(['Bachelors','Masters','Doctorate'])]
    no_edu_p = round((no_education[no_education['salary']=='>50K']['education'].value_counts() / no_education['education'].value_counts()) * 100, 2)
    return no_edu_p
print("What percentage of people without advanced education make more than 50K?")
df_5 = pd.DataFrame(no_edu(df))
print(df_5)

def min_work_hours(df):
    min_hours = df['hours-per-week'].min()
    return min_hours
print("What is the minimum number of hours a person works per week?")
print(min_work_hours(df))

def min_50k(df):
    min_worker = df[df['hours-per-week'] == df['hours-per-week'].min()]
    min_50k_p = round((len(min_worker[min_worker['salary'] == '>50K']) / len(min_worker)) * 100,2)
    return min_50k_p
print("What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?")
print(min_50k(df))

def country_50k(df):
    country_salary_50k = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_salary_all = df['native-country'].value_counts()
    country_50k_p = round((country_salary_50k / country_salary_all) * 100, 2)
    return country_50k_p
print("What country has the highest percentage of people that earn >50K and what is that percentage?")
df_8 = pd.DataFrame(country_50k(df))
print(df_8)

def india_50k_occupation(df, top_positions=25):
    india_only = df[df['native-country'] == 'India']
    india_50k = india_only[india_only['salary'] == '>50K']['occupation'].value_counts()
    return india_50k.head(top_positions)
print("Identify the most popular occupation for those who earn >50K in India.")
df_9 = pd.DataFrame(india_50k_occupation(df))
print(df_9)

