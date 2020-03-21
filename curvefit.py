#! /usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

from get_data import return_info

fig, ax = plt.subplots(1,1, figsize=(9,6))
next_ = 5

y, days, dates = return_info()
next_days = np.append(days, days[-1] + np.arange(1, next_ + 1))


def fit(x, a, tau):
    return a * np.exp(x/tau)

def error(pcov):
    a_sd, tau_sd = np.sqrt(np.diag(pcov))
    error_ar = np.ones(days.size + next_)
    for i in range(days.size + next_):
        error_ar[i] = fit(next_days[i], a, tau) * (a_sd/a + next_days[i] * tau_sd/ tau**2)

    return error_ar

(a, tau), pcov = curve_fit( fit, days, y)

print("Prediction in the next {} days:\n".format(next_))
for i in range(1, next_+1):
    print("Day {}: {}".format(days[-1] + i, int(a * np.exp((days[-1] + i)/tau))))


ax.set_title("COVID-19 India")
ax.axhline(color='#999999', alpha=.8)
ax.axvline(1, color='#999999', alpha=.8)
ax.grid(True, linestyle="--", color='#cccccc', alpha=0.8)

ax.fill_between(next_days, fit(next_days, a, tau) - error(pcov), 
                    fit(next_days, a, tau) + error(pcov), color="blue", alpha = 0.25, label="Error")
ax.plot(next_days, a * np.exp(next_days/tau), color="salmon", label="Fit curve")
ax.scatter(next_days, fit(next_days, a, tau), color="magenta", label="Prediction")
ax.scatter(days, y, label="Actual case")

ax.set_xlabel("Days")
ax.set_xlim(0.5, days[-1] + next_)
ax.set_xticks(days)
ax.set_xticklabels(dates, rotation=30)
ax.set_ylabel('Affected')

ax.legend(loc=2)
fig.savefig("plot.png")
fig.tight_layout()

plt.show()