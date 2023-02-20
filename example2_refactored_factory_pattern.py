"""
Example of usage

>>> import serializer_demo as sd
>>> song = sd.Song('1', 'Water of Love', 'Dire Straits')
>>> serializer = sd.SongSerializer()

>>> serializer.serialize(song, 'JSON')
'{"id": "1", "title": "Water of Love", "artist": "Dire Straits"}'

>>> serializer.serialize(song, 'XML')
'<song id="1"><title>Water of Love</title><artist>Dire Straits</artist></song>'

>>> serializer.serialize(song, 'YAML')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "./serializer_demo.py", line 30, in serialize
    raise ValueError(format)
ValueError: YAML


"""


import json
import xml.etree.ElementTree as et


class Song:
    def __init__(self, song_id, title, artist) -> None:
        self.song_id = song_id
        self.title = title
        self.artist = artist

class SongSerializer:
    def serialize(self, song , format):
        serializer = get_serializer(format)
        return serializer(song)


def get_serializer(format):
    if format == "XML":
        return _serielize_to_xml
    elif format == "JSON":
        return _seriealize_to_json
    else:
        raise ValueError(format)


def _seriealize_to_json(song):
    payload = {
        'id': song.song_id,
        'title': song.title,
        'artist': song.artist
    }

    return json.dumps(payload)


def _serielize_to_xml(song):
    song_info = et.Element('song',attrib={'id': song.song_id})
    title = et.SubElement(song_info, 'title')
    title.text = song.title
    artist = et.SubElement(song_info, 'artist')
    artist.text = song.artist
    return et.tostring(song_info, encoding='unicode')


if __name__ == '__main__':
    song = Song('1', 'Water of Love', 'Dire Straits')
    serializer = SongSerializer()
    print(serializer.serialize(song, 'XML'))