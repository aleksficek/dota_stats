import requests
import matplotlib.pyplot as plt
import statistics

# print(statistics.stdev([1, 3, 5, 7, 9, 11]))

# durations = [36.03333333333333, 39.416666666666664, 32.28333333333333, 35.483333333333334, 34.63333333333333, 57.85, 42.11666666666667, 37.38333333333333, 52.7, 24.633333333333333, 29.133333333333333, 23.85, 34.233333333333334, 71.78333333333333, 45.75, 37.016666666666666, 38.3, 26.183333333333334, 33.03333333333333, 36.916666666666664, 40.55, 31.166666666666668, 28.65, 50.38333333333333, 32.18333333333333, 36.95, 49.35, 47.0, 34.86666666666667, 22.633333333333333, 49.233333333333334, 36.71666666666667, 30.316666666666666, 40.6, 37.36666666666667, 31.7, 33.583333333333336, 38.78333333333333, 42.06666666666667, 41.11666666666667, 28.8, 34.766666666666666, 32.15, 35.083333333333336, 36.68333333333333, 32.35, 34.43333333333333, 22.066666666666666, 32.93333333333333, 34.05, 32.266666666666666, 51.85]
# towers = [11, 12, 9, 14, 12, 16, 14, 15, 17, 7, 5, 4, 12, 16, 13, 6, 12, 4, 9, 12, 13, 8, 10, 12, 9, 9, 17, 14, 10, 9, 15, 9, 9, 14, 10, 14, 8, 10, 15, 15, 10, 9, 9, 10, 11, 11, 15, 9, 12, 8, 10, 15]
# barracks = [3, 6, 2, 4, 6, 4, 6, 6, 7, 0, 0, 0, 6, 7, 2, 0, 4, 0, 4, 4, 4, 2, 2, 0, 2, 1, 8, 6, 6, 4, 1, 4, 3, 0, 2, 6, 2, 2, 4, 6, 4, 2, 0, 2, 1, 2, 6, 3, 4, 0, 4, 4]
# barracks_both = [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]


# response = requests.get("https://api.opendota.com/api/leagues/14173/matches")

# durations = []
# towers = []
# barracks = []
# barracks_both = []
# matches = len(response.json())

# print("Number of matches: ", matches)

# for j in range(len(response.json())):
#     curr_duration = response.json()[j]["duration"]
#     durations.append(curr_duration / 60)

#     tower_status_radiant = '{0:011b}'.format(response.json()[j]["tower_status_radiant"])
#     tower_status_dire = '{0:011b}'.format(response.json()[j]["tower_status_dire"])
#     barracks_status_radiant = '{0:06b}'.format(response.json()[j]["barracks_status_radiant"])
#     barracks_status_dire = '{0:06b}'.format(response.json()[j]["barracks_status_dire"])

#     tower_dcount = 0
#     for i in tower_status_radiant:
#         if i == '0':
#             tower_dcount += 1
#     for i in tower_status_dire:
#         if i == '0':
#             tower_dcount += 1
#     towers.append(tower_dcount)


#     barracks_dcount = 0
#     r_barrack, d_barrack = False, False
#     for i in barracks_status_radiant:
#         if i == '0':
#             r_barrack = True
#             barracks_dcount += 1
#     for i in barracks_status_dire:
#         if i == '0':
#             d_barrack = True
#             barracks_dcount += 1
#     barracks.append(barracks_dcount)
    
#     if r_barrack and d_barrack:
#         barracks_both.append(1)
#     else:
#         barracks_both.append(0)

# print("Durations std: ", statistics.stdev(durations))
# print("Towers std: ", statistics.stdev(towers))
# print("Barracks std: ", statistics.stdev(barracks))
# print("Barracks both std: ", statistics.stdev(barracks_both))

# Durations std:  9.023027243799053
# Towers std:  2.9446412006506035
# Barracks std:  2.1614172893151227
# Barracks both std:  0.24855632476172143

# durations_std = 9.023027243799053
# towers_std = 2.9446412006506035
# barracks_std = 2.1614172893151227
# barracks_both = 0.24855632476172143

# # 95% confidence
# print("Duration Sample Size: ", (1.96 * durations_std / 2)**2)
# print("Towers Sample Size: ", (1.96 * towers_std / 0.4)**2)
# print("Barracks Sample Size: ", (1.96 * barracks_std / 0.1)**2)
# print("Barracks Both Sample Size: ", (1.96 * barracks_both / 0.05)**2)

