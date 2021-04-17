from datetime import datetime
from time import sleep
import time

class LRUCacheItem(object):
    """Data structure of items stored in cache"""
    def __init__(self, key, item):
        self.key = key
        self.item = item
        self.timestamp = datetime.now()


class LRUCache(object):
    """A sample class that implements LRU algorithm"""

    def __init__(self, length, delta=None):
        self.length = length
        self.delta = delta
        self.hash = {}
        self.item_list = []

    def insertItem(self, item):
        """Insert new items to cache"""

        if item.key in self.hash:
            # Move the existing item to the head of item_list.
            #print(self.item_list)
            item_index = self.item_list.index(item)
            self.item_list[:] = self.item_list[:item_index] + self.item_list[item_index+1:]
            print(self.item_list[0])
            self.item_list.insert(0, item)
        else:
            # Remove the last item if the length of cache exceeds the upper bound.
            if len(self.item_list) > self.length:
                self.removeItem(self.item_list[-1])

            # If this is a new item, just append it to
            # the front of item_list.
            self.hash[item.key] = item
            self.item_list.insert(0, item)

    def removeItem(self, item):
        """Remove those invalid items"""

        del self.hash[item.key]
        del self.item_list[self.item_list.index(item)]

    def validateItem(self):
        """Check if the items are still valid."""

        def _outdated_items():
            now = datetime.now()
            for item in self.item_list:
                time_delta = now - item.timestamp
                if time_delta.seconds > self.delta:
                    yield item
        map(lambda x: self.removeItem(x), _outdated_items())
        
def print_cache(cache):
   for i, item in enumerate(cache.item_list):
       return ("index: {0} "
               "key: {1} "
               "item: {2} "
               "timestamp: {3}".format(i,
                                       item.key,
                                       item.item,
                                       item.timestamp))


slog= open('access','r')
squid_lines = slog.readlines()

cache = LRUCache(length=3, delta=5)
logfl = open('./mod_log16.csv','a')
for line in squid_lines:
    clean_line = ' '.join(line.split())
    splt_line = clean_line.split()
    #print (float(splt_line[0]))
    time_ = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(splt_line[0])))
    #print(time_)
    duration = splt_line[1]
    ip_addr  = splt_line[2]
    result_code = splt_line[3]
    size = splt_line[4]
    methode = splt_line[5]
    url = splt_line[6]
    user = splt_line[7]
    ftype = splt_line[8]
    # print (ftype)
    # str_to_write = time_+','+ip_addr+','+result_code+','+size
    # str_to_write = LRUCacheItem(line, time_+','+ip_addr+','+result_code+','+size)
    # cache.insertItem(str_to_write)'
    # print (str_to_write)   
    
#logfl = open('./mod_log15.csv','a')
    str_to_write = LRUCacheItem(time,(ip_addr+size))
    #cache = LRUCache(length =3, delta =5)
#print_cache(cache+"\n")

# **************TESTING*****************************************
    cache.insertItem(str_to_write)  
# **************************************************************

#cache.insertItem(str_to_write)
#print(print_cache(cache))
#print ("-" * 100)

#print(print_cache(cache))
#print( "-" * 100)

#cache.insertItem(str_to_write)
#print(print_cache(cache))
#print( "-" * 100)
  
    sleep(3)
cache.validateItem()
with logfl as out:
    out.write(print_cache(cache)+"\n")


logfl.close()
