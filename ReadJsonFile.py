# ReadJsonFile
# Description:
# Read data.txt produced by M. Sanchez in March 2014; output a list of owner ids for
# each photograph.  Formatting is at my discretion.

# Testing with Xcode:
#print 'Hello, world!'

import os.path
import json
################################################################################
################################################################################
def GrabJsonFileData(FileName):
    with open(FileName) as json_data:
        data = json.load(json_data)
    json_data.close()
    return data

################################################################################
################################################################################
if __name__ == '__main__':
    JsonFileName = '/Users/danahipolite/Downloads/data.txt'
    JsonData = GrabJsonFileData(JsonFileName)
    for val in JsonData:
        print 'Owner: ', val["owner"], ' Id: ', val["id"]
        print ''
