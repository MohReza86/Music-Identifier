"""
@author: Mohammadreza Baghery

"""

import pickle
from create_constellation import read_audio, st_fourier_transform, create_constellation
from create_hashes import create_hashes
from score_hashes import score_hashes_against_database
from convert_to_wav import convert_to_wav

song_index_lookup = pickle.load(open("song_index.pickle", "rb")) # loading the song index


# first convert the recordd snippet to wav then provide the path below
recorded_snippet = ''

def find_match(test_path):
    '''Return the song with the highest hash score'''

    sample_freq, audio_input = read_audio(test_path)
    freq, stft = st_fourier_transform(audio_input, sample_freq)
    constellation = create_constellation(freq, stft)
    hashes = create_hashes(constellation, None)
    scores = score_hashes_against_database(hashes)
    matched_song_path  = song_index_lookup[scores[0][0]]

    audio_path_split = matched_song_path.split('/')
    audio_name = audio_path_split[-1]
    audio_name = audio_name[:-4]

    return audio_name




if __name__ == '__main__':	
	print(find_match(recorded_snippet))


