import urllib
import urllib2
import cookielib
import re

class Calendar():
    def __init__(self):
        self.baseURL = 'https://www.pogdesign.co.uk/cat'

    """ Login to your calendar """
    def login(self,username,password):
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

        form = {'username': username,
            'password': password,
            'sub_login': ''}

        self.submit_form(self.baseURL + '/cat/login', form)

    """ Returns HTML code of a given URL """
    def get_page(self, url):
        response = urllib2.urlopen(url)
        return response.read()

    """ Submits POST request """
    def submit_form(self,url,form):
        data = urllib.urlencode(form)
        request = urllib2.Request(url, data)
        urllib2.urlopen(request)

    """ Returns episode's id number """
    def get_epid(self,show,season,episode):
        showName = show
        content = ""
        try:
          showName = self.process_name(show)
          content = self.get_page(self.baseURL + '/cat/' + showName + '-summary')
        except:
          try:
            showName = self.process_name(show, True)
            content = self.get_page(self.baseURL + '/cat/' + showName + '-summary')
          except:
            content = None
            return None

        if content is None:
          return None

        matcher = re.compile('class="watchcheck" type="checkbox" value="(\d*-[0]*' + str(season) + '-[0]*' + str(episode) + '/\d*-\d*)')
        epid = matcher.findall(content)
        if not epid:
            return None
        else:
            return epid[0]

    """ Processing Kodi's show name into Pogdesign name used in URL of -summary page (eg. "Mr. Robot" to "Mr-Robot") """
    def process_name(self, show, remove_brackets = False):
        if remove_brackets:
          show = re.sub('\(.*?\)','',show)

        show = show.strip()
        show = re.sub('[^A-Za-z0-9\s&]+', '', show)
        show = show.replace('&','and')
        show = show.replace(' ','-')
        return show

    def mark_watched(self,epid):
        data = { 'watched': 'adding', 'shid': epid}
        self.submit_form(self.baseURL + '/watchhandle', data)

    def mark_unwatched(self,epid):
        data = { 'watched': 'removing', 'shid': epid}
        self.submit_form(self.baseURL + '/watchhandle', data)
