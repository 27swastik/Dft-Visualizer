import numpy as np

def compute_dft(signal):
    fft_vals = np.fft.fft(signal)
    mag = np.abs(fft_vals)
    phase = np.angle(fft_vals)
    return mag.tolist(), phase.tolist()

def compute_idft(spectrum):
    return np.fft.ifft(spectrum).real