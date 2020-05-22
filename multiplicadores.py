# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
N = 32
p = np.arange(0.1, 3.1, .01)
multi1d = p/N 
multi2d = p+23/N 

fig, ax = plt.subplots()
ax.plot(p, multi1d)
ax.plot(p, multi2d)

ax.set(xlabel='Prevalencia (%)', ylabel='Multiplicador',
       title='Multiplicador vs prevalencia para cada método')
ax.set_xscale('log')
ax.set_xticks(np.arange(0.1,3.5,.5))
ax.set_yticks([1,2,3])

ax.grid(True, linestyle='-.')
#ax.tick_params(labelsize='medium', width=3)

plt.savefig("multi"+str(N)+".eps")
plt.show()