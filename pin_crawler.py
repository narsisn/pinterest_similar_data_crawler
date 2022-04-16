# ---  pinterest crawling code for creating visual search dataset

from src import PinterestScraper, PinterestConfig
import pandas as pd
import time
# read input file including search keywords 
keywordsList = pd.read_csv('csv_files/keywords.csv')
counter = 0 

for keys,pc,mc,ge in zip (keywordsList.Keyword,keywordsList.product_category,keywordsList.main_category,keywordsList.gender):
    counter = counter + 1 
    print ("Counter is =================>", counter,keys,pc,mc,ge )
 
    configs = PinterestConfig(search_keywords=keys, # Search word
                            file_lengths=200,     # total number of images to download (default = "100")
                            image_quality="orig", # image quality (default = "orig")
                            bookmarks="",
                            )         # next page data (default= "")

    

    pinList = PinterestScraper(configs).get_pins()
    # save in csv file
    PinterestScraper(configs).save_pin_csv(pinList, pc,mc,ge)
    time.sleep(5)
