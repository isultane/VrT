from itertools import count
from numpy import array
from cProfile import label
import os
from pydoc import Doc
import nltk
import pandas as pd
import re
import string
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize

from collections import Counter
def extract_top_25_cwes():
    dataset = './vuln_data/'
    for file in os.listdir(dataset):
        print('Processing ' + file)
        top25cwesource = open('top25cwe.txt', 'r')  
        for top25cwe in top25cwesource.readlines():
            cwe = top25cwe.split(None, 1)[0]
            cvesource = open(dataset+file, 'r+', encoding="UTF-8")
            data = cvesource.readlines()
            top25cwe_out = open('./vuln_data_top25cwe/'+str(file)+'top25cwe.txt', 'a')
            for line in data:
                label, text = line.split(' ', 1)
                oldcwe = label.split('__')[2]
                if oldcwe == cwe:
                    top25cwe_out.write(label + " " + text)
            cvesource.close()
            top25cwe_out.close()
    top25cwesource.close()

def count_unique_labels():
    data_set = './test/'
    print("Number of labels: ")

    for file in os.listdir(data_set):
        print('Processing ' + file)
   
        f = open(data_set+file, 'r+', encoding="UTF-8")
        data = array(f.readlines())
        labels_list = []
        
        for line in data:
            # print(line)
            label = line.split(' ')
            labels_list.append(label[0])
        
        print("Total number of unique labels: ", len(Counter(labels_list).keys())) # equals to list(set(words))
        # print("Total number of labels", sum(Counter(labels_list).values())) # counts the elements' frequency

       


# Returns a list of common english terms (words)
def initialize_words():
    content = None
    with open('./wordlist') as f: # A file containing common english words
        content = f.readlines()
    return [word.rstrip('\n') for word in content]

# source : https://stackoverflow.com/questions/20516100/term-split-by-hashtag-of-multiple-words
def parse_terms(term, wordlist):
    words = []
    word = find_word(term, wordlist)  
    while word != None and len(word) > 2:
        words.append(word)            
        if len(term) == len(word): # Special case for when eating rest of word
            break
        term = term[len(word):]
        word = find_word(term, wordlist)
    return " ".join(words)
# source: https://stackoverflow.com/questions/20516100/term-split-by-hashtag-of-multiple-words
def find_word(token, wordlist):
    i = len(token) + 1
    while i > 1:
        i -= 1
        if token[:i] in wordlist:
            return token[:i]
    return None 

def parse_sentence(sentence, wordlist):
    new_sentence = "" # output  
    tokens = re.findall(r'\w+\b', sentence)
 #   tokens = word_tokenize(sentence)
    # convert to lower cases
    tokens = [w.lower() for w in tokens]
    # prepare regex for char filtering
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
    # remove punctuation from each word
    tokens = [re_punc.sub(' ', w) for w in tokens]
    # filter out stop words
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if w not in stop_words]
    for term in tokens:
        new_sentence += parse_terms(term, wordlist)
        new_sentence += " "

    return " ".join(new_sentence.split())

if __name__ == '__main__':

    count_unique_labels()
    # data_set = './tmp/'
    # for file in os.listdir(data_set):
    #     print('Processing ' + file)

    #     f_out = './preprocessed_'+file
     
    #     # open the output file for writing
    #     file_1 = open(f_out, "w")

    #     wordlist = initialize_words()

    #     f = open(data_set+file, 'r+', encoding="UTF-8")
    #     data = array(f.readlines())
    #     out_data = []
        
    #     for line in data:
    #         # print(line)
    #         lable = line.split(' ')
    #         doc = line.split(" ", 1)[1]

            
    #         # pre-processing the input file (tokanizing, stop words, etc.)
    #         doc_preprocessed = parse_sentence(doc, wordlist)
    #         # wrting to the output file
    #         # print("Writing " + lable[0] +" to file")
    #         file_1.write(lable[0]+' '+doc_preprocessed +'\n') 
    #     # closing the output file
    #     file_1.close()
    #     print(f'Processed {len(data)} lines.')
       