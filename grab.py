# from google.appengine.api import urlfetch
import sys
sys.path.insert(0, 'lib')

from bs4 import BeautifulSoup
import urllib3
import urllib
import json


HTTP = urllib3.PoolManager()


def id_type(query):
    """Return the type of query -- application number or patent number --
    based on input query string."""
    if len(query) == 7:
        return "patent number"
    else:
        i = int(query[0])
        if (len(query) == 11) & (i in set([1, 2])):
            return "application number"
        else:
            raise Exception


def patent_parse(query):
    """Returns the structured data for the patent query, checking first for
    whether the query conforms to the parameters for a patent identifier."""
    try:
        s = id_type(query)
    except Exception:
        return {
            'error':
            'You must provide a valid patent or application number'
        }

    if s == "patent number":
        title = Patent(query).get_title()

    elif s == "application number":
        title = Application(query).get_title()

    return {
        "number": query,
        "type": s,
        "title": title.lower().capitalize()
    }


class Patent:
    def __init__(self, num):
        self.number = num
        self.host = "http://patft.uspto.gov/netacgi/nph-Parser"
        self.params = dict(
            Sect1="PTO1",
            Sect2="HITOFF",
            d="PALL",
            p=1,
            u="%2Fnetahtml%2FPTO%2Fsrchnum.htm",
            r=1,
            f="G",
            l=50,
            s1="%s.PN." % self.number,
            OS="PN/%s" % self.number,
            RS="PN/%s" % self.number
        )
        self.body = HTTP.request('GET', self.host, fields=self.params).data
        self.soup = BeautifulSoup(self.body)

    def get_title(self):
        try:
            [title] = self.soup.find_all('font', {'size': '+1'})
            return title.string.strip()
        except Exception:
            return "No results found."


class Application:
    def __init__(self, num):
        self.number = num
        self.host = "http://appft.uspto.gov/netacgi/nph-Parser"
        self.params = dict(
            Sect1="PTO1",
            Sect2="HITOFF",
            d="PG01",
            p=1,
            u="%2Fnetahtml%2FPTO%2Fsrchnum.html",
            r=1,
            f="G",
            l=50,
            s1=urllib.quote('"' + str(self.number) + '"' + '.PGNR.'),
            OS="DN/%s" % self.number,
            RS="DN/%s" % self.number
        )
        self.body = HTTP.request('GET', self.host, fields=self.params).data
        self.soup = BeautifulSoup(self.body)

    def get_title(self):
        try:
            [title] = self.soup.find_all('font', {'size': '+1'})
            return title.string.strip()
        except Exception:
            return "No results found."
