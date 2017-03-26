import requests
import re
from bs4 import BeautifulSoup
from collections import Counter

def get_lyrics(artist, title):
    artist, title = artist.lower(), title.lower()
    artist = re.sub('[^A-Za-z0-9]+', "", artist)
    title = re.sub('[^A-Za-z0-9]+', "", title)
    if artist.startswith("the"):
        artist = artist[3:]
    url = "http://azlyrics.com/lyrics/{}/{}.html".format(artist, title)
    # Fake User Agent
    headers = { 'User-Agent': 'Mozilla/6.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    r = requests.get(url, headers=headers)
    content = r.text
    try:
        soup = BeautifulSoup(content, 'html.parser')
        lyrics = str(soup)
        start_bound = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
        end_bound = '<!-- MxM banner -->'
        lyrics = lyrics.split(start_bound)[1]
        lyrics = lyrics.split(end_bound)[0]
        lyrics = lyrics.replace('<br>','').replace('</br>'
                                ,'').replace('</div>','').replace('<i>'
                                ,'').replace('</i>','').strip()
        lyrics = re.sub('[^A-Za-z0-9\n ]+', "", lyrics)
        lyrics = [word.upper() for word in lyrics.split()]
        return lyrics
    except:
        return None

def word_frequencies(artist, title):
    lyrics = get_lyrics(artist, title)
    if lyrics:
        c = Counter(lyrics)
        pair_list = []
        return c.most_common()
        

if __name__ == '__main__':
    word_frequencies("beatles", "yellow submarine")
