import sys, base64

def fileToB64(fileToConvert):
    output = open('output.txt','w+')

    with open(fileToConvert, 'rb') as bFile:
        bData = bFile.read()
        b64Data = base64.b64encode(bData)
        b64Data = b64Data.decode('utf-8')

    output.write(b64Data)

parameterList = sys.argv

if len(parameterList) == 1:
    sys.exit(0)
else:
    fileToB64(parameterList[1])