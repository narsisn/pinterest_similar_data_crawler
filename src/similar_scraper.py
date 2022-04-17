import requests
import json
import os
import urllib
import sys
import pandas as pd 
from os.path import exists


class Scraper:
    def __init__(self, config, image_urls=[], pin_urls=[] ):
        self.config = config
        self.image_urls = image_urls
        self.pin_urls = []
      
    # Set config for bookmarks (next page)
    def setConfig(self, config):
        self.config = config

    # Download images
    def download_images(self):
        folder = "photos/"+self.config.search_keyword.replace(" ", "-")
        number = 0
        # prev get links
        results = self.get_urls()
        try:
            os.makedirs(folder)
            print("Directory ", folder, " Created ")
        except FileExistsError:
            a = 1
        arr = os.listdir(folder+"/")
        for i in results:
            if str(i + ".jpg") not in arr:
                try:
                    file_name = str(i.split("/")[len(i.split("/"))-1])
                    download_folder = str(folder) + "/" + file_name
                    print("Download ::: ", i)
                    urllib.request.urlretrieve(i,  download_folder)
                    number = number + 1
                except Exception as e:
                    print(e)

    # get_urls return array
    def get_urls(self):
        SOURCE_URL = self.config.source_url,
        DATA = self.config.image_data,
        URL_CONSTANT = self.config.search_url
        print(SOURCE_URL)
        print(DATA)
        r = requests.get(URL_CONSTANT, params={
                         "source_url": SOURCE_URL, "data": DATA})
        jsonData = json.loads(r.content)
        resource_response = jsonData["resource_response"]
        data = resource_response["data"]
        results = data["results"]
        
        for i in results:
            self.image_urls.append(
                i["images"][self.config.image_quality]["url"])
    
        if len(self.image_urls) < int(self.config.file_length):
            self.config.bookmarks = resource_response["bookmark"]
            # print(self.image_urls)
            print("Creating links", len(self.image_urls))
            self.get_urls()
            return self.image_urls[0:self.config.file_length]


    # get_pins 
    def get_pins(self):
        SOURCE_URL = self.config.source_url,
        DATA = self.config.image_data,
        URL_CONSTANT = self.config.search_url
        r = requests.get(URL_CONSTANT, params={
                         "source_url": SOURCE_URL, "data": DATA})
        jsonData = json.loads(r.content)
        resource_response = jsonData["resource_response"]
        data = resource_response["data"]
        results = data["results"]
        for i in results:
            self.pin_urls.append(
                i["id"])
        if len(self.pin_urls) < int(self.config.file_length):
            self.config.bookmarks = resource_response["bookmark"]
            print("Creating links", len(self.pin_urls))
            self.get_pins()
            return self.pin_urls[0:self.config.file_length]
    # save pins at csv files 
    def save_pin_csv(self,pinList,pc,mc,ge):

        pinDF = pd.DataFrame(pinList, columns=['pin'])
        pinDF = pinDF.assign(product_category=pc,main_category=mc, gender=ge)
        if exists('csv_files/pin.csv'):
            pinDF.to_csv('csv_files/pin.csv', mode='a', index=False, header=False)
        else:
             pinDF.to_csv('csv_files/pin.csv', mode='a', index=False, header=True)




