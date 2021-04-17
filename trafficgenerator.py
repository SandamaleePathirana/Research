#!/usr/bin/python3
import time
slog= open('access.log20200530','r')
#logfl = open('mod_log1.arff','a')
squid_lines = slog.readlines()
for line in squid_lines:
    clean_line = ' '.join(line.split())
    splt_line = clean_line.split()
    #print (float(splt_line[0]))
    time_ = splt_line[0]
    #print(time_)
    duration = splt_line[1]
    ip_addr  = splt_line[2]
    result_code = splt_line[3]
    size = splt_line[4]
    methode = splt_line[5]
    url = splt_line[6]
    user = splt_line[7]
    ftype = splt_time[8]
    print (ftype)
    str_to_write = time_+','+duration+''+ip_addr+','+result_code+','+size+''+methode+''+url+''+user+''+ftype
    #logfl = open('/root/squid_log1/mod_log6.csv','a')
    #logfl.write(str_to_write + "\n")
    #logfl.close()