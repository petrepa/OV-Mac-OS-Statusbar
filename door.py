from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def door_status():
    find_string = ('Omega Verksted er åpent!').encode('utf-8')
    #print(find_string)

    try:
        html = urlopen("https://omegav.no/door")

    except HTTPError as e:
        print(e)
    except URLError:
        print("Server down or incorrect domain")

    else:
        res = BeautifulSoup(html.read(),"lxml")
    
        tags = res.find("a", {"href": "/door"})
        #print((tags.getText()).encode('utf-8'))
        
        status = (tags.getText()).encode('utf-8')
        #print(status)
        
        if status == find_string:
            door = "OV er ope"
            print(door)
            return True
        else:
            door = "OV er stengt"
            print(door)
            return False
        

door_status()