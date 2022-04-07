#sources:
#askpython.com/python/examples/list-files-in-a-directory-using-python
#codegrepper.com/code-examples/python/python+sha256+of+file
#pynative.com/python-file-creation-modification-datetime
#stackoverflow.com/questions/15578331/save-list-of-ordered-tuples-as-csv
#stackoverflow.com/questions/18776370/converting-a-csv-file-into-a-list-of-tuples-with-python
import os
import hashlib
import datetime
import csv

path = '/'
storelist = []

for path, folders, files in os.walk(path):
    if ("/usr" not in str(path)) and ("/dev" not in str(path)) and ("/proc" not in str(path)) and ("/run" not in str(path)) and ("/sys" not in str(path)) and ("tmp" not in str(path)) and ("/var/lib" not in str(path)) and ("/var/run" not in str(path)):
        for file in files:    
            #Part 1: if you want to print out filename with paths and take no action
            filepath = (os.path.abspath(os.path.join(path,file)))
            #Part 2: Integrate SHA256 so that each file is hashed as it moves through
            sha256_hash = hashlib.sha256()
            try:
                with open (file, 'rb') as f:
                    for byte_block in iter(lambda: f.read(4096),b""):
                        sha256_hash.update(byte_block)
                    hashfile = sha256_hash.hexdigest()
                  #  print(filepath)
                   # print(hashfile)
                   #Find modified date/time
                    mtime = os.path.getmtime(filepath)
                    dt_m = datetime.datetime.fromtimestamp(mtime)
                    #store information as a tuple
                    info = (filepath, hashfile, dt_m)
                    
                    #check csv file to check for any updates later
                    with open('/home/sy402/test.csv','r') as check:
                        data=[tuple(line) for line in csv.reader(check)]
                        #print(info)
                        for infodata in data:
                            if infodata == info:
                                print('this is not new' + str(info))
                            else:
                                print('this info is new' + str(info))
                                #add to csv file if there is some new information
                                csv_writer= csv.writer(check)
                                csv_writer.writerow(info)   
                
            except:
                    pass
                
for tuples in storelist:
    print(tuples)


