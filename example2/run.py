import serializers
import songs

song = songs.Song('1', 'Water of love', 'Dire Straits')
serializer = serializers.ObjectSerializer()


print(serializer.serialize(song, 'JSON'))

print(serializer.serialize(song, 'XML'))

print(serializer.serialize(song, 'YAML'))