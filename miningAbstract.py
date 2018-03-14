from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

# from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

# from sumy._compat import to_unicode

from tika import parser
import time

tStart = time.time()

def rFile(fPath):
    # parser is a Tika package function
    parsed = parser.from_file(fPath)
    cont = parsed["content"]
    meta = parsed["metadata"]
    # print (parsed)
    return cont

LANGUAGE = "english"
SENTENCES_COUNT = 5

# class Child(PlaintextParser):
#     def from_file(cls, file_path, tokenizer):
#         with open(file_path, 'rb') as file:
#             return cls(file.read(), tokenizer)
#
#     def __init__(self, text, tokenizer):
#         super(PlaintextParser, self).__init__(tokenizer)
#         self._text = to_unicode(text).strip()

if __name__ == "__main__":
    # fPath = "/Users/YJccccc/PycharmProjects/tika/data/Untitled.txt"
    # parser = PlaintextParser.from_file(fPath, Tokenizer(LANGUAGE))
    fPath = "/Users/YJccccc/PycharmProjects/tika/data/USING INFORMATION FROM RENDEZVOUS MISSIONS FOR BEST-CASE APPRAISALS OF IMPACT DAMAGE TO PLANET EARTH .pdf"
    str = rFile(fPath)
    parser = PlaintextParser.from_string(str, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)

tEnd = time.time()
print("\nTotal time: ", tEnd - tStart, "seconds")
