from datetime import datetime
from time import sleep
import time

class CacheService(object):

    def __init__(self):
        self.data = {}

    def __setitem__(self, key, item):
        self.data[key] = [item, 0]

    def __getitem__(self, key):
        value = self.data[key]
        value[1] += 1
        return value[0]

    def getcount(self, key):
        return self.data[key][1]
        
>>> cs = CacheService()
>>> cs[1] = 'one'
>>> cs[2] = 'two'
>>> print cs.getcount(1)
0
>>> cs[1]
'one'
>>> print cs.getcount(1)
1

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