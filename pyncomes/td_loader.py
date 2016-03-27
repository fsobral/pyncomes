"""
This module is responsible for crawling, reading, filling
and updating information about Tesouro Direto.
"""
import requests
import pandas
from bs4 import BeautifulSoup


class TDPage:
    """
    This class collects information directly from the
    Tesouro Direto page
    """

    def __init__(self):
        self.pageURL = 'http://www.tesouro.fazenda.gov.br/' + \
                       'tesouro-direto-precos-e-taxas-dos-titulos'

        r = requests.get(self.pageURL)

        self.soup = BeautifulSoup(r.text, 'html.parser')

    def __siteGenerator(self, bs):

        for line in bs.find_all('tr'):
            if line.td is not None and line.td.has_attr('class') \
               and u'listing0' in line.td['class']:

                wholeline = line.find_all('td')

                name = wholeline[0].text
                endDate = wholeline[1].text
                sellValue = float(wholeline[3].text.replace(',', '.'))

                yield (name, endDate, sellValue)

    def extractTD(self, title):
        """
        This function returns the current sell price of the given title,
        or None if it does not find it.
        """

        for (name, endDate, sellValue) in self.__siteGenerator(self.soup):

            if title.name() in name and endDate == title.endDate():
                title.setSellValue(sellValue)
                return title

        return None

    def __iter__(self):

        return self.__siteGenerator(self.soup)


class TDExcel:
    """
    This class extracts information from Tesouro Direto Excel files.
    """

    def __init__(self):
        self.fileLocations = []

    def extractFileIterator(self, filename):

        """
        Returns an iterator which extracts all the information about the file
        """

        table = pandas.read_excel(filename, skiprows=1, index_col=0)

        for i in table.index:
            yield (i, table.loc[i][u'Taxa Compra Manhã'],
                   table.loc[i][u'PU Compra Manhã'],
                   table.loc[i][u'PU Venda Manhã'])


class Title:
    """
    This class represents a Title at Tesouro Direto. A title is uniquelly
    defined by its name and its expiration date.
    """

    def __init__(self, name, endDate):
        self._name = name
        self._endDate = endDate

    def id(self):
        return self._name + '_' + self._endDate

    def name(self):
        return self._name

    def endDate(self):
        return self._endDate

    def setSellValue(self, sellValue):
        self._sellValue = sellValue

    def sellValue(self):
        return self._sellValue
