from cProfile import label
import requests
import matplotlib.pyplot as plt

response = requests.get("https://api.opendota.com/api/leagues/14417/matches")

durations = []
towers = []
barracks = []
barracks_both = []
matches = len(response.json())

print("Number of matches: ", matches)

for j in range(len(response.json())):
    curr_duration = response.json()[j]["duration"]
    durations.append(curr_duration / 60)

    tower_status_radiant = '{0:011b}'.format(response.json()[j]["tower_status_radiant"])
    tower_status_dire = '{0:011b}'.format(response.json()[j]["tower_status_dire"])
    barracks_status_radiant = '{0:06b}'.format(response.json()[j]["barracks_status_radiant"])
    barracks_status_dire = '{0:06b}'.format(response.json()[j]["barracks_status_dire"])

    tower_dcount = 0
    for i in tower_status_radiant:
        if i == '0':
            tower_dcount += 1
    for i in tower_status_dire:
        if i == '0':
            tower_dcount += 1
    towers.append(tower_dcount)


    barracks_dcount = 0
    r_barrack, d_barrack = False, False
    for i in barracks_status_radiant:
        if i == '0':
            r_barrack = True
            barracks_dcount += 1
    for i in barracks_status_dire:
        if i == '0':
            d_barrack = True
            barracks_dcount += 1
    barracks.append(barracks_dcount)
    
    if r_barrack and d_barrack:
        barracks_both.append(1)
    else:
        barracks_both.append(0)

# response = requests.get("https://api.opendota.com/api/leagues/14391/matches")

# for i in range(len(response.json())):
#     curr_duration = response.json()[i]["duration"]
#     durations.append(curr_duration / 60)



fig, ((ax0, ax1, axnull), (ax2, ax3, ax4), (ax5, ax6, ax7)) = plt.subplots(nrows=3, ncols=3)

counts, edges, bars = ax0.hist(durations, bins=[0,20,30,40,50,60,120])
ax0.bar_label(bars, labels=[round(x / matches * 100, 2) for x in counts])
ax0.set_title('Durations')

counts, edges, bars = axnull.hist(towers, bins=[0, 11.5, 20])
axnull.bar_label(bars, labels=[round(x / matches * 100, 2) for x in counts])
axnull.set_title('Towers 11.5')
counts, edges, bars = ax2.hist(towers, bins=[0, 12.5, 20])
ax2.bar_label(bars, labels=[round(x / matches * 100, 2) for x in counts])
ax2.set_title('Towers 12.5')
counts, edges, bars = ax3.hist(towers, bins=[0, 13.5, 20])
ax3.bar_label(bars, labels=[round(x / matches * 100, 2) for x in counts])
ax3.set_title('Towers 13.5')
counts, edges, bars = ax4.hist(towers, bins=[0, 14.5, 20])
ax4.bar_label(bars, labels=[round(x / matches * 100, 2) for x in counts])
ax4.set_title('Towers 14.5')


counts, edges, bars = ax5.hist(barracks, bins=[0, 0.5, 14])
ax5.bar_label(bars, labels=[round(x / matches * 100, 2) for x in counts])
ax5.set_title('Barracks 1.5')
counts, edges, bars = ax6.hist(barracks, bins=[0, 3.5, 14])
ax6.bar_label(bars, labels=[round(x / matches * 100, 2) for x in counts])
ax6.set_title('Barracks 3.5')
counts, edges, bars = ax7.hist(barracks, bins=[0, 5.5, 14])
ax7.bar_label(bars, labels=[round(x / matches * 100, 2) for x in counts])
ax7.set_title('Barracks 5.5')

counts, edges, bars = ax1.hist(barracks_both, bins=[0, 1, 2])
ax1.bar_label(bars, labels=[round(x / matches * 100, 2) for x in counts])
ax1.set_title('Both Barracks')

plt.show()


