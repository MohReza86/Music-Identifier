# Music Identifier

Following the fundamentals behind the algorithms used in Shazam (the commercially available song identifier app), 
the current Music Identifier module allows identifying a short snippet of a music from a music database. 

Viewing songs in terms of the frequencies of sound that combine to make it up is the key to fingerprinting. 
Fourier Transfrom (FT) transforms a signal, such as a song, into the constituent frequencies that comprise it.
This technique analyzes the spectrum of the entire song as a whole. However, songs tend to change their sound 
throughout. A short snippet of a song is unlikely to match the frequency content of the entire song. To overcome 
this problem, we can perform the FT on short snippets of the song. Each snippet's frequencies identifies how the song 
changes over time. This can be achieved employing Short Time Fourier Transfrom (STFT). The module capitalizes on the 
principle o STFT to create fingerprints of tracks, identfying some kind of distictive feature of a song that tell it 
appart from other songs. 

We can then perform a peak finding algorithm on each STFT over the entire song. These peaks form a constellation of points 
which characterise the song. The idea behind such constellation is to be entirely unique. However, it is highly unlikely 
that a short recorded snippet of a song exactly all of the same frequencies present as in the original song. Based on the
solution provided by the founders of Shazam, we can combinatorially associate points in the constellation map. As such, we
would have each point paired with several other points to form pairs of frequency peaks, stored with the difference in time 
between them. To achieve such frequency pairs, We can create a combinatorial Hashing for each song. 

Next, we can generate a database containing all hashes. Finding a match for a short recording requires a a scoring strategy to 
differentiate which song a particular recording matches. The scoring method keeps track of the specific hash which matched between 
the database and the user recording, as well as the time in the database that matched occured and the time it occured in the user sample. 

The current module has tried to follow the fundamentals of Shazam algorithm. Although the module can reliably identify even a short 
recording (as short as 5 seconds) of a song with a noisy background, admittedly, several improvements can be done to improve the 
time and storage requirements at various steps. 

## Running

1) First off, all the avialable songs need to be converted to "wav" format. To do this, provide the directory path of the song 
folder in the "convert_to_wav" module and run it.

2) Then execute the "create_database" module to create a hash database of the entire songs. The databas will be saved in the directory
where the codes are saved. 

3) Record a short snippet of a song; use the "convert_to_wav" module to convert it to wav and feed it to the "find_match" module.
Next, running the "find_match" module will print the title of the matched song from the database.



