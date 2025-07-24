from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D8
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in a list
results = []
num_rolls = 10_000
for num_roll in range(num_rolls): # roll die 1000 times
    result = die_1.roll() + die_2.roll()
    results.append(result) # store the result

# Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides # join the two dies result 12
for value in range(2, max_result+1): # loop through the 12 side
    frequency = results.count(value) # count how many time a number repeated
    frequencies.append(frequency) # store the frequency 

# Visualize the results
x_values = list(range(2, max_result+1)) # convert the range in a list and display the result on the vertical of the chart.

data = [Bar(x=x_values, y=frequencies)] # set the data in a bar chart 
title = f'Result of rolling a D8 {num_rolls:,} times.'

x_axis_config = {'title': 'Result', 'dtick':1} # xaxis (result of two D8s)

y_axis_config = {'title': 'Frequency of Result'} # yaxis (how often each result occured)

my_layout = Layout(title=title, xaxis=x_axis_config, yaxis=y_axis_config) # set the chart layout

offline.plot({'data': data, 'layout':my_layout}, filename='d8_d8_simulation.html') # generate a chart and save it in a html format
