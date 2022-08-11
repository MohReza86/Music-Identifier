"""
@author: Mohammadreza Baghery

"""

import glob
from typing import List, Dict, Tuple
from tqdm import tqdm
import pickle
from convert_to_wav import OUTPUT_PATH
from create_constellation import read_audio, st_fourier_transform, create_constellation
from create_hashes import create_hashes  


 
def create_database():
    
    songs = glob.glob('{}/*.wav'.format(OUTPUT_PATH))

    song_name_index = {}

    database: Dict[int, List[Tuple[int, int]]] = {}

    # Go through each song, using where they are alphabetically as an id
    for index, filename in enumerate(tqdm(sorted(songs))):
        song_name_index[index] = filename
        # Read the song, develop short time fourier transform, create a constellation and hashe map
        sample_freq, audio_input = read_audio(filename)
        freq, stft = st_fourier_transform(audio_input, sample_freq)
        constellation = create_constellation(freq, stft)
        hashes = create_hashes(constellation, index)

        # For each hash, append it to the list for this hash
        for hash, time_index_pair in hashes.items():
            if hash not in database:
                database[hash] = []
            database[hash].append(time_index_pair)

    # Dump the database and list of songs as pickles
    with open("database.pickle", 'wb') as db:
        pickle.dump(database, db, pickle.HIGHEST_PROTOCOL)
    with open("song_index.pickle", 'wb') as songs:
        pickle.dump(song_name_index, songs, pickle.HIGHEST_PROTOCOL)

    return database

    

		
if __name__ == '__main__':	
	create_database()



