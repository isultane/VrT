import nltk
import string
import re
from nltk.corpus import stopwords


#nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')
print(len(stopwords))

stopwords.append("prior")
stopwords.append("versions")
stopwords.append("cve")
stopwords.append("CVE")
stopwords.append("wndr")
stopwords.append("rax")
stopwords.append("rs")
stopwords.append("xr")
stopwords.append("rbr")

print(len(stopwords))

def RemoveStopwords(text):
  TextClean = [word for word in text if word not in stopwords]
  return TextClean



def NLP1(X):
  Description = X
  tokens = Description.split()
  tokens = RemoveStopwords(tokens)
  Description = ''
  for token in tokens:
    Description = Description +" " + token
  alphabet = list(string.ascii_uppercase)
  pattern = r'[0-9]'
  spaciel = r'[^A-Za-z0-9]+'
  Description = Description.upper()
  Description = re.sub(spaciel," ",Description)
  Description = re.sub(pattern,"",Description)
  re.sub("\s\s+", " ", Description)
  Description = re.sub(' +', ' ',Description)
  tokens = Description.split()
  for i in range(1,len(tokens)):
    for j in alphabet :
      if tokens[i] == j:
        tokens[i]=''
  Description = ''
  for token in tokens:
    Description = Description +" " + token
  return Description
