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
Write a Python expression that creates a list of length 16 whose first 8 entries are \color{red}{\verb|True|}True and whose last 8 entries are \color{red}{\verb|False|}False . Note that your answer should not include more than one instance of \color{red}{\verb|True|}True and one instance of \color{red}{\verb|False|}False in the expression used to create the list. 
"""
truefalse_list =[True] * 8 + [False] * 8
print(truefalse_list)
#This example tells that the list object can be formed by "add". And the repetition number of element should be outside the list expression.

"""
Challenge: Write a Python function \color{red}{\verb|concatenate_ints(int_list)|}concatenate_ints(int_list) that takes a list of non-negative integers \color{red}{\verb|int_list|}int_list and returns a single integer formed by concatenating the digits of the integer in the list. For example, \color{red}{\verb|list_to_int([11, 33, 50])|}list_to_int([11,33,50]) should return the integer \color{red}{\verb|113350|}113350.
"""
def concatenate_ints(int_list):
    """
    Given a list of integers int_list, return the integer formed by
    concatenating their decimal digits together
    """
    new_list=""
    for item in int_list:
        new_list = new_list + str(item)
    return new_list
# Tests
print(concatenate_ints([4]))
print(concatenate_ints([4, 0, 4]))
print(concatenate_ints([123, 456, 789]))
print(concatenate_ints([32, 796, 1000]))
#This task looks similar to the above one, but different in "string" and [list].
#String should initiate at "", then concatenate str(item) directly by "+"sign. List is [item] * repetition.

"""
Select the code snippets below in which \color{red}{\verb|list2|}list2 is a copy of list \color{red}{\verb|list1|}list1 (as opposed to simply being another reference to the list \color{red}{\verb|list1|}list1).
"""
list1 = list(range(1, 10))
list2 = list1
print(list1," ",list2)
list2[0]=3
print(print(list1," ",list2))
"""
[1, 2, 3, 4, 5, 6, 7, 8, 9]   [1, 2, 3, 4, 5, 6, 7, 8, 9] 
[3, 2, 3, 4, 5, 6, 7, 8, 9]   [3, 2, 3, 4, 5, 6, 7, 8, 9]
So list2 is exact the list1. The list2 is considered "reference" that points to list1. Any changes in the list under either variable name will be reflected in the other.
(Thank Patrick Dennis, MD for his kind answer)
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



"""
Week3
"""

"""
Given a list \color{red}{\verb|example_list|}example_list containing at least 4 elements, write an expression that replaces the second and third elements of the list by the list \color{red}{\verb|[0, 0, 0]|}[0,0,0] . 
Shortly - Update a slice of a list
"""
example_list = [2, 3, 5, 7, 11, 13]
print(example_list)
example_list[1:2]=[0,0]
print(example_list)
#This Slice Updata part tells that lst[num]=[item1,item2,...] will create a new list inside the list lst
#Using lst[num:num+1]=[item1,item2,...] instead have the effect of "replace" multiple items on one given position.
#For extend multiple items to the end of the list, using lst.extend([item1,item2,...])
#list.append() adds the argument as an object, list.extend() adds the context of the sequence.
#If need to create a new list from the original one, use new_list = old_list + [item1,item2,...]

"""
Using loop to append item to the list
"""
for number in [0, 0, 0]:
    example_list.append(number)    
print(example_list)

"""
Challenge: The items in a list can themselves be lists. These nested lists can be used to represent a wide range of 2D data such as spreadsheet information. Write a function \color{red}{\verb|flatten(nested_list)|}flatten(nested_list) that takes as input the list of lists \color{red}{\verb|nested_list|}nested_list. The function \color{red}{\verb|flaten()|}flaten() should return a list consisting of the items in the sublists of \color{red}{\verb|nested_list|}nested_list all appended together. (See the provided template for example input and output.) 
Shortly - Flatten a nested list
"""
def flatten(nested_list):
    """
    Given a list whose items are list, 
    return the list formed by joining all of these lists
    """
    flattened_list=[]
    for sub_list in nested_list:
        flattened_list.extend(sub)
    return flattened_list
# Test code
print(flatten([]))
print(flatten([[]]))
print(flatten([[1, 2, 3]]))
print(flatten([["cat", "dog"], ["pig", "cow"]]))
print(flatten([[9, 8, 7], [6, 5], [4, 3, 2], [1]]))
#The difference between week2's concatenate_ints and this one is that weeks create an empty string, and this one empty list.

"""
Challenge: Write a function \color{red}{\verb|remove_duplicates(items)|}remove_duplicates(items) that takes a list \color{red}{\verb|items|}items and returns a new list that consists of all unique items in \color{red}{\verb|items|}items. The items in the returned list should be in the same order as those in \color{red}{\verb|items|}items.
Shortly - Remove duplicates from a list while preserving the order of items
"""
def remove_duplicates(items):
    """
    Given a list, return a list with duplicate items removed
    and the remaining items in the same order
    """
#    new_list=list(items)
#    for item in new_list:
#        if new_list.count(item) > 1:
#            new_list.remove(item)
#    return new_list   #This does not work well for requirement because the order has changed.
    new_list=[]
    for item in items:
        if item not in new_list:
            new_list.append(item)
    return new_list
# Test code
print(remove_duplicates([]))
print(remove_duplicates([1, 2, 3, 4]))
print(remove_duplicates([1, 2, 2, 3, 3, 3, 4, 5, 6, 6]))
print(remove_duplicates(["cat", "dog", "cat", "pig", "cow", "cat", "pig", "pug"]))
#The pseud-algorithm is listed as follows:()
#myList = [1, 2, 3, 1, 2, 5, 6, 7, 8]
#cleanlist = []
#[cleanlist.append(x) for x in myList if x not in cleanlist]

"""
Given a list \color{red}{\verb|fib = [0, 1]|}fib=[0,1], write a loop that appends the sum of the last two items in \color{red}{\verb|fib|}fib to the end of \color{red}{\verb|fib|}fib. What is the value of the last item in \color{red}{\verb|fib|}fib after twenty iterations of this loop? Enter the answer below as an integer.
As a check, the value of the last item in \color{red}{\verb|fib|}fib after ten iterations is 89.
"""
def mysum(lst,iteMax):
    templist=lst[:]
    sum=0
    for i in range(iteMax):
        lastsum=templist[-2]+templist[-1]
        templist.append(lastsum)
    return lastsum
fib=[0,1]
print(mysum(fib,10))
print(mysum(fib,20))

"""
One of the first examples of an algorithm was the Sieve of Eratosthenes. This algorithm computes all prime numbers up to a specified bound. The provided code below implements all but the innermost loop for this algorithm in Python. Review the linked Wikipedia page and complete this code.
Implement the Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""
def compute_primes(bound):
    """
    Return a list of the prime numbers in range(2, bound)
    """
    
    answer = list(range(2, bound))
    for divisor in range(2, bound):
        # Remove appropriate multiples of divisor from answer
        pass
    return answer

print(len(compute_primes(200)))
print(len(compute_primes(2000)))



"""
Week4
"""
