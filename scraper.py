#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 23:32:04 2017

@author: fede
"""

from bs4 import BeautifulSoup
import urllib.request as urllib
import re
import pandas as pd


base_url="http://www.milongueando.it/letras_testi_di_tango/"

html_page = urllib.urlopen("http://www.milongueando.it/letras_testi_di_tango/index.html").read()
soup = BeautifulSoup(html_page, "lxml")
    
urls_list=[]
for link in soup.findAll('a'):
    print (link.get('href'))
    if link.get("href") is not None:
        urls_list.append(link.get("href"))
        print(urls_list)
    
urls_list=[e for e in urls_list if ((len(e)==14) or (len(e)==15)) and ("letras" in e)]

urls_list=[base_url + e for e in urls_list]

columnNames=["Titulo", "Autor_musica", "Autor_letra", "Letra"]
start="Música: "
end="\nLetra: "

title=[]
a_music=[]
a_lyric=[]
lyric=[]

#Title
for each in range(len(urls_list)):
    url= urllib.urlopen(urls_list[each]).read()
    url=BeautifulSoup(url, "lxml")
    
    print(each)
    #Titles
    tit=url.find_all("div", {"class":"titletra"})
    st='">'
    en='</'
    for t in tit: 
        temp=t.find("a").text
        temp=temp[temp.find(st)+len(st)-1:temp.find(en)]
        title.append(temp.replace("\n",""))
    #Autores
    auth=url.find_all("div",{"class":"datosletra"})
    for a in auth: 
        str=a.text
        start="Música: "
        end="\nLetra: "
        a_music.append(str[str.find(start)+len(start):str.find(end)])
        a_lyric.append(str[str.find(end)+len(end):-1])    
    #Letra
    lyr=url.find_all("div", {"class":"textoletra"})
    for l in lyr: 
        lyric.append(l.text.replace("\n",""))



data=pd.DataFrame(
                  {"title":title,
                   "a_music":a_music,
                   "a_lyric":a_lyric,
                   "lyric":lyric})