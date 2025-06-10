import numpy as np

def generate_signal(waveform, freq, amp, duration, rate):
    t = np.linspace(0, duration, int(rate * duration), endpoint=False)
    if waveform == "sine":
        return t, amp * np.sin(2 * np.pi * freq * t)
    elif waveform == "square":
        return t, amp * np.sign(np.sin(2 * np.pi * freq * t))
    elif waveform == "composite":
        return t, amp * (np.sin(2 * np.pi * freq * t) + 0.5 * np.sin(2 * np.pi * freq * 3 * t))
    else:
        raise ValueError("Unsupported waveform")