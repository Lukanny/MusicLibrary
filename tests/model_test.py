import unittest

from model import MusicLibrary

class TestMusicLibrary(unittest.TestCase):

    def test_add_music(self):
        ml = MusicLibrary()
        ml.add_music(title='I Bet You Look Good On The Dancefloor', artist='Artic Monkeys', year=2006)
        all_musics = ml.get_all_musics()
        for music in all_musics:
            self.assertEqual(music.title, 'I Bet You Look Good On The Dancefloor')
    
    def test_get_one_music_by_title(self):
        ml = MusicLibrary()
        ml.add_music(title='I Bet You Look Good On The Dancefloor', artist='Artic Monkeys', year=2006)
        wanted_music = ml.get_one_music_by_title('I Bet You Look Good On The Dancefloor')
        self.assertEqual(wanted_music.artist, 'Artic Monkeys')

    def test_get_all_musics_by_year(self):
        ml = MusicLibrary()
        ml.add_music(title='The View From The Afternoon', artist='Artic Monkeys', year=2006)
        ml.add_music(title='I Bet You Look Good On The Dancefloor', artist='Artic Monkeys', year=2006)
        ml.add_music(title='Fake Tales Of San Francisco', artist='Artic Monkeys', year=2006)
        musics = ml.get_all_musics_by_year(2006)
        for music in musics:
            self.assertEqual(music.year, 2006)

    def test_create_random_playlist(self):
        ml = MusicLibrary()
        ml.add_music(title='The View From The Afternoon', artist='Artic Monkeys', year=2006)
        ml.add_music(title='I Bet You Look Good On The Dancefloor', artist='Artic Monkeys', year=2006)
        ml.add_music(title='Fake Tales Of San Francisco', artist='Artic Monkeys', year=2006)
        my_playlist = ml.create_random_playlist()
        self.assertEqual(len(my_playlist), 3)
