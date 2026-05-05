import pandas as pd   
import matplotlib.pyplot as plt
df = pd.read_csv('alumni_clean.csv', index_col='Id')

df['Age'] = df['Exit_Year'] - df['Birth_Year']
print(df.head())

df = df[df['Age']>7]
df_age_24 = df[df['Age']==24]
df = df[df['Age']<24]

df_sorted = df.sort_values(by = 'Exit_Year')
print(df_sorted.head())
print(df_sorted.tail())

df_66_90 = df[(df['Exit_Year'] >= 1866) & (df['Exit_Year'] <= 1890)]
df_91_15 = df[(df['Exit_Year'] >= 1891) & (df['Exit_Year'] <= 1915)]
df_16_40 = df[(df['Exit_Year'] >= 1916) & (df['Exit_Year'] <= 1940)]
df_41_64 = df[(df['Exit_Year'] >= 1941) & (df['Exit_Year'] <= 1964)]
df_65_90 = df[(df['Exit_Year'] >= 1965) & (df['Exit_Year'] <= 1990)]


df_65_90.plot.scatter(x='Exit_Year', y='Age')
plt.xlabel('Year of Exit')
plt.ylabel('Age')
plt.title('Year of Exit against Age (1965-1990)')
plt.show()
# I just switch the numbers in df_65_90 for each graph, so I don't print out all the graphs at the same time.

df_mean = df.groupby('Exit_Year')['Age'].mean()

df_mean.plot(x='Exit_Year', y='Age')
plt.xlabel('Year of Exit')
plt.ylabel('Age')
plt.title('Year of Exit against mean Age')
plt.show()
