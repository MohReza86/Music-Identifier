"""
@author: Mohammadreza Baghery

"""

# 23_000 is slighlty higher than the maximum frequency 
# that can be stored in the .wav files, 22.05 kHz
upper_frequency = 23_000 
frequency_bits = 10


def create_hashes(constellation_map, song_id=None):
    ''' Return a combinatorial hash map 
    The points in the constellation map are combinatorially associated,
    each point is paired with several other points to form pairs of frequencies, 
    stored with the difference in time between them.'''

    hashes = {}
    # Iterate the constellation
    for idx, (time, freq) in enumerate(constellation_map):
        # Iterate the next 100 pairs to produce the combinatorial hashes
        for other_time, other_freq in constellation_map[idx : idx + 100]: 
            diff = other_time - time
            # If the time difference between the pairs is too small or large
            # ignore this set of pairs
            if diff <= 1 or diff > 10:
                continue
            # Place the frequencies (in Hz) into a 1024 bins
            freq_binned = freq / upper_frequency * (2 ** frequency_bits)
            other_freq_binned = other_freq / upper_frequency * (2 ** frequency_bits)
            # Produce a 32 bit hash
            # Use bit shifting to move the bits to the correct location
            hash = int(freq_binned) | (int(other_freq_binned) << 10) | (int(diff) << 20)
            hashes[hash] = (time, song_id)

    return hashes

