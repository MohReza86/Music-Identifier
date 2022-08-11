"""
@author: Mohammadreza Baghery

"""

import numpy as np 
from scipy.io.wavfile import read
from scipy import signal


def read_audio(path):
    sample_freq, audio = read(path)
    return sample_freq, audio


def st_fourier_transform(audio, sample_freq):
    '''Return 
        frequencies: a list of all frequencies 
        st_fourier_transform: short time fourier transform 
        a list of Fourier transform of all time segments 
        normalized into positive and negative frequencies.
     '''
    win_len_sec = 0.5  # lenghth of the window for short time fourier transform
    win_len_samples = int(win_len_sec * sample_freq)
    win_len_samples += win_len_samples % 2
    # Pad the song to divide evenly into windows
    amount_to_pad = win_len_samples - audio.size % win_len_samples
    audio_input = np.pad(audio, (0, amount_to_pad))
    # Perform a short time fourier transform (stft)
    freq, times, st_fourier_transform = signal.stft(audio_input, sample_freq, 
                                                    nperseg=win_len_samples, 
                                                    nfft=win_len_samples, 
                                                    return_onesided=True
    )

    return freq, st_fourier_transform



def create_constellation(frequencies, st_fourier_transform):
    '''Return a list of peak frequencies produced by short time fourier transform
    at different time points throughout the audio, 
    refered to as constellation of frequency peaks at each time point
    '''
    constellation_map = []
    num_peaks = 15  # maximum of peaks per time slice

    for time_idx, window in enumerate(st_fourier_transform.T):
        # Spectrum is by default complex; We want real values only
        spectrum = abs(window)
        # Find peaks - these correspond to interesting features
        # Note the distance - want an even spread across the spectrum
        peaks, props = signal.find_peaks(spectrum, prominence=0, distance=200)
        # We only want the most prominent peaks, with a maximum of 15 per time slice
        n_peaks = min(num_peaks, len(peaks))
        # Get the n_peaks largest peaks from the prominences
        largest_peaks = np.argpartition(props["prominences"], -n_peaks)[-n_peaks:]

        for peak in peaks[largest_peaks]:
            frequency = frequencies[peak]
            constellation_map.append([time_idx, frequency])

    return constellation_map

