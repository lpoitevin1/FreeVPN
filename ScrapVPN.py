from bs4 import BeautifulSoup
import requests
import os
from time import sleep
from urllib.parse import unquote
import re
from urllib.request import urlretrieve
import zipfile


os.system("figlet '                             VPN' -f small \r\n")
os.system("figlet '                             Free' -f small \r\n")
os.system("figlet '                             Programmed' -f small \r\n")
os.system("figlet '                             By  ' -f small \r\n")
os.system("figlet '                             JohnDoe' -f small \r\n")



vpnbook_site = "https://www.vpnbook.com"
response = requests.get(vpnbook_site)
page_source = response.content
soup = BeautifulSoup(page_source , 'html.parser')
id_soup = soup.find(id="openvpn")
tab = []
tab2 = []
tab_href = []
tab_download = []
nb = 0

if( id_soup is not None ) :
    print("\r\n \r\n \r\n")
    for li in id_soup.find_all('li',recursive=True):
        if str(li).find('Username') != -1 :
            tab.append(str(li))
    for a in id_soup.find_all('a',href=True):
        if str(a.get('href')).find('zip') != -1 :
            tab_href.append((str(a.get('href'))))

    for element in tab_href:

        downloadUrl = vpnbook_site+element
        tab_download.append(downloadUrl)

    tab2.append((re.findall(r'<strong>(.*?)</strong>', str(tab[0]))))
    img = str(id_soup.find('img')['src'])
    img = img.replace(" ", "%20")
    print(img)
    tab2.append(img)
    username = str(tab2[0]).replace('Username: ','')
    username = username.replace('[','')
    username = username.replace(']','')
    username = username.replace("'",'')

    if ( img is not None ) :
        passwordDownload = vpnbook_site+'/'+img
        file = 'password.png'
        urlretrieve(passwordDownload, file)


        for link in tab_download :
            print("Téléchargement du liens : " + link)
            urlretrieve(link, 'link'+str(nb)+'.zip')
            nb = nb + 1

        print('\r\n \r\n \r\n')
        os.system('chmod a+rwx *')
        os.system('unzip -o \*.zip')
        os.system('chmod a+rwx *')


        print("\r\n \r\n")


        print("        #=========================================================================================================#\n")
        print("        #                                                                                                         #\n")
        print("        #                                    login file find !                                                    #\n")
        print("        #                                                                                                         #\n")
        print("        #                       username : "+username+"                                                                #\n")
        print("        #                                                                                                         #\n")
        print("        #                       password file : "+file+"                                                      #\n")
        print("        #                                                                                                         #\n")
        print("        #                                                                                                         #\n")
        print("        #                                                                                                         #\n")
        print("        #=========================================================================================================#\n")

        print('\r\n \r\n \r\n')
        print("        #=======================================================================================================================================#\n")
        print("        #                        We have all config file, we just need to type this command :                                                   #\n")
        print("        #                                                                                                                                       #\n")
        print("        #                                          openvpn --config <configFileName.ovpn>                                                       #\n")
        print("        #                                                                                                                                       #\n")
        print("        #                                                                                                                                       #\n")
        print("        #=======================================================================================================================================#\n")
