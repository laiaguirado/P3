#!  /usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf


fitxer = 'pav_2181.wav'

senyal, fm = sf.read(fitxer)
t = np.arange(len(senyal)) / fm

np.delete(t,(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30))
np.delete(senyal,(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30))

print(senyal)
print("\n")
print(t)
plt.plot(t, senyal)
plt.show()