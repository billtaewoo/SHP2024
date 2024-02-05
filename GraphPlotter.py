import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read the data
path = 'C:/Users/billt/SHP2024/Evecutwfc.xlsx'
data = pd.read_excel(path)

# extract the data
cutoffwf = data['cutoffwf'].values
E = data['energy'].values
energy = np.zeros(6)
cut_off_wave_function = np.zeros(6)
for i in range(6):
    energy[i] = E[i]
    cut_off_wave_function[i] = cutoffwf[i]
reference_energy = E[6]  # this is reference energy

pressure = data['pressure'].values
reference_pressure = pressure[6]  # this is reference pressure

# process the data
new_energy = np.log10(np.absolute(energy - reference_energy))
new_pressure = pressure - reference_pressure

# Plot the graph
plt.plot(cut_off_wave_function, new_energy, label='Curve Plot')

# Add labels and title
plt.xlabel('Cutoff Work Function/Ry')  # Replace with your desired X-axis label
plt.ylabel('Energy/Ry')  # Replace with your desired Y-axis label
plt.title('Energy vs. Cutoff Wave Function')  # Replace with your desired title


# Show the plot
plt.show()