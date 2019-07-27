from createDatabase import Database
from lyrics_data_scrape import Artist, Song, Album

results = ''
<<<<<<< HEAD
i = 1
j = 1
m = 1
database2 = Database()
#database2.create_song_table()

elliottsmith = Artist('elliottsmith')
albums = elliottsmith.get_album_infos()
k = len(albums)
print (len(albums))
print (len(elliottsmith.get_song_list()))
for album in albums:
	album = Album('elliottsmith',album)
	print(album.title)
	#change album title


	for song in album.songs:
		full_song = Song('elliottsmith',song)
		results += full_song.lyrics
		print("song number " + str(i) + " is being written out of "+ str(len(album.songs)) + " from album: " + str(j) + " out of: " + str(k))
		print(str(m/1.50) + " percent done")
		i += 1 
		m += 1
	

		#i+=1
		#print(full_song.lyrics)
		#print("\n")
		#print("\n")
	j += 1
	i = 0
		
#change txt file name
make_txt = open("elliottsmith_songs.txt", "w+")


make_txt.write(results)
