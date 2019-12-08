from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

#https://translate.google.com/#view=home&op=translate&sl=en&tl=en&text=hello
#tlid-transliteration-content transliteration-content full

#ttps://translate.google.com/translate_a/single?client=webapp&sl=en&tl=fr&hl=en&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&dt=gt&source=bh&ssel=0&tsel=0&kc=1&tk=327718.241137&q=goodmorning

class Phonetizer:
    def __init__(self,sentence : str,language_ : str = 'en'):
        self.words=sentence.split()
        self.language=language_
    def get_phoname(self):
        for word in self.words:
            print(word)
            #url="https://translate.google.com/translate_a/single?client=webapp&sl="+self.language+"&tl="+self.language+"&hl=en&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&dt=gt&source=bh&ssel=0&tsel=0&kc=1&tk=327718.241137&q="+word.lower()
            #url="https://translate.google.com/#view=home&op=translate&sl="+self.language+"&tl="+self.language+"&text="+word
            url="https://translate.google.com/translate_a/single?client=webapp&sl=en&tl=en&hl=en&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&dt=gt&source=bh&ssel=0&tsel=0&kc=1&tk=327718.241137&q=goodmorning"
            print(url)
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'})
            webpage = urlopen(req).read()
            f= open("debug.html","w+")
            f.write(webpage.decode("utf-8"))
            f.close()
            #print(webpage)
            #bsoup = BeautifulSoup(webpage,'html.parser')
            #phonems = bsoup.findAll("div", {"class": "tlid-transliteration-content transliteration-content full"})
            print(webpage.decode())
            #break

ph=Phonetizer("Hello Beautiful!")
ph.get_phoname()
