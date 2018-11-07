"""
Week1
"""
"""
Write a function \color{red}{\verb|count_vowels(word)|}count_vowels(word) that takes the string \color{red}{\verb|word|}word as input and returns the number of occurrences of lowercase vowels (i.e. the lowercase letters \color{red}{\verb|"aeiou"|}"aeiou") in \color{red}{\verb|word|}word. Hint: Python has a built-in string method that can count the number of occurrences of a letter in a string.
The first statement should print \color{red}{\verb|13|}13 in the console. 
"""
def demystify(l1_string):
    a1_string = l1_string.replace('l','a')
    ab_string = a1_string.replace('1','b')
    return ab_string

print(demystify("lll111l1l1l1111lll"))
print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))

"""
Write a function \color{red}{\verb|demystify(l1_string)|}demystify(l1_string) that takes a string composed of the characters \color{red}{\verb|"l"|}"l" and \color{red}{\verb|"1"|}"1" and returns the string formed by replacing each instance of \color{red}{\verb|"l"|}"l" by \color{red}{\verb|"a"|}"a" and each instance of \color{red}{\verb|"1"|}"1" by \color{red}{\verb|"b"|}"b".
The first call should print the string \color{red}{\verb|"aaabbbabababbbbaaa"|}"aaabbbabababbbbaaa" in the console.
"""
def count_vowels(word):
    num = word.count('a')+word.count('e')+word.count('i')+word.count('o')+word.count('u')
    return num

print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))
print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))


"""
Week2
"""
"""
Write a function \color{red}{\verb|strange_sum(numbers)|}strange_sum(numbers) that takes a list of integers and returns the sum of those items in the list that are not divisible by 33. When you are done, test your function using the code snippet below.
"""
def strange_sum(alist):
    sum=0
    for item in alist:
        if item % 3 != 0:
            sum += item
    return sum


print(strange_sum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
print(strange_sum(list(range(123)) + list(range(77))))
