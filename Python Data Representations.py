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
"""
"""
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
