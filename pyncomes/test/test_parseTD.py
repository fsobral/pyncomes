import unittest
from unittest import TestCase
from parseTD import Title, TDPage


class TestTitle(TestCase):

    """
    Classe de teste
    """

    def test_title(self):
        name = u'name'
        date = u'00/00/0000'
        title = Title(name, date)

        self.assertEqual(title.id(), name + '_' + date)
        self.assertEqual(title.name(), name)
        self.assertEqual(title.endDate(), date)

    def test_getTitle(self):
        title = Title(u'NTNB', u'15/05/2035')
        tdpage = TDPage()

        r = tdpage.extractTD(title)

        self.assertFalse(r is None)
        self.assertEqual(len(r), 2)
        self.assertEqual(r[1] > 0.0, True,
                         'Unable to extract information from ' +
                         tdpage.pageURL)
        
if __name__ == '__main__':
    unittest.main()

    
