#!  /usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

senyal, fm = sf.read('pav_2181.wav')

t = np.arange(0, len(senyal)) / fm

plt.subplot(2,1,1)
plt.title('Senyal en temps')
plt.plot(t, senyal)

plt.subplot(2,1,2)
plt.title('Autocorrelació')
plt.acorr(senyal, maxlags=20)

plt.show()

