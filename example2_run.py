import example2_serializers
import example2_songs

song = example2_songs.Song('1', 'Water of love', 'Dire Straits')
serializer = example2_serializers.ObjectSerializer()


print(serializer.serialize(song, 'JSON'))

print(serializer.serialize(song, 'XML'))

print(serializer.serialize(song, 'YAML'))