import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('length_data.csv')

#part 1, plot length over years
yrs = list(set(data["Year"]))
nyrs = len(yrs)
avg_game_len = [data["Gm Len"][data["Year"]==yrs[i]].mean() for i in range(nyrs)]
plt.plot(yrs,avg_game_len)
plt.xlabel('Season')
plt.ylabel('Avg Length (minutes)')
plt.title('The Growth of the Average Length of Baseball Games Over Time')

pct95_game_len = [np.percentile(data["Gm Len"][data["Year"]==yrs[i]],95) for i in range(nyrs)]
pct75_game_len = [np.percentile(data["Gm Len"][data["Year"]==yrs[i]],75) for i in range(nyrs)]
pct50_game_len = [np.percentile(data["Gm Len"][data["Year"]==yrs[i]],50) for i in range(nyrs)]
pct25_game_len = [np.percentile(data["Gm Len"][data["Year"]==yrs[i]],25) for i in range(nyrs)]
pct5_game_len = [np.percentile(data["Gm Len"][data["Year"]==yrs[i]],5) for i in range(nyrs)]
plt.figure()
plt.plot(yrs,pct95_game_len,'r')
plt.plot(yrs,pct75_game_len,color='orange')
plt.plot(yrs,pct50_game_len,'y')
plt.plot(yrs,pct25_game_len,'b')
plt.plot(yrs,pct5_game_len,'g')
plt.legend(['95th percentile','3rd quartle','Median','1st quartile','5th percentile'])
plt.title('Percentiles of Game Length Over Time')
plt.xlabel('Year')
plt.ylabel('Game Length')

#avg for 2023 season
data23 = pd.read_csv('data23.csv')
season23_avg_lens=[60*int(data23["Time"][i].split(':')[0])+int(data23["Time"][i].split(':')[1]) for i in range(len(data23["Time"]))]
print("Mean Length of Games: " + str(np.mean(season23_avg_lens))+" Minutes")

#now find the "runs scored per minute" data
avg_game_runs = [data["Runs"][data["Year"]==yrs[i]].mean() + data["Runs Allowed"][data["Year"]==yrs[i]].mean()for i in range(nyrs)]
runs_per_hour = [60*avg_game_runs[i]/avg_game_len[i] for i in range(nyrs)]
plt.figure()
plt.plot(yrs,runs_per_hour,linewidth=2)
plt.xlabel('Year')
plt.ylabel('Runs per Hour of Game Time')

plt.figure()
plt.plot(yrs,avg_game_runs,linewidth=2)
plt.xlabel('Year')
plt.ylabel('Average Runs per Game')

#find team names
modern_data = data[data["Year"]>=2000]
teams = list(set(modern_data["Team"]))
nteams = len(teams)
home_lengths = [modern_data["Gm Len"][modern_data["Team"]==teams[i]].mean() for i in range(nteams)]
home_lengths, teams = (list(t) for t in zip(*sorted(zip(home_lengths, teams))))

avg_since_2k = np.mean(avg_game_len[-15:])
rel_avg=[home_lengths[i]-avg_since_2k for i in range(nteams)]
plt.figure()
plt.bar(teams[-6:],rel_avg[-6:])
plt.ylabel('Average Game Length')
plt.title('Teams with the Longest Games')

plt.figure()
plt.bar(teams[1:6],rel_avg[1:6])
plt.ylabel('Average Game Length')
plt.title('Teams with the Shortest Games')
plt.xticks(rotation='vertical')
