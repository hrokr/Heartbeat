import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.io.wavfile import read
from scipy import signal
from scipy.signal import butter, lfilter, freqz

%matplotlib inline

t = np.linspace(0, 0.5, 500)

rate, data = wav.read('a0001.wav')

data = data[0:7000]

print(f"The length of this is {len(data)} samples")
print(f"This was sampled at {rate} samples/sec")
print(f"So, the recording is {len(data)/rate} seconds long")

plt.ylabel("Amplitude")
plt.xlabel("Time [total sample count]")
plt.plot(data)
plt.show()


# run and print the values of a FFT as these can be a bit ... counterintuitive
fft = np.fft.fft(data)

for i in range(2):
    print("Value at index {}:\t{}".format(i, fft[i + 1]), "\nValue at index {}:\t{}".format(fft.size -1 - i, fft[-1 - i]))

# Display of FFT
fft = np.fft.fft(data)
T = t[1] - t[0]  # sampling interval 
D = data.size
f = np.linspace(0, 1/T, D) #(start, stop, # of bins); 1/T = frequency
plt.rc('xtick', labelsize=30)     
plt.rc('ytick', labelsize=30)
plt.figure(figsize=(20,8))
plt.ylabel("Amplitude", fontsize = 40)
plt.xlabel("Freq", fontsize = 40)
plt.bar(f[:D // 2], np.abs(fft)[: D// 2] * 1 / D, width=1.5)  # 1 / N is a normalization factor
plt.show()

# Welch
fs = 2000 # sample rate in Hz. This has to be at least 2x the freq
N = D//2 # number of samples
amp = 2*np.sqrt(2)
freq = np.abs(fft)[: D// 2] * 1 / D
time = np.arange(N) / fs


# Display Power Spectrum Density
f, Pxx_den = signal.welch(freq, fs, nperseg=1024)

plt.figure(figsize=(20,8))
plt.rc('xtick', labelsize=30)     
plt.rc('ytick', labelsize=30)
plt.semilogy(f, Pxx_den)
plt.ylim([.05e-3, 1])
plt.title('Power Spectrum Density (PSD)', fontsize = 50)
plt.xlabel('frequency [Hz]', fontsize = 40)
plt.ylabel('PSD [V**2/Hz]', fontsize = 40)
plt.show()

# Obtaining the peaks using scipi convolve
from scipy.signal import convolve


#Obtaining derivative
kernel = [1, 0, -1]
dY = convolve(Pxx_den, kernel, 'valid') 

#Checking for sign-flipping
S = np.sign(dY)
ddS = convolve(S, kernel, 'valid')

#These candidates are basically all negative slope positions
#Add one since using 'valid' shrinks the arrays
candidates = np.where(dY < 0)[0] + (len(kernel) - 1)

#Here they are filtered on actually being the final such position in a run of
#negative slopes
peaks = sorted(set(candidates).intersection(np.where(ddS == 2)[0] + 1))

plt.figure(figsize=(20,8))
plt.plot(Pxx_den)

#If you need a simple filter on peak size you could use:
alpha = -0.0025
peaks = np.array(peaks)[Pxx_den[peaks] < alpha]


plt.scatter(peaks, Pxx_den[peaks], marker='x', color='g', s=40)


# Same thing using a different method:

sortedPxx=sorted(Pxx_den)[::-1]
sortedPxx

indices_Pxx_high_low = np.argsort(Pxx_den)[::-1]
top_n = 10
top_freq = f[indices_Pxx_high_low][:top_n]
top_amp = Pxx_den[indices_Pxx_high_low][:top_n]
print(top_freq)
print(top_amp)

out= np.argsort(dY)[0:22]
top_n = f[out]
print(out, top_n)