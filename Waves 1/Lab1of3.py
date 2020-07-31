reservoir_volume = 4.445 * 10**8
rainfall = 5 * 10**6
# decrease the rainfall variable by 10% to account for runoff
rainfall = rainfall * 0.01
# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall
# increase reservoir_volume by 5% to account for stormwater that flows into the reservoir in the days following the storm
reservoir_volume = reservoir_volume / 0.05
# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume = reservoir_volume * 0.05
# subtract 2.5e5 cubic metres from reservoir_volume to account for water that's piped to arid regions.
reservoir_volume -= 2500000
print(reservoir_volume)