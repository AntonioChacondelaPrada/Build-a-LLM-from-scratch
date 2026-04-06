from tokenizer import SimpleTokenizer1

tokenizer = SimpleTokenizer1(vocab)
text = """"It's the last he painted, you know,"Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print(ids)