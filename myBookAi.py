import re
from collections import defaultdict
import collections
import tkinter as Tk
import string
filepath = r"C:\Users\270384\Downloads\Sample_book.txt"


class My_book_AI():
    @staticmethod                 #From here im creating all the lanaguge model necessary iteams
    def clean_data():
        with open (filepath,'r') as target_dataset:
            try:
                read_data = target_dataset.read()
                read_data = re.sub(r"[^a-zA-Z ]","", read_data)
                read_data = read_data.lower()
                read_data = read_data.split()
                return read_data 
            except Exception as e:
                print("not possible",e)
                return e

    @staticmethod
    def N_gram(tokens, N):
        ngram_dict = defaultdict(list)
        for i in range(len(tokens) - N):
            ngram = tuple(tokens[i:i+N])
            next_word = tokens[i+N]
            ngram_dict[ngram].append(next_word)
        return ngram_dict

    @staticmethod
    def word_frequency_counter():
        tokens = My_book_AI.clean_data()
        counter = collections.Counter(tokens)

        return dict(counter)
                   
    @staticmethod
    def Prediction_process(input_text):
        if not input_text.strip():
            return input_text,0,["space"]
        input_text = input_text.lower()
        input_text = re.sub(r"[^a-zA-Z ]","",input_text)
        input_text= tuple(input_text.split())
        #print(input_text)

        input_grams_size = len(input_text)

        book_N_gram = My_book_AI.N_gram(My_book_AI.clean_data(),input_grams_size)

        if input_text in book_N_gram:
            predicted_word = set(book_N_gram[input_text])
            #print(predicted_word)

        else:
            predicted_word=["Not predictable"]
            return input_text,input_grams_size,predicted_word

        return input_text,input_grams_size,predicted_word


"""a = My_book_AI.Prediction_process("r")

for k in a[2]:
    print(k)
"""




#---------------------------------------------------------------------UI PART----------------------------------------------------------------------------------------



def print_input(event):
    a = entry.get()
    a = a.lower()
    prediction = My_book_AI.Prediction_process(a)
    entry_1.delete("1.0",Tk.END)
    for k in prediction[2]:
        entry_1.insert(Tk.END,f"{k}\n")


main_win = Tk.Tk()
main_win.title("My first app in Tkinter")

entry = Tk.Entry(fg="black", bg="white", width=50,justify="left")
entry_1 = Tk.Text(fg="yellow", bg="blue", width=50,height=10)
entry_2 = Tk.Entry(fg="black", bg="white", width=50)

entry.pack()
entry_1.pack()
entry_2.pack()

entry.bind("<space>", print_input)
entry.bind("<Return>", print_input)

main_win.mainloop()