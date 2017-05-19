

def parse(data):
    #print "Hello Parse function, The data is ",data
    print data[1]
    print len(data)
    for i in range(0, len(data)):
        print data[i]['title']+'\n'
