#! /usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

fig, ax = plt.subplots(1,1, figsize=(9,6))
next_ = 5
no_days = 18
days = np.arange(1, no_days + 1, 1)
next_days = np.arange(1, no_days + next_ + 1, 1)

y = np.array([29, 30, 31, 34, 39, 45, 50, 71, 76, 83, 95,
        109, 120, 141, 171, 202, 252, 309])

def fit(x, a, tau):
    return a * np.exp(x/tau)

def error(pcov):
    a_sd, tau_sd = np.sqrt(np.diag(pcov))
    error_ar = np.ones(no_days + next_)
    for i in range(no_days + next_):
        error_ar[i] = fit(next_days[i], a, tau) * (a_sd/a + next_days[i] * tau_sd/ tau**2)

    return error_ar

(a, tau), pcov = curve_fit( fit, days[10:], y[10:])

print("Prediction in the next {} days:\n".format(next_))
for i in range(1, next_+1):
    print("Day {}: {}".format(no_days + i, int(a * np.exp((no_days + i)/tau))))


ax.set_title("COVID-19 India")
ax.axhline(color='black')
ax.axvline(1, color='black')
ax.grid(True, linestyle="--", color='#cccccc', alpha=0.8)

ax.fill_between(next_days, fit(next_days, a, tau) - error(pcov), 
                    fit(next_days, a, tau) + error(pcov), color="blue", alpha = 0.25, label="Error")
ax.plot(next_days, a * np.exp(next_days/tau), color="salmon", label="Fit curve")
ax.scatter(next_days, a * np.exp(next_days/tau), color="magenta", label="Prediction")
ax.scatter(days, y, label="Actual case")

ax.set_xlabel("Days")
ax.set_xlim(0.5, no_days + next_)
ax.set_xticks(np.arange(1, next_ + no_days +1 , 4))
ax.set_ylabel('Affected')

ax.legend(loc=2)
fig.savefig("plot.png")
fig.tight_layout()

plt.show()