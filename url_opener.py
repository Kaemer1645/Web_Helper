import webbrowser
from database import DataBase

class Opener:
    def __init__(self, urls):
        self.urls = urls

    def opener(self):
        for url in self.urls:
            webbrowser.open(url[1])
            print('Otwieram strone o nazwie ',url[0],' znajdujaca sie pod linkiem ',url[1])

if __name__ == '__main__':
    urls = DataBase()
    inst = Opener(urls.open())
    inst.opener()


