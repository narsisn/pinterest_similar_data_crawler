## **Pinterest Similar Data Crawler for Visual Search Tasks**
Note: I have used the git "https://github.com/ataknkcyn/pinterest-crawler" as a base code and then changed it for similar data crawling target. 

## Requirements
 - Python 3+

## Phase 1: Extracting Target Pins 

Run :
python3 pin_crawler.py

Input: keywords.csv file that contains the different search key words.  File path: /csv_files/keywords.csv 

Output: pin.csv file that contains the pin of target images. File path: /csv_files/pin.csv

## Phase 2: Downloading the Similar Images
Run :
python3 similar_downloader.py  

Input: pin.csv

Output: images directory including downloded images and similar_images.csv file that contains images metadata. 
File path : /csv_files/similar_images.csv  


Sample Code: 
```python
from src import PinSimilarScraper, PinSimilarConfig
import pandas as pd

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
   
```
