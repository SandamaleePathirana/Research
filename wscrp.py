from datetime import datetime
from time import sleep
import time
        
class WSCRPCacheItem(object):
    """Data structure of items stored in cache"""
    def __init__(self, key, item):
        self.key = key
        self.item = item
        self.timestamp = datetime.now()
        self.wscrp = value

class WSCRPCache(object):
    """A sample class that implements WSCRP algorithm"""

    def __init__(self, length,size,frequency,trequest,numofcopy,bandwidth, delta=None):
        self.length = length
        self.delta = delta
        self.hash = {}
        self.item_list = []
        self.size = size
        self.frequency = frequency
        self.trequest = trequest
        self.numofcopy = numofcopy
        self.bandwidth = bandwidth
        self.difftime = difftime
        
    def __init__(self,c2):
        for i in item_list[]
            c2 =+ (bandwidth*size*trequest)
            
    def __init__(c1):
        for j in item_list[]
            c1 = (bandwidth*size*numofcopy)

    def insertItem(self, item):
        """Insert new items to cache"""
        #print("========")
        #print(self.hash)
        #print(self.item_list)
        
        if item.key in self.hash:
            # Move the existing item to the head of item_list.
            pre_item = self.hash[item.key]
            # print(pre_item)
            item_index = self.item_list.index(pre_item)
            self.item_list[:] = self.item_list[:item_index] + self.item_list[item_index+1:]
            self.item_list.insert(0, item)
            self.hash[item.key] = item
            self.item_list[csv] = c1/c2
            self.item_list[item.value] = (item_list[:]/(frequency*difftime))* size/(csv)
        else:
            # Remove the last item if the length of cache exceeds the upper bound.
            if len(self.item_list) > self.length:
                self.removeItem(self.item_list[-1])


            # If this is a new item, just append it to
            # the front of item_list.
            self.hash[item.key] = item
            # print(item.key)
            self.item_list.insert(0, item)
            self.hash[item.key] = item
            self.item_list[csv] = c1/c2
            self.item_list[item.value] = (item_list[:]/(frequency*difftime))* size/(csv)
        
    
    def removeItem(self, item):
        """Remove those invalid items"""
        #print('rem item ; '+ str(item))
        del self.hash[item.key]
        del self.item_list[self.item_list.index(item)]
        del self.item_list[self.item_list[item.value]]
        
    def replaceItem(self,value):
        def _outsized_items():
            thre_size = 65000
            for item in self.item_list:
                it_size =  int(item.item.split(' ')[1])
                if thre_size < it_size:
                    yield item
    
    def validateItem(self):
        """Check if the items are still valid."""
        
        def _outdated_items():
            now = datetime.now()
            for item in self.item_list:
                time_delta = now - item.timestamp
                if time_delta.seconds > self.delta:
                    yield item
        

        def _outsized_items():
            thre_size = 65000
            for item in self.item_list:
                it_size =  int(item.item.split(' ')[1])
                if thre_size < it_size:
                    yield item
        
        # Remove outsized cache 
        for genit_os in _outsized_items():
            self.removeItem(genit_os)

        # Remove outdated cache
        for genit_od in _outdated_items():
            self.removeItem(genit_od)

   
def print_cache(cache, fl):
   for csv in enumerate item_list[cache.item_list]
        for i, item in enumerate(cache.item_list):
            fl.write("index: {0} "
                    "key: {1} "
                    "item1: {2} "
                    "timestamp: {3}\n".format(i,
                                       item.key,
                                       item.item,
                                       item.timestamp))


slog= open('datasets/access-0.log','r')
squid_lines = slog.readlines()

cache = LRUCache(length=300, delta=5)
logfl = open('mod_log23.csv','a')
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
  
    str_to_write = LRUCacheItem(url,(result_code+" "+size))
   
    cache.insertItem(str_to_write)  
    cache.validateItem()
    
    sleep(0.001)

with logfl as out:
    print_cache(cache, out)


logfl.close()
