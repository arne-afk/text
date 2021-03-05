from bs4 import BeautifulSoup
import requests
import shutil
from os import startfile
"""

shutil.copyfile("testcopy.txt", "testcopy.md")
"""

class getDatas:
    def __init__(self):
        self.status = True
        self.header = self.header()







    def header(self):
        headers_param = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"}
        return headers_param
    def bbcMostPopular(self):

        headers_param = self.header
        web = "https://www.bbc.com"
        webPage = "https://www.bbc.com/news"
        run = requests.get(webPage, headers_param)
        self.webStatus(run)

        contents = run.content
        soup = BeautifulSoup(contents, "html.parser")
        code = soup.find_all("a", {
            "class": "gs-c-promo-heading nw-o-link gs-o-bullet__text gs-o-faux-block-link__overlay-link gel-pica-bold gs-u-pl-@xs"})

        a = 1
        with open("veriler.txt", "w") as my_file:

            for haber in code:
                my_file.write(f"\n{a}){haber.text}\n")
                my_file.write(f"<iframe src='{web}{haber.get('href')}' class='resize-vertical' style='height: 674px; width: 774px;'></iframe>\n")

                a = a+1
        shutil.copyfile("veriler.txt", ".\deneme\\veriler.md")
        startfile(".\deneme\\veriler.md")
    def playTusu(self):
        headers_param = self.header
        web = "https://playtusu.com"
        webPage = "https://playtusu.com"
        run = requests.get(webPage, headers_param)
        self.webStatus(run)
        contents = run.content
        soup = BeautifulSoup(contents, "html.parser")
        code = soup.find("div",{"id": "pt-slideshow"})
        # pt-slideshow > div.owl-stage-outer > div > div:nth-child(6) > a > figure > figcaption > h2
        #id pt-slideshow
        new = code.find_all("a")
        a = 1

        for i in new:
            print(f"{a}) {i.text}")
            print(i.get("href"))
            print("*******************")
            a = a+1

        code31 = soup.find_all("div", {"class": "col-sm-6"})

        for new31 in code31:
            print(f"{a}) {new31.a.text}")
            print(new31.a.get("href"))
            print("************************")
            a = a+1









    def menu(self):
        print("""
        1- Get BBC's most populer news.
        2- To exit the system.
        3- Get PlayTusu's news.
        """)

    def run(self):
        self.menu()
        choice = int(input("Choice a number: "))


        if choice==1 :
            self.bbcMostPopular()


        if choice==2:
            self.exit()

        if choice==3:
            self.playTusu()


    def webStatus(self,run):
        if run.status_code != 200:
            print(run.status_code)
            print("Can't get in.")





    def exit(self):
        self.status = False



object = getDatas()

while object.status:
    object.run()

