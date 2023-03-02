from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

def get_medicient(disease):
    url = "https://www.drugs.com/condition/{}.html".format(disease)
    urlclient = urlopen(url)
    page_html = urlclient.read()
    drug_html = bs(page_html, "html.parser")
    bigbox = drug_html.find_all("main", {'class':'ddc-width-container'})
    bigbox = bigbox[0].div.div.find_all("div", {"class":"contentBox"})
    bigbox = bigbox[0].find_all("div", {"class":"ddc-clear-both injection-ignore-inside"})
    bigbox = bigbox[0].find_all("div", {"class":"responsive-table-wrap"})
    table = bigbox[0].table.tbody.find_all("tr", {"class":"condition-table__summary condition-table__summary--generic"})
    med_list = []
    for i in range(0,5):
        med_list.append(table[i].find("a", {"class":"condition-table__drug-name__link ddc-text-wordbreak"}).text)
    return med_list
