import numpy as np
import matplotlib.pyplot as plt

# 1. Time settings
Fs = 1000  # Sampling frequency
T = 1.0 / Fs
N = 1000   # Number of samples
t = np.linspace(0.0, N*T, N, endpoint=False)

# 2. Signal - mix of sine + square
signal = np.sin(2.0*np.pi*50.0*t) + 0.5*np.sign(np.sin(2.0*np.pi*120.0*t))

# 3. FFT
fft_vals = np.fft.fft(signal)
freqs = np.fft.fftfreq(N, T)

# 4. Plot
plt.figure(figsize=(12, 8))

# Time-domain signal
plt.subplot(2, 2, 1)
plt.plot(t, signal)
plt.title("Time Domain Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# Magnitude Spectrum
plt.subplot(2, 2, 2)
plt.stem(freqs[:N//2], np.abs(fft_vals[:N//2]))
plt.title("Magnitude Spectrum")
plt.xlabel("Frequency [Hz]")

# Phase Spectrum
plt.subplot(2, 2, 3)
plt.stem(freqs[:N//2], np.angle(fft_vals[:N//2]))
plt.title("Phase Spectrum")
plt.xlabel("Frequency [Hz]")

# Reconstructed signal (Optional)
reconstructed = np.fft.ifft(fft_vals)
plt.subplot(2, 2, 4)
plt.plot(t, reconstructed.real)
plt.title("Reconstructed Signal")
plt.xlabel("Time [s]")

plt.tight_layout()
plt.show()
