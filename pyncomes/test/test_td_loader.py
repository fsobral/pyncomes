import unittest
from unittest import TestCase
from pyncomes.td_loader import Title, TDPage


class TestTitle(TestCase):

    def test_title(self):
        name = u'name'
        date = u'00/00/0000'
        title = Title(name, date)

        self.assertEqual(title.id(), name + '_' + date)
        self.assertEqual(title.name(), name)
        self.assertEqual(title.endDate(), date)

    def test_setSellValue(self):
        title = Title('name', '00/00/0000')
        sellValue = 1.0

        title.setSellValue(sellValue)

        self.assertEqual(title.sellValue(), sellValue)


class TestTDPage(TestCase):

    def test_getTitle(self):
        title = Title(u'NTNB', u'15/05/2035')
        tdpage = TDPage()

        t = tdpage.extractTD(title)

        self.assertFalse(t is None)
        self.assertTrue(t.sellValue() > 0.0,
                        'Unable to extract information from ' +
                        tdpage.pageURL)

    def test_iterator(self):

        titlecnt = 0
        tdpage = TDPage()

        for (name, endDate, sellValue) in tdpage:
            if sellValue > 0.0:
                titlecnt += 1

        self.assertTrue(titlecnt > 0)

if __name__ == '__main__':
    unittest.main()
