# Aim:-Implementation of Python Libraries for ML application such as Pandas and Matplotlib

import pandas as pd
import matplotlib.pyplot as plt


data = {
'Year': [2010, 2011, 2012, 2013, 2014],
'Sales': [100, 120, 140, 160, 80]
}
df = pd.DataFrame(data)


# A figure for the line plot
plt.figure(figsize=(8, 4))
plt.plot(df['Year'], df['Sales'], marker='o', linestyle='-', color='b', label='Sales')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales Over the Years')
plt.legend()
plt.grid(False)


# figure for the scatter plot
plt.figure(figsize=(8, 4))
plt.scatter(df['Year'], df['Sales'], color='r', marker='o', label='Dot Graph')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Dot Graph Over the Years')
plt.legend()
plt.grid(False)
plt.show()