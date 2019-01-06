"""
Week1 
Write a function count_letters(word_list) that takes as input a 
list of words that are composed entirely of lower case letters . 
This function should return the lower case letter that appears 
most frequently (total number of occurrences) in the words in 
word_list. (In the case of ties, return the earliest letter in 
alphabetical order.)
The Python code snippet below represents a start at implementing 
count_letters using a dictionary letter_count whose keys are the 
lower case letters and whose values are the corresponding number 
of occurrences of each letter in the strings in word_list.
Complete your implementation of count_letters based on this snippet.
As a test, count_letters(["hello","world"]) should return the 
letter ’l’ since ’l’ appears 3 times total in the strings "hello" 
and "world".When you are confident in your code, compute the 
lower case letter return by count_letters(monty_words) where 
monty_words is defined as shown.
"""
def count_letters(word_list):
    """ See question description """
    #转换为能够计数的类型list
    phrase=""
    for item in word_list:
        phrase+=str(item)
    phrase_list=list(phrase)
    
    #创建字典
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    letter_count = {}
    for letter in ALPHABET:
        letter_count[letter] = phrase_list.count(letter)
    
    #输出value最大的key.如果相等就按alphrabet的顺序
    max_key=''
    max_value=0
    for key in letter_count:
        value=letter_count[key]
        if value > max_value:
            max_value=value
            max_key=key
    return max_key
#test for result 'l'    
print(count_letters(['hello','world']))

monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"

monty_words = monty_quote.split(" ")

print(count_letters(monty_words))
