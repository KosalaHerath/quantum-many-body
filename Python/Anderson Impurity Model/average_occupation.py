# Anderson Impurity Model
# Variation of occupation electron in single state with state energy value

# In this case we are assuming Temperature = 0K and consider Self Energy assumptions

import math
import numpy as np
import matplotlib.pyplot as plt
# Parameter definition
delta = 0.1
u_max = 1.0
e_zero = -1.5
e_zero_array = np.array([])
while e_zero < u_max:
    e_zero_array = np.append(e_zero_array, e_zero)
    e_zero = e_zero + (u_max/20)
n_up_array = np.array([])
n_down_array = np.array([])
for e in e_zero_array:
    n_up = 0.5
    n_down = 0.5
    n_up_old = n_up
    n_down_old = n_down
    n_up_temp = n_up_old
    n_down_temp = n_down_old
    for i in range(1, 101):
        n_up = 0.5 - (1.0 / math.pi) * math.atan((e + (u_max * n_down_old)) / delta)
        n_down = 0.5 - (1.0 / math.pi) * math.atan((e + (u_max * n_up_old)) / delta)
        n_up_temp = n_up_old
        n_down_temp = n_down_old
        n_up_old = n_up
        n_down_old = n_down
    n_up_array = np.append(n_up_array, 0.5 * (n_up + n_up_temp))
    n_down_array = np.append(n_down_array, 0.5 * (n_down + n_down_temp))
total_array = np.add(n_up_array,n_down_array)
plt.plot(e_zero_array, n_up_array, 'r--', e_zero_array, n_down_array, 'g--', e_zero_array, total_array)
plt.show()
