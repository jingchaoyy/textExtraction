from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

# from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
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

def dirExtract(contS):
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
    LANGUAGE = "english"
    SENTENCES_COUNT = 5

    fname = input("Input your file path: ")
    # e.g. /Users/YJccccc/PycharmProjects/tika/data/USING INFORMATION FROM RENDEZVOUS MISSIONS FOR BEST-CASE APPRAISALS OF IMPACT DAMAGE TO PLANET EARTH .pdf
    if os.path.exists(fname):
        # read though a file and extract content using Tika package
        content = rFile(fname)
        # separate extracted content by line break
        contSplit = content.split("\n")
        # print(contSplit)

        # first to look for keywords, if not shown, apply mining method
        texts = dirExtract(contSplit)

        # merge strings in the list to one
        keyW = ' '.join(texts[0])
        strAbstract = ' '.join(texts[1])

        if keyW == '':
            print("no direct keywords found, applying text mining")
        else:
            print(keyW)
        if strAbstract == '':
            print("no direct abstract found, applying text mining \nAbstract: ")
            parser = PlaintextParser.from_string(content, Tokenizer(LANGUAGE))
            stemmer = Stemmer(LANGUAGE)

            summarizer = Summarizer(stemmer)
            summarizer.stop_words = get_stop_words(LANGUAGE)

            for sentence in summarizer(parser.document, SENTENCES_COUNT):
                print(sentence)
        else:
            print("Abstract:", strAbstract)

    else:
        print("Please check your input path")

tEnd = time.time()
print("\nTotal time: ", tEnd - tStart, "seconds")
