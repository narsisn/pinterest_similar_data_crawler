# ---  pinterest crawling code for creating visual search dataset

from src import PinSimilarScraper, PinSimilarConfig
import pandas as pd
import time
# read input file including search pins 
pinList = pd.read_csv('csv_files/pin.csv')
counter = 0 

for pin,pc,mc,ge in zip (pinList.pin,pinList.product_category,pinList.main_category,pinList.gender):
    counter = counter + 1 
    print ("Counter is =================>", counter,pin,pc,mc,ge )
 
    configs = PinSimilarConfig(search_pin=str(pin), # Search word
                            file_lengths=50,     # total number of images to download (default = "100")
                            image_quality="orig", # image quality (default = "orig")
                            bookmarks="",
                            )         # next page data (default= "")

    

    pinList = PinSimilarScraper(configs).download_images(pc,mc,ge)
    time.sleep(5)
