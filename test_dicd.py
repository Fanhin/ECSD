import unittest
import dicd
from unittest import mock

class DicdTest(unittest.TestCase):
    def setUp(self):
        self.dicd_obj = dicd.Dicd()

        #def get_face():
        #    return 6

        #self.dicd_obj.get_face = get_face
    @mock.patch('dicd.random.randint')
    def test_role_get_6(self,randmock):
        expected = 6
        randmock.return_value = 6
        self.dicd_obj.roll()
        result = self.dicd_obj.get_face()

        self.assertEqual(expected,result)

    @mock.patch('dicd.random.randint',return_value = 3)
    def test_role_get_3(self,randmock):
        expected = 3
        self.dicd_obj.roll()
        result = self.dicd_obj.get_face()

        self.assertEqual(expected,result)

