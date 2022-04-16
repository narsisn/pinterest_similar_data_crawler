## **Pinterest Similar Data Crawler for Visual Search Tasks**
Note: I have used the git "https://github.com/ataknkcyn/pinterest-crawler" as a base code and then channged it for similar data crawling target. 

## Requirements
 - Python 3+

## Phase 1: Extracting Target Pins 

Run :
python3 pin_crawler.py

input: 

output: 

## Phase 2: Downloading the Similar Images

```python
from src import PinterestScraper, PinterestConfig

configs = PinterestConfig(search_keywords=keys, # Search word
                            file_lengths=200,     # total number of images to download (default = "100")
                            image_quality="orig", # image quality (default = "orig")
                            bookmarks="",
                            )         # next page data (default= "")

    
pinList = PinterestScraper(configs).get_pins()
# save in csv file
PinterestScraper(configs).save_pin_csv(pinList, pc,mc,ge)
```
