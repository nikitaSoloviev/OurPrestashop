import math
import random
from io import StringIO
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv

def solo(img):
    check =0
    i=-1
    word =None
    while 1:
        i+=1
        new = img[i]
        if img[i]=='"' and check !=1:
            check =1
        elif img[i]=='"' and check ==1:
            return word

        if check ==1 and img[i] !='"':
            if word is None:
                word = img[i]
            else:
                word+=img[i]

def copy_next(name,table,index=0,yes=1):
    number = table.find(name,index)
    check = 0
    word=None
    if yes==1:
        while 1:
            number+=1
            new = table[number]
            if new == '"' :
                if check==0:
                    check=1
                elif check ==1:
                    check=2
                elif check==2:
                    return word
            if check == 2 and new!='"'and new!=':' and new!="}" and new!='/' :
                if word is None:
                    word=new
                else:
                    word= word+new
    elif yes==0:
        while 1:
            number+=1
            new = table[number]
            if new == '"' :
                if check==0:
                    check=1
            if new == ',':
                return word
            if check == 1 and new!='"' and new!=',' and new!=':' and new!="}" and new!='/' :
                if word is None:
                    word=new
                else:
                    word= word+new
    elif yes==2:
        while 1:
            number+=1
            new = table[number]
            if new == '"' or new == '\\':
                if check==0:
                    check=1
                elif check ==1:
                    check=2
                elif check==2:
                    return word
            if check == 2 and new!='"'and new!=':' and new!="}" and new!='/' and new!= '\\':
                if word is None:
                    word=new
                else:
                    word= word+new


my_url = 'https://stock.adobe.com/pl/search/premium?load_type=search&native_visual_search=&similar_content_id=&is_recent_search=&search_type=autosuggest&k=macro&acp=0&aco=macro'
category = "Makro"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")
#print(page_soup.h1)
containers =page_soup.find_all("div",{"class":"search-result-cell small-bottom-spacing js-search-result-cell ftl-thumb-mosaic js-hover-container"})
#print(len(containers))
filename = "makro_id.csv"
f = open(filename,"w")
f.write("id;image;title;author;format;nazwa;rozmiary;kategoria;cena_duzy;cena_maly;ilosc(quantity)\n")
ident = 397

'''

cont= containers[0]
image = cont.div.a.img["src"]
print(image)
link = cont.div.a["href"]
print(link)
client_u = uReq(link)
page_h = client_u.read()
client_u.close()
page_s = soup(page_h,"html.parser")
#print(page_s)
img = page_s.find_all("meta",{"property":"og:image"})

image = solo(str(img))
print(image)
up_f = page_s.find_all("div",{"id":"image-detail-json"})
print(up_f)
up_f = str(up_f)
#print(up_f)
title = copy_next("title",up_f)


large_h = copy_next("content_original_height",up_f,1,0)
large_w = copy_next("content_original_width",up_f,1,0)
format = copy_next("format",up_f)
author = copy_next("author",up_f)
index= up_f.find("image_height") +3
index = up_f.find("image_height",index) +3
small_h = copy_next("image_height",up_f,index,0)
small_w = copy_next("image_width",up_f,index,0)
index= up_f.find("license_price") +3
large_price = copy_next("license_price",up_f,index,2)
index = up_f.find("license_price",index) +3
small_price = copy_next("license_price",up_f,index,2)

print(title)
print(large_h)
print(large_w)
print(format)
print(author)
print(small_h)
print(small_w)
large_price =large_price.replace(",",".")
large_price = float(large_price) * 4.48
large_price = math.ceil(large_price)
large_price+=0.99
print(large_price)
small_price = small_price.replace(",",".")
small_price = float(small_price) * 4.48
small_price = math.ceil(small_price)
small_price+=0.99
print(small_price)

'''
#print("title: "+ title)
#print("author: "+author)


for cont in containers:
    quantity = random.randint(1,105)
    #image = cont.div.a.img["src"]
    link = cont.div.a["href"]
    #print(link)
    client_u = uReq(link)
    page_h = client_u.read()
    client_u.close()
    page_s = soup(page_h,"html.parser")
    img = page_s.find_all("meta",{"property":"og:image"})
    image = solo(str(img))
    #print(page_s)
    up_f = page_s.find_all("div",{"id":"image-detail-json"})
    #print(up_f)
    up_f = str(up_f)
    #print(up_f)
    title = copy_next("title",up_f)

    large_h = copy_next("content_original_height",up_f,1,0)
    large_w = copy_next("content_original_width",up_f,1,0)
    format = copy_next("format",up_f)
    author = copy_next("author",up_f)
    index= up_f.find("image_height") +3
    index = up_f.find("image_height",index) +3
    small_h = copy_next("image_height",up_f,index,0)
    small_w = copy_next("image_width",up_f,index,0)
    index = up_f.find("license_price") + 3
    large_price = copy_next("license_price", up_f, index, 2)
    index = up_f.find("license_price", index) + 3
    small_price = copy_next("license_price", up_f, index, 2)

    print(title)
    print(large_h)
    print(large_w)
    print(format)
    print(author)
    print(small_h)
    print(small_w)
    print(image)
    large_price = large_price.replace(",", ".")
    large_price = float(large_price) * 4.48
    large_price = math.ceil(large_price)
    large_price += 0.99
    print(large_price)
    small_price = small_price.replace(",", ".")
    small_price = float(small_price) * 4.48
    small_price = math.ceil(small_price)
    small_price += 0.99
    print(small_price)


    large = large_w+"x"+large_h
    small = small_w + "x" + small_h






    f.write(str(ident)+';'+image+';'+title.replace(","," ")+';'+author+';'+format+';Rozmiar;'+ large+','+ small+';'+category+';'+str(large_price)+';'+str(small_price)+';'+str(quantity)+'\n')
    ident+=1
f.close()
