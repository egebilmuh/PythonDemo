def readFile(fileName):
    fName = 'C:/Users/Harun ER/Python/fileOperations/'+fileName
    f = open(fName)
    for line in f:
        print (line, end='')
    f.close()

