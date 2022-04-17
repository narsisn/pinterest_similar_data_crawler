import urllib

class Config:
    IMAGE_SEARCH_URL = "https://www.pinterest.com/resource/VisualLiveSearchResource/get/?"
    def __init__(self, search_pin="", file_lengths=100, image_quality="orig", bookmarks=""):
        self.search_pin = search_pin
        self.file_lengths = file_lengths
        self.image_quality = image_quality
        self.bookmarks = bookmarks

    #image search url
    @property
    def search_url(self):
        return self.IMAGE_SEARCH_URL

    #search parameter "source_url"
    @property
    def source_url(self):
         return "/pin/"+ urllib.parse.quote(self.search_pin) +"/visual-search/" 

    #search parameter "data"
    @property
    def image_data(self):        
        if self.bookmarks == "":
            return '''{"options":{"isPrefetch":false,"pin_id":"''' + self.search_pin + '''","crop_source":5,"no_fetch_context_on_resource":false},"context":{}}'''
        else:
            return '''{"options":{"page_size":25,"pin_id":"''' + self.search_pin + '''","crop_source":5,"bookmarks":["''' + self.bookmark + '''"],"no_fetch_context_on_resource":false},"context":{}}'''.strip()

    @property
    def search_keyword(self):
        return self.search_pin
    
    @search_keyword.setter
    def search_keyword(self, search_pin):
        self.search_keywords = search_pin
    
    @property
    def file_length(self):
        return self.file_lengths
    
    @file_length.setter
    def file_length(self, file_lengths):
        self.file_lengths = file_lengths

    @property
    def image_quality(self):
        return self.image_qualitys
    
    @image_quality.setter
    def image_quality(self, image_qualitys):
        self.image_qualitys = image_qualitys

    @property
    def bookmark(self):
        return self.bookmarks

    @bookmark.setter
    def bookmark(self, bookmarks):
        self.bookmarks = bookmarks
    