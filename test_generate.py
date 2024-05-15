import unittest
from generate import getFaker, getConsentToContact

class TestGenerate(unittest.TestCase):

    def test_getFaker(self):
        faker, locale = getFaker()
        self.assertIn(locale, ['sv_SE', 'no_NO', 'fi_FI', 'dk_DK'])

    def test_consentToContact(self):
        self.assertIsInstance(getConsentToContact(), bool)

if __name__ == '__main__':
    unittest.main()
