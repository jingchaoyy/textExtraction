## This function assume the keywords for "abstract" and "keywords"
# exists in the paper

from tika import parser
import time
import os.path

tStart = time.time()

# read file and return all content
def rFile(fPath):
    # parser is a Tika package function
    parsed = parser.from_file(fPath)
    cont = parsed["content"]
    meta = parsed["metadata"]
    # print (parsed)
    return cont

def getString(contS):
    # initiate keyword list and abstract list
    keyWd,abstr = [], []
    # iterate every string in separated string list
    for i in contS:
        # check if specified string is in the list
        if "Keywords:" in i:
            keyWd.append(i)
            # # print(keyWd)
            # # find the start point using keyword "Keywords:"
            # keyStart = contS.index(i)
            # # for loop to allocate all keywords, until next line break symbol
            # for j in contS[keyStart:len(contS)]:
            #     if j != ' ':
            #         keyWd.append(j)
            #     else:
            #         break
            
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

if __name__ == "__main__":
    fname = input("Input your file path: ")
    # e.g. data/USING INFORMATION FROM RENDEZVOUS MISSIONS FOR BEST-CASE APPRAISALS OF IMPACT DAMAGE TO PLANET EARTH .pdf
    if os.path.exists(fname):
        # read though a file and extract content using Tika package
        content = rFile(fname)
        # separate extracted content by line break
        contSplit = content.split("\n")
        # print(contSplit)

        texts = getString(contSplit)

        # merge strings in the list to one
        keyW = ' '.join(texts[0])
        strAbstract = ' '.join(texts[1])

        if keyW == '':
            print("no keywords found")
        else:
            print(keyW)
        if strAbstract == '':
            print("no abstract found")
        else:
            print("Abstract:", strAbstract)

    else:
        print("No such file")

tEnd = time.time()
print("\nTotal time: ", tEnd - tStart, "seconds")
