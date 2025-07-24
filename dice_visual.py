from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6 and a D10
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list
results = []
for num_roll in range(50_000): # roll die 1000 times
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
title = 'Result of rolling a D6 and a D10 50,000 times.'

x_axis_config = {'title': 'Result', 'dtick':1} # set vertical title

y_axis_config = {'title': 'Frequency of Result'} # set horizontal title

my_layout = Layout(title=title, xaxis=x_axis_config, yaxis=y_axis_config) # set the chart layout

offline.plot({'data': data, 'layout':my_layout}, filename='d6_d10.html') # generate a chart and save it in a html format
