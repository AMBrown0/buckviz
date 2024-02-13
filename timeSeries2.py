import matplotlib.pyplot as plt
import seaborn as sns
# upload dataset
flights_df = sns.load_dataset("flights")
# include only July flights in each year
flights_df= flights_df[flights_df.month=="July"]
# plot
plt.plot('year', 'passengers', data=flights_df, marker='o', 
markerfacecolor='darkgreen', color='green', linewidth=2)
plt.title("number of passengers in July between 1949 and 1960")
plt.xlabel('Year');
plt.ylabel('number of passengers');


