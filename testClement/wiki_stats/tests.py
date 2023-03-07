# 3rd Party imports
#----------------------------
from django.test import TestCase, Client
from django.urls import reverse

class TestHomepage(TestCase):

    def test_homepage(self):

        url = reverse('index')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_summary_existing_title(self):

        summary = 'Albert Camus was a French philosopher, author, dramatist, and journalist.'\
            ' He was the recipient of the 1957 Nobel Prize in Literature at the age of 44, the second-youngest recipient in history.'\
            ' His works include The Stranger, The Plague, The Myth of Sisyphus, The Fall, and The Rebel.'
        c = Client()

        response = c.get('/wikistats/Camus')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), summary)

    
    def test_summary_non_existing_title(self):

        c = Client()

        response = c.get('/wikistats/boiabfi')
        self.assertEqual(response.status_code, 404)


    def test_long_word(self):

        c = Client()

        response = c.get('/wikistats/Camus/words')
        self.assertEqual(response.status_code, 200)

    def test_long_word_not_found(self):

        c = Client()

        response = c.get('/wikistats/boiabfi/words')
        self.assertEqual(response.status_code, 404)