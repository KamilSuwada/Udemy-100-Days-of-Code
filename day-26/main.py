import pandas as p
import os


CWD = os.path.dirname(__file__)

#list1 = [n for n in range(0, 101)]
#list2 = [n for n in list1 if n%2 == 0]

#dict1 = { str(value) : value for value in list1 }
#dict2 = { value : key for (key, value) in dict1.items()}



#students = {
    #"student" : ["Angela", "James", "Lily", "Kamil"],
    #"score" : [56, 76, 98, 100]
#}

#data = p.DataFrame(students)


#for (index, row) in data.iterrows():
    #print(f"{index} :   {row.student}, {row.score}")
    #print()

path = os.path.join(CWD, "nato_phonetic_alphabet.csv")
data = p.read_csv(path)
phonetic = {row.letter:row.code for (index, row) in data.iterrows()}

while True:
    word = input("Enter a word: ")

    try:
        letters = [letter.upper() for letter in word]
        word_phonetic = [phonetic[value] for value in letters]
    except KeyError:
        print("Your word contains unsupported characters.")
    else:
        print(" ".join(word_phonetic))
        break
