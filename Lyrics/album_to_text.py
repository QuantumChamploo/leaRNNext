from createDatabase import Database
from lyrics_data_scrape import Artist, Song, Album

results = ''
i = 0
database2 = Database()
#database2.create_song_table()

mfdoom = Artist('mfdoom')
albums = mfdoom.get_album_infos()

for album in albums:
	album = Album('mfdoom',album)
	print(album.title)
	#change album title
	if(album.title == 'Nehruviandoom'):
		i = 1

		for song in album.songs:
			full_song = Song('mfdoom',song)
			results += full_song.lyrics
			print("song number " + str(i) + " is being written out of "+ str(len(album.songs)))
			i += 1 

			#i+=1
			#print(full_song.lyrics)
			#print("\n")
			#print("\n")
			
#change txt file name
make_txt = open("Nehruviandoom.txt", "w+")

make_txt.write(results)
