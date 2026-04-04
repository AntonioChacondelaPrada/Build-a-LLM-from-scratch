# TOKENIZING TEXT

import urllib.request
import re
url = ("https://raw.githubusercontent.com/rasbt/"
       "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
       "the-verdict.txt")
filepath = "the-verdict.txt"
urllib.request.urlretrieve(url, filepath)

with open("the-verdict.txt", "r", encoding="utf-8") as f:
       raw_text = f.read()
# print("Total number of character: ", len(raw_text))
# print(raw_text [:99])

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
# print(len(preprocessed))
# print(preprocessed[:30])

#CONVERTING TOKENS INTO IDs

all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
vocab = {token: integer for integer, token in enumerate(all_words)}

# for i, item in enumerate(vocab.items()):
#        print(item)
#        if i >= 50:
#               break

