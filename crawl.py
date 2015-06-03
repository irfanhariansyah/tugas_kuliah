import sys
import requests
import mysql.connector
import datetime
from mysql.connector import errorcode
from bs4 import BeautifulSoup


def get_link(argv):
    hari = str(datetime.datetime.now().day)
    bulan = str(datetime.datetime.now().month)
    tahun = str(datetime.datetime.now().year)
    url = "http://www.viva.co.id/indeks/berita/sainstek/"+tahun+"/"+bulan+"/"+hari
    url = "http://www.viva.co.id/indeks/berita/sainstek/2015/6/3"
    r = requests.get(url)

    soup = BeautifulSoup(r.content)
    if r.status_code == 400 or r.status_code == 408 or r.status_code == 302:
        print("Error! Halaman gagal dimuat")
    else:
        g_data = soup.find("ul", {"class": "indexlist"})
        if g_data.li is None:
            print("Tidak ada berita terbaru")
        else:
            for list in g_data.findAll("li"):
                alamat = list.a.get("href")
                string = str(alamat)
                if url_check(string):
                    get_content(string)
    pass

def url_check(url):
    r = requests.get(url, allow_redirects=False)
    #print(r.status_code, r.history)
    if r.status_code == 302:
        return False
    else:
        return True

def get_content(url):
    r = requests.get(url, allow_redirects=False)
    soup = BeautifulSoup(r.content)
    title = soup.title.text
    date = soup.find("div", {"class": "date"})
    content = soup.find(id="article-content")
    image = soup.find("div", {"class": "thumbcontainer"})

    news_title = title
    news_img = image.img.get("src")
    news_date = date.contents[0]
    for tag in content.find_all('aside'):
        tag.replaceWith('')
    for tag in content.find_all('script'):
        tag.replaceWith('')
    for tag in content.findAll("div", {"class": ['portlet', 'sideskycrapper']}):
        tag.replaceWith('')
    news_content = content.text
    news_content = news_content.strip('\t\r\n')
    if not title:
        print("Data tidak ada")
    else:
        insert_data(news_title, news_date, news_content, news_img)
    pass


def insert_data(title, date, content, img):
    try:
        cnx = mysql.connector.connect(user='root', password='root', database='web')
        cursor = cnx.cursor()
        title = (title.replace("'", "\\\'")).replace('"', '\\\"')
        content = (content.replace("'", "\\\'")).replace('"', '\\\"')
        query = "INSERT INTO berita (news_title, news_date, news_content, news_img) VALUES ('"+title+"','"+date+"','"+content+"','"+img+"')"
        cursor.execute(query)
        #print(query)
        cnx.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursor.close()
        cnx.close()
    pass

if __name__ == "__main__":
    get_link(sys.argv)
