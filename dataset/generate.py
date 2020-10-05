import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a, m, n, t = 100.0, 20.0, 1200.0, 1.8

# Appropriate x values, evenly spaced.
x = np.linspace(0.0, 25.0, 1000)

# Remove half the x values at random.
x = x[np.sort(np.random.choice(len(x), size=len(x) // 2, replace=False))]

# Error values.
e = np.random.normal(0.0, 4.0, len(x))

# y values.
y = a * ((1.0 + m * np.exp(-x / t)) / (1.0 + n * np.exp(-x / t)))
y = y + e

# Set negative y values to zero.
y[y < 0] = 0.0

# When x is too small, make sure y is zero.
y[x <= 0.3] = 0.0

# When x is too big, make sure y is zero.
y[x >= 24.4] = 0.0

# Randomly set some y values to zero.
y[np.sort(np.random.choice(len(y), size=len(y) // 100, replace=False))] = 0.0

# Plot the data.
fig = plt.figure()
plt.plot(x, y, 'k.')
plt.xlabel(r"speed m/s")
plt.ylabel(r"power kW")
fig.savefig('scatter.png', dpi=fig.dpi)

# Convert to data frame.
df = pd.DataFrame({"speed": x, "power": y})
df.to_csv("powerproduction.csv", index=False, float_format='%.3f')
