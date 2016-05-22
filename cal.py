import requests
import re

class Calendar():
    def __init__(self):
        self.baseURL = 'http://www.pogdesign.co.uk/cat'

    """ Login to your calendar """
    def login(self,username,password):
        self.s = requests.session()
        plod = {'username':username, 'password':password, 'sub_login':''}
        self.s.post(self.baseURL + '/login', data=plod)

    """ Returns HTML code of a given URL """
    def get_page(self, url):
        self.r = self.s.get(url)
        return self.r.text

    """ Returns episode's id number """
    def get_epid(self,show,season,episode):
        showName = show
        content = ""
        if showName != self.process_name(show):
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

        eps = re.findall('class="watchcheck" type="checkbox" value="(.*)" />', content)
        return next((x for x in eps if x.find('-' + str(season) + '-' + str(episode) + '/') != -1), None)

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
        plod = { 'watched': 'adding', 'shid': epid}
        self.s.post('http://www.pogdesign.co.uk/cat/watchhandle', data=plod)

    def mark_unwatched(self,epid):
        plod = { 'watched': 'removing', 'shid': epid}
        self.s.post(baseURL + '/watchhandle', data=plod)
