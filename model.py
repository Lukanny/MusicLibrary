from dataclasses import dataclass

@dataclass
class Music:
    title: str
    artist: str
    year: int

class MusicLibrary:

    def __init__(self):
        self.music_lib = []

    def __str__(self):
        return f'Music: {self.title} \n Artist: {self.artist} \n Year: {self.year}'

    def get_all_musics(self):
        return self.music_lib

    def add_music(self, title, artist, year):
        self.music_lib.append(Music(title=title, artist=artist, year=year)

    def get_one_music_by_title(self, title):
        all_musics = self.get_all_musics()
        return [music for music in all_musics if music.title == title][0]

    def get_all_musics_by_year(self, year):
        all_musics = self.get_all_musics()
        return [music for music in all_musics if music.year == year]

    def create_random_playlist(self):
        import random

        all_musics = self.get_all_musics()
        random.shuffle(all_musics)
        return all_musics