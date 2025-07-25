from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a two D6
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list
results = [die_2.roll() * die_2.roll() for num_roll in range(1000)]


# Analyze the results

max_result = die_1.num_sides * die_2.num_sides # join the two dies result 12
frequencies = [results.count(value) for value in range(1,max_result+1)]

# Visualize the results
x_values = list(range(1, max_result+1)) # convert the range in a list and display the result on the vertical of the chart.

data = [Bar(x=x_values, y=frequencies)] # set the data in a bar chart 
title = 'Result of rolling a two multiply D6 1000 times.'

x_axis_config = {'title': 'Result', 'dtick':1} # set vertical title

y_axis_config = {'title': 'Frequency of Result'} # set horizontal title

my_layout = Layout(title=title, xaxis=x_axis_config, yaxis=y_axis_config) # set the chart layout

offline.plot({'data': data, 'layout':my_layout}, filename='d6_d6_multi.html') # generate a chart and save it in a html format
