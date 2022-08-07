from cProfile import label
import requests
import matplotlib.pyplot as plt
from pybettor import implied_odds
import json

def return_odds(values, matches, american=False):
    for k in range(len(values)):
        if values[k] == 0.0:
            values[k] = 0.01
        if values[k] == 1.0:
            values[k] = 0.99 

    if american:
        return [implied_odds(x / matches, category="us") for x in values]
    return [round(x / matches * 100, 2) for x in values]

def return_rolling_odds(values, matches, bins, target_index):

    total_histagram_probs = []

    for i in range(1, len(values)):

        counts, edges, bars = plt.hist(values[:i], bins=bins)
        histogram_probs = return_odds(counts, i)

        total_histagram_probs.append(histogram_probs[target_index])
    plt.clf()

    return total_histagram_probs
   
# Previous Tournament 14173 Current Tournament 14417

f = open('pgl.json')
response_json = json.load(f)

# response = requests.get("https://api.opendota.com/api/leagues/14417/matches")
# response_json = response.json()
# with open('pgl.json', 'w') as json_file:
#     json.dump(response_json, json_file)

durations = []
towers = []
barracks = []
barracks_both = []
roshans = []
roshans_both = []
matches = len(response_json)
matches_without_chat = 0

print("Number of matches: ", matches)

for j in range(len(response_json)):

    curr_duration = response_json[j]["duration"] / 60

    if curr_duration < 15:
        matches -= 1
        continue

    durations.append(curr_duration)

    tower_status_radiant = '{0:011b}'.format(response_json[j]["tower_status_radiant"])
    tower_status_dire = '{0:011b}'.format(response_json[j]["tower_status_dire"])
    barracks_status_radiant = '{0:06b}'.format(response_json[j]["barracks_status_radiant"])
    barracks_status_dire = '{0:06b}'.format(response_json[j]["barracks_status_dire"])

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

    roshan_team_2, roshan_team_3 = False, False
    roshan_dcount = 0
    if response_json[j]["objectives"] == None:
        matches_without_chat += 1
    else: 
        for i in response_json[j]["objectives"]:
            if i["type"] == "CHAT_MESSAGE_ROSHAN_KILL":
                roshan_dcount += 1
                if i["team"] == 2:
                    roshan_team_2 = True
                if i["team"] == 3:
                    roshan_team_3 = True
        roshans.append(roshan_dcount)
    if roshan_team_2 and roshan_team_3:
        roshans_both.append(1)
    else:
        roshans_both.append(0)


print("Number of matches without chat: ", matches_without_chat)
matches_adj = matches - matches_without_chat
american = True

fig, ((ax0, ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8, ax9), (ax10, ax11, ax12, ax13, ax4)) = plt.subplots(nrows=3, ncols=5)

counts, edges, bars = ax0.hist(durations, bins=[0,20,30,40,50,60,120])
ax0.bar_label(bars, labels=return_odds(counts, matches, american=american))
ax0.set_title('Durations')

counts, edges, bars = ax5.hist(towers, bins=[0, 9.5, 20])
ax5.bar_label(bars, labels=return_odds(counts, matches, american=american))
ax5.set_title('Towers 9.5')
counts, edges, bars = ax6.hist(towers, bins=[0, 10.5, 20])
ax6.bar_label(bars, labels=return_odds(counts, matches, american=american))
ax6.set_title('Towers 10.5')
counts, edges, bars = ax7.hist(towers, bins=[0, 11.5, 20])
ax7.bar_label(bars, labels=return_odds(counts, matches, american=american))
ax7.set_title('Towers 11.5')
counts, edges, bars = ax8.hist(towers, bins=[0, 12.5, 20])
ax8.bar_label(bars, labels=return_odds(counts, matches, american=american))
ax8.set_title('Towers 12.5')
counts, edges, bars = ax9.hist(towers, bins=[0, 13.5, 20])
ax9.bar_label(bars, labels=return_odds(counts, matches, american=american))
ax9.set_title('Towers 13.5')
counts, edges, bars = ax4.hist(towers, bins=[0, 14.5, 20])
ax4.bar_label(bars, labels=return_odds(counts, matches, american=american))
ax4.set_title('Towers 14.5')

counts, edges, bars = ax10.hist(barracks, bins=[0, 0.5, 14])
ax10.bar_label(bars, labels=return_odds(counts, matches, american=american))
ax10.set_title('Barracks 1.5')
counts, edges, bars = ax11.hist(barracks, bins=[0, 3.5, 14])
ax11.bar_label(bars, labels=return_odds(counts, matches, american=american))
ax11.set_title('Barracks 3.5')
counts, edges, bars = ax12.hist(barracks, bins=[0, 5.5, 14])
ax12.bar_label(bars, labels=return_odds(counts, matches, american=american))
ax12.set_title('Barracks 5.5')
counts, edges, bars = ax13.hist(barracks, bins=[0, 7.5, 14])
ax13.bar_label(bars, labels=return_odds(counts, matches, american=american))
ax13.set_title('Barracks 7.5')

counts, edges, bars = ax1.hist(barracks_both, bins=[0, 1, 2])
ax1.bar_label(bars, labels=return_odds(counts, matches, american=american))
ax1.set_title('Both Barracks')

counts, edges, bars = ax3.hist(roshans, bins=[0, 2.5, 7])
ax3.bar_label(bars, labels=return_odds(counts, matches_adj, american=american))
ax3.set_title('Roshans 2.5')

counts, edges, bars = ax2.hist(roshans_both, bins=[0, 1, 2])
ax2.bar_label(bars, labels=return_odds(counts, matches_adj, american=american))
ax2.set_title('Roshans Both')

plt.figure()

total_histogram_odds = return_rolling_odds(durations, matches, [0,20,30,40,50,60,120], 4)
plt.plot(total_histogram_odds, color='black', ls='-', marker='.')
# plt.set_title('50 Minute Duration')

plt.show()

plt.figure()

total_histogram_odds = return_rolling_odds(barracks, matches, [0, 5.5, 14], 0)
plt.plot(total_histogram_odds, color='black', ls='-', marker='.')
# plt.set_title('Barracks 5.5')

plt.show()