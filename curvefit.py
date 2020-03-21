#! /usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# plt.style.use('ggplot')

next_ = 5
no_days = 18
days = np.arange(1, no_days + 1, 1)
next_days = np.arange(1, no_days + next_ + 1, 1)

y = np.array([29, 30, 31, 34, 39, 45, 50, 71, 76, 83, 95,
        109, 120, 141, 171, 202, 252, 301])

def fit(x, a, tau):
    return a * np.exp(x/tau)

def error(pcov):
    a_sd, tau_sd = np.sqrt(np.diag(pcov))
    error_ar = np.ones(no_days + next_)
    for i in range(no_days + next_):
        error_ar[i] = fit(next_days[i], a, tau) * (a_sd/a + next_days[i] * tau_sd/ tau**2)

    return error_ar

(a, tau), pcov = curve_fit( fit, days, y)

print("Prediction in the next {} days:\n".format(next_))
for i in range(1, next_+1):
    print("Day {}: {}".format(no_days + i, int(a * np.exp((no_days + i)/tau))))


plt.title("COVID-19 India")
plt.axhline(color='black')
plt.axvline(1, color='black')
plt.grid(True, linestyle="--", color='#cccccc', alpha=0.8)

plt.fill_between(next_days, fit(next_days, a, tau) - error(pcov), 
                    fit(next_days, a, tau) + error(pcov), color="blue", alpha = 0.25, label="Error")
plt.plot(next_days, a * np.exp(next_days/tau), color="salmon", label="Fit curve")
plt.scatter(next_days, a * np.exp(next_days/tau), color="magenta", label="Prediction")
plt.scatter(days, y, label="Actual case")

plt.xlabel("Days")
plt.xlim(0.5, no_days + next_)
plt.ylabel('Affected')


plt.legend(loc=2)
plt.savefig("plot.png")
plt.tight_layout()

plt.show()