## This function assume the keywords for "abstract" and "keywords"
# exists in the paper

from tika import parser
import time
import os

tStart = time.time()

pdfTest = 'USING INFORMATION FROM RENDEZVOUS MISSIONS FOR BEST-CASE APPRAISALS OF IMPACT DAMAGE TO PLANET EARTH .pdf'

# read file and return all content
def rFile(fPath):
    # parser is a Tika package function
    parsed = parser.from_file(fPath)
    cont = parsed["content"]
    meta = parsed["metadata"]
    # print (parsed)
    return cont

# read though a file and extract content using Tika package
content = rFile(pdfTest)
# separate extracted content by line break
contSplit = content.split("\n")

def getString(contS):
    # initiate keyword list and abstract list
    keyWd,abstr = [], []
    # iterate every string in separated string list
    for i in contS:
        # check if specified string is in the list
        if "Keywords:" in i:
            # keyWd = contS[i]
            # print(keyWd)
            # find the start point using keyword "Keywords:"
            keyStart = contS.index(i)
            # for loop to allocate all keywords, until next line break symbol
            for j in contS[keyStart:len(contS)]:
                if j != ' ':
                    keyWd.append(j)
                else:
                    break

        if "ABSTRACT" in i or "Abstract—" in i:
            # find the start point using keyword "Abstract", some time it's "Abstract—"
            for j in contS[contS.index(i) + 1:len(contS)]:
                if j != '' and j != ' ':
                    abstrStart = contS.index(j)
                    break
            # for loop to allocate all strings for abstract in the list, until next line break symbol
            for k in contS[abstrStart:len(contS)]:
                # print(contSplit[abstrStart:len(contSplit)])
                if k != ' ':
                    abstr.append(k)
                else:
                    break

    return keyWd, abstr


# for filename in os.listdir("/Users/YJccccc/PycharmProjects/tika/data"):
#     if filename.endswith(".pdf"):
#         # read though a file and extract content using Tika package
#         content = rFile("/Users/YJccccc/PycharmProjects/tika/data/"+filename)
#         # separate extracted content by line break
#         contSplit = content.split("\n")
#         test = getString(contSplit)


texts = getString(contSplit)

# merge strings in the list to one
keyW = ' '.join(texts[0])
strAbstract = ' '.join(texts[1])

if keyW =='':
    print("no keywords found")
else:
    print(keyW)
if strAbstract =='':
    print("no abstract found")
else:
    print("\nAbstract:", strAbstract)


tEnd = time.time()
print("\nTotal time: ", tEnd - tStart, "seconds")
