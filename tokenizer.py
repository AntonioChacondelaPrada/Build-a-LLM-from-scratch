import re

class SimpleTokenizer1:
    def __init__(self, vocab):
        #stores the vocabulary as a class attribute for access in the encode and decode methods
        self.str_to_int =  vocab
        #Crates an inverse vocabulary that maps token IDs back to the original text tokens
        self.int_to_str = {i:s for s,i in vocab.items()}

    # encode function- Processes input text into token IDs
    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
    # decode function - Converts token IDs back into text
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        #Removes spaces before the specified punctiation
        text = re.sub(r'\s+([,.?!"()\'])', r'\l', text)
        return text


tokenizer = SimpleTokenizer1(vocab)
text = """"It's the last he painted, you know,"Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print(ids)