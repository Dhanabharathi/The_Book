import re
from collections import defaultdict
import collections

filepath = r"C:\Users\270384\Downloads\Sample_book.txt"

def clean_data():
    with open (filepath,'r') as target_dataset:
        try:
            read_data = target_dataset.read()
            read_data = re.sub(r"[^a-zA-Z ]", "", read_data)
            read_data = read_data.lower()
            read_data = read_data.split()
            return read_data 
        except Exception as e:
            print("not possible",e)
            return e
    
"""def frequency_counter():
    tokens = clean_data()
    counter = collections.Counter(tokens)
    print(len(tokens))
    return dict(counter)
a = frequency_counter()
print(a)"""


input_text = "health plans also"
input_text = input_text.lower()
input_text= tuple(input_text.split())
input_grams_size = len(input_text)


def N_gram(tokens,N):
    length_of_token = len(tokens)
    ngram_dict = {}
    for i in range ((length_of_token-N)):
        ngram = tuple(tokens[i:i+N])
        next_word = tokens[i+N] if i+N < length_of_token else None
        ngram_dict[ngram] = next_word
    return ngram_dict

book_N_gram = N_gram(clean_data(),input_grams_size)
#print(book_N_gram)


if input_text in book_N_gram:
        result = ''.join(book_N_gram[input_text])
        print(result)
else:
        print("not predictable")