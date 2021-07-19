# pip3 install flickrapi

import flickrapi
import urllib
import sys
import time
import argparse
from PIL import Image

parser=argparse.ArgumentParser(
    description='''Python tool for downloading big image sets from Flickr''')
parser.add_argument('-o', type=str, default=".", help="Output Directory")
parser.add_argument("tags", type=str, help="tags to search for")
parser.add_argument("-n", type=int, help="Number of items to search for")
args=parser.parse_args()

# Flickr api access key from some dudes github
flickr=flickrapi.FlickrAPI('c6a2c45591d4973ff525042472446ca2', '202ffe6f387ce29b', cache=True)


keyword = args.tags

photos = flickr.walk(text=keyword,
                     tag_mode='all',
                     tags=keyword,
                     extras='url_c',
                     per_page=1000,           
                     sort='relevance')

urls = []
for i, photo in enumerate(photos):
    print (i)
    
    url = photo.get('url_c')
    urls.append(url)
    
    if i > args.n:
        break

# Download image from the url and save it

counter = 1
finished = True
while finished:
    try:
        print(f"{counter} : "+urls[counter])
        print("Next is :" + urls[counter+1])
        urllib.request.urlretrieve(urls[counter], args.o+f'{counter}.jpg') 
        counter = counter + 1
        time.sleep(0.1)
    except IndexError:
        print("EOF")
        finished = False
    except TypeError:
        print("None Type Detected")
        counter = counter + 1
    

x = len(urls)
print("Length: " + str(x))
