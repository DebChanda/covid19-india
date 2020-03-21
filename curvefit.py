#! /usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

plt.style.use('seaborn')

next_ = 5
no_days = 19
days = np.arange(1, no_days + 1, 1)
next_days = np.arange(1, no_days + next_ + 1, 1)

y = np.array([6, 29, 30, 31, 34, 39, 45, 50, 71, 76, 83, 95,
        109, 120, 141, 171, 202, 252, 288])

def fit(x, a, tau):
    return a * np.exp(x/tau)


(a, tau), _ = curve_fit( fit, days, y)

print("Prediction in the next {} das:\n".format(next_))
for i in range(1, next_+1):
    print("Day {}: {}".format(no_days + i, int(a * np.exp((no_days + i)/tau))))


plt.title("COVID-19 India")
plt.plot(next_days, a * np.exp(next_days/tau), color="salmon", label="Fit curve")
plt.scatter(next_days, a * np.exp(next_days/tau), color="magenta", label="Prediction")
plt.scatter(days, y, label="Actual case")

plt.xlabel("Days")
plt.ylabel('Affected')
plt.legend()
plt.savefig("plot.png")
plt.show()
