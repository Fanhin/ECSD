import unittest
from unittest.mock import patch, MagicMock
import fivedots

class fivedotsTest(unittest.TestCase):

    @patch('fivedots.requests.get')
    def test_text_get_Welcome(self,gmock):
        expected = "Welcome"
        rmock = gmock()
        rmock.status_code = 200
        rmock.text = expected

        html = fivedots.get_fivedots_data()

        self.assertTrue(expected in html)

    @patch('fivedots.requests.get')
    def test_get_None(self,gmock):
        expected = None
        rmock = gmock()
        rmock.status_code = 300

        html = fivedots.get_fivedots_data()

        self.assertEqual(expected,html)

    @patch('fivedots.requests.get')
    def test_get_Damrong(self,gmock):
        expected = "Damrong"
        rmock = gmock()
        rmock.status_code = 200
        rmock.text = expected

        html = fivedots.get_fivedots_data()

        self.assertTrue(expected in html)

    @patch('fivedots.requests.get')
    def test_get_fivedotss_user_homepages(self,gmock):
        expected = "fivedots's user homepages"
        rmock = gmock()
        rmock.status_code = 200
        rmock.text = expected

        html = fivedots.get_fivedots_data()

        self.assertTrue(expected in html)


        


