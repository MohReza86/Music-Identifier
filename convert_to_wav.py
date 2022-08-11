"""
@author: Mohammadreza Baghery

"""

from pydub import AudioSegment
import os

INPUT_PATH = '' # path to input audios
OUTPUT_PATH = ''  # path to the converted wav audios


def convert_to_wav(input_path, output_path=None):
	"""Take audio in different formats and return in wav format """

	for audio in os.listdir(input_path):
		if not audio.startswith('.'): # ignore hidden system files like .DS_Store
			audio_split = audio.split('.')
			audio_format = audio_split[len(audio_split) - 1] 
			audio_name = audio[:-4]
			audio_path = os.path.join(input_path, audio)

			try:
				audio_segment = AudioSegment.from_file(audio_path, audio_format)
				audio_segment = audio_segment.set_channels(1) # channel 1 is mono; 2 is stereo
				if output_path:
					audio_segment.export('{}/{}.{}'.format(output_path, audio_name, 'wav'), format="wav")
				else:
					audio_segment.export('{}/{}.{}'.format(input_path, audio_name, 'wav'), format="wav")
				
			except:
				print('Could not load the audio!')

		
if __name__ == '__main__':	
	convert_to_wav(INPUT_PATH, OUTPUT_PATH)
