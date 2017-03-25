import requests
import re
from bs4 import BeautifulSoup

def get_lyrics(artist, title):
    artist, title = artist.lower(), title.lower()
    artist = re.sub('[^A-Za-z0-9]+', "", artist)
    title = re.sub('[^A-Za-z0-9]+', "", title)
    if artist.startswith("the"):
        artist = artist[3:]
    url = "http://azlyrics.com/lyrics/{}/{}.html".format(artist, title)
    # Fake User Agent
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    r = requests.get(url, headers=headers)
    content = r.text
    try:
        soup = BeautifulSoup(content, 'html.parser')
        lyrics = str(soup)
        start_bound = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
        end_bound = '<!-- MxM banner -->'
        lyrics = lyrics.split(start_bound)[1]
        lyrics = lyrics.split(end_bound)[0]
        lyrics = lyrics.replace('<br>','').replace('</br>','').replace('</div>','').replace('.','').replace(',','').strip()
        return lyrics
    except:
        return None

if __name__ == '__main__':
    print(get_lyrics("death grips","beware"))
