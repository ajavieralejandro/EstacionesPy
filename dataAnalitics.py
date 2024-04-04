import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

estaciones = pd.read_csv('estaciones.csv')

df = pd.read_csv('estaciones.csv')
avg_column = df['temperature'].mean()
print("Average of temperature:", avg_column)
avg_column = df['feels_like'].mean()
print("Average of feels like:", avg_column)
avg_column = df['humidity'].mean()
print("Average of humidity like:", avg_column)
avg_column = df['wind'].mean()
print("Average of wind like:", avg_column)
avg_column = df['wind_gust'].mean()
print("Average of wind gust like:", avg_column)
