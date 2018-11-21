import json
def writeToJson():
    fName = 'C:/Users/Harun ER/Python/fileOperations/jsonFile'
    f = open(fName, 'w')
    json.dump([1, 'simple', 'list'],f)
    f.close()

def readFromJson():
    fName = 'C:/Users/Harun ER/Python/fileOperations/jsonFile'
    f = open(fName, 'r')
    x = json.load(f)
    f.close()
    return x
