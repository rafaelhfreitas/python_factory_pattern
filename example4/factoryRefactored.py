"""
Basic video exporting example
"""

import pathlib
from typing import Protocol, Type
from dataclasses import dataclass

class VideoExporter(Protocol):
    """Basic representation of video exporting code"""

    def prepare_export(self, video_data):
        """Prepares the video data to a folder."""

    def do_export(self, folder: pathlib.Path):
        """Exports the video data to a folder."""


class LosslessVideoExporter:
    """Lossless video exporting code."""

    def prepare_export(self, video_data):
        print("Preparing video data for lossless export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in lossless format to {folder}.")


class H264BPVideoExporter:
    """H.264 video exporting codec with Baseline profile."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Baseline) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Baseline) format to {folder}.")


class H264Hi422PVideoExporter:
    """H.264 video exporting codec with Hi422P profile (10-bit, 4:2:2 chroma sampling)."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Hi422P) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}.")


class AudioExporter(Protocol):
    """Basic representation of audio exporting codec."""

    def prepare_export(self, audio_data):
        """Prepares audio data for exporting"""

    def do_export(self, folder: pathlib.Path):
        """Exports the audio data to a folder. """


class AACAudioExporter:
    """AAC audio exporting codec."""

    def prepare_export(self, audio_data):
        print( "Preparing audio data for AAC export")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in AAC format to {folder}.")


class WAVAudioExporter:
    """WAV (lossless) audio exporting codec."""

    def prepare_export(self, audio_data):
        print( "Preparing audio data for WAV export")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in WAV format to {folder}.")




@dataclass
class MediaExporter:
    video: VideoExporter
    audio: AudioExporter

@dataclass
class MediaExporterFactory:
    video_class: Type[VideoExporter]
    audio_class: Type[AudioExporter]

    def __call__(self) -> MediaExporter:
        return MediaExporter(
            self.video_class(),
            self.audio_class()
        
        )
        


FACTORIES = {
    "low": MediaExporter(H264BPVideoExporter, AACAudioExporter),
    "high": MediaExporter(H264Hi422PVideoExporter, AACAudioExporter),
    "master": MediaExporter(LosslessVideoExporter, WAVAudioExporter),
}   


def read_factory() -> MediaExporter:
    """Constructs an exporter factory based on the user's preference"""
 

    #read  the desired export quality
    while True:
        export_quality = input(
            #f"Enter desired output quality (low, high, master):"
            f"Enter desired output quality ({', '.join(FACTORIES)}):"
        )
        try:
            return FACTORIES[export_quality]
            #video_class, audio_class = FACTORIES[export_quality]
            #return (video_class(), audio_class())
        except KeyError:
            print(f"Unknown output quality option: {export_quality}")


def do_export(media_exporter: MediaExporter)  -> None:
    """ Do a test export using a video and audio exporter."""


    # retrieve  the video and audio exporters

    # prepare the export
    media_exporter.video.prepare_export("placeholder_for_video_data")
    media_exporter.audio.prepare_export("placeholder_for_audio_data")

    # do the export
    folder = pathlib.Path("/home/rafael/Downloads")
    media_exporter.video.do_export(folder)
    media_exporter.audio.do_export(folder)


def main() -> None:
    # create a factory
    factory = read_factory()

    media_exporter = factory()

    # perform the exporting job
    do_export(media_exporter)


if __name__ == "__main__":
    main()
