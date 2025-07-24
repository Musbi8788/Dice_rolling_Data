from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6
die = Die()

# Make some rolls, and store results in a list
results = []
for num_roll in range(1000): # roll die 1000 times
    result = die.roll() # roll die
    results.append(result) # store the result

# Analyze the results
frequencies = []
for value in range(1, die.num_sides+1): # loop through the six side
    frequency = results.count(value) # count how many time a number repeated
    frequencies.append(frequency) # store the frequency 

# Visualize the results
x_values = list(range(1, die.num_sides+1)) # convert the range in a list

data = [Bar(x=x_values, y=frequencies)] # set the data in a bar chart 
title = 'Result of rolling one D6 1000 times.'

x_axis_config = {'title': 'Result'} # set vertical title

y_axis_config = {'title': 'Frequency of Result'} # set horizontal title

my_layout = Layout(title=title, xaxis=x_axis_config, yaxis=y_axis_config) # set the chart layout

offline.plot({'data': data, 'layout':my_layout}, filename='d6.html') # generate a chart and save it in a html format
