import urllib
import urllib2
import cookielib
import re


URL = 'http://www.pogdesign.co.uk'
SHOW_NAME = ''
PAGE = ''

""" Login to your calendar """
def login(username,password):
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)

    form = {'username': username,
            'password': password,
            'sub_login': 'Account Login'}

    submit_form(URL + '/cat/', form)

""" Returns HTML code of a given URL """
def get_page(url):
    response = urllib2.urlopen(url)
    return response.read()

""" Submits POST request """
def submit_form(url,form):
    data = urllib.urlencode(form)
    request = urllib2.Request(url, data)
    urllib2.urlopen(request)

""" Returns episode's id number """
def get_epid(show,season,episode):
    global SHOW_NAME
    global PAGE

    if SHOW_NAME != process_name(show):
      try:
        SHOW_NAME = process_name(show)
        PAGE = get_page(URL + '/cat/' + SHOW_NAME + '-summary')
      except:
          try:
            SHOW_NAME = process_name(show, True)
            PAGE = get_page(URL + '/cat/' + SHOW_NAME + '-summary')
          except:
            PAGE = None
            return None

    if PAGE is None:
      return None

    eps = re.findall('input class="watchcheck" type="checkbox" value="(.*)"', PAGE)
    eps = [ep.replace('" checked="checked','') for ep in eps]
    return next((x for x in eps if x.find('-' + str(season) + '-' + str(episode) + '/') != -1), None)

""" Processing Kodi's show name into Pogdesign name used in URL of -summary page (eg. "Mr. Robot" to "Mr-Robot") """
def process_name(show, remove_brackets = False):
    if remove_brackets:
        show = re.sub('\(.*?\)','',show)

    show = show.strip()
    show = re.sub('[^A-Za-z0-9\s&]+', '', show)
    show = show.replace('&','and')
    show = show.replace(' ','-')
    return show

def mark_watched(epid):
    submit_form(URL + '/cat/watchhandle', { 'watched': 'adding',
                                            'shid': epid})
def mark_unwatched(epid):
    submit_form(URL + '/cat/watchhandle', { 'unwatched': 'removing',
                                            'shid': epid})
def url_exists(url):
    request = urllib2.Request(url)
    request.get_method = lambda : 'HEAD'
    try:
        urllib2.urlopen(request)
        return True
    except:
        return False