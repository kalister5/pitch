import unittest
from app.models import Pitch,User
from app import db

class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.user_hazard = User(username = 'hazard',password = '1234')
        self.new_pitch = Pitch(name='cat',title='movie',description='moviereview',user =self.user_hazard, category='technology')

    # def tearDown(self):
    #     Pitch.query.delete()
    #     User.query.delete()

    def test_check_instance_variable(self):
        self.assertEquals(self.new_pitch.name,'cat')
        self.assertEquals(self.new_pitch.title,'movie')
        self.assertEquals(self.new_pitch.description,'moviereview')
        self.assertEquals(self.new_pitch.category, 'technology')
        # self.assertEquals(self.new_pitch.user,self.user_naiyoma)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all()) >0)

    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        got_pitch = Pitch.get_pitches(12345)
        self.assertTrue(len(got_pitch) > 0)
