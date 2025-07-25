import matplotlib.pyplot as plt

fig, ax = plt.subplots()

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

bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(x_values, frequencies, label=x_values, color=bar_colors) # set the data in a bar chart 

ax.set_ylabel('Rolling D6 Dice')
ax.set_title('Rolling a D6 Dice 1000 times.')
ax.legend(title='Dice color')

plt.show()
