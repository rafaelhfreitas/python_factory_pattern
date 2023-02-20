"""
Basic video exporting example
"""

import pathlib
from abc import ABC, abstractclassmethod

class VideoExporter(ABC):
    """Basic representation of video exporting code"""

    @abstractclassmethod
    def prepare_export(self, video_data):
        """Prepares the video data to a folder."""

    @abstractclassmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the video data to a folder."""


class LosslessVideoExporter(VideoExporter):
    """Lossless video exporting code."""

    def prepare_export(self, video_data):
        print("Preparing video data for lossless export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in lossless format to {folder}.")


class H264BPVideoExporter(VideoExporter):
    """H.264 video exporting codec with Baseline profile."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Baseline) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Baseline) format to {folder}.")


class H264Hi422PVideoExporter(VideoExporter):
    """H.264 video exporting codec with Hi422P profile (10-bit, 4:2:2 chroma sampling)."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Hi422P) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}.")


class AudioExporter(ABC):
    """Basic representation of audio exporting codec."""


    @abstractclassmethod
    def prepare_export(self, audio_data):
        """Prepares audio data for exporting"""

    @abstractclassmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the audio data to a folder. """


class AACAudioExporter(AudioExporter):
    """AAC audio exporting codec."""

    def prepare_export(self, audio_data):
        print( "Preparing audio data for AAC export")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in AAC format to {folder}.")


class WAVAudioExporter(AudioExporter):
    """WAV (lossless) audio exporting codec."""

    def prepare_export(self, audio_data):
        print( "Preparing audio data for WAV export")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in WAV format to {folder}.")


class ExporterFactory(ABC):
    """
    Factory that represents a combination of video and audio codecs.
    The factory doesn't maintain any of instances it creates.
    """

    @staticmethod
    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter instance."""

    @staticmethod
    def get_audio_exporter(self) -> AudioExporter:
        """ Returns a new audio exporter instance."""        


class FastExporter(ExporterFactory):
    """Factory aimed at providing a high speed , lower quality export"""

    def get_audio_exporter(self) -> AudioExporter:
        return H264BPVideoExporter()
    
    def get_video_exporter(self) -> VideoExporter:
        return AACAudioExporter()


class HighQualityExporter(ExporterFactory):
    """Factory aimed at providing a slower speed , high quality export"""

    def get_audio_exporter(self) -> AudioExporter:
        return H264Hi422PVideoExporter()
    
    def get_audio_exporter(self) -> VideoExporter:
        return AACAudioExporter()


class MasterQualityExporter(ExporterFactory):
    """Factory aimed at providing a slower speed , master quality export"""

    def get_video_exporter(self) -> AudioExporter:
        return LosslessVideoExporter()
    
    def get_audio_exporter(self) -> VideoExporter:
        return WAVAudioExporter()

FACTORIES = {
    "low": FastExporter(),
    "high": HighQualityExporter(),
    "master": MasterQualityExporter(),
}   


def read_factory() -> ExporterFactory:
    """Constructs an exporter factory based on the user's preference"""
 

    #read  the desired export quality
    while True:
        export_quality = input(
            #f"Enter desired output quality (low, high, master):"
            f"Enter desired output quality ({', '.join(FACTORIES)}):"
        )
        try:
            return FACTORIES[export_quality]
        except KeyError:
            print(f"Unknown output quality option: {export_quality}")


def do_export(fac: ExporterFactory) -> None:
    """ Do a test export using a video and audio exporter."""

    # retrieve  the video and audio exporters
    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()

    # prepare the export
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    # do the export
    folder = pathlib.Path("/home/rafael/Downloads")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


def main() -> None:
    # create a factory
    factory = read_factory()

    # perform the exporting job
    do_export(factory)


if __name__ == "__main__":
    main()
