'''
Write a function that given a string, counts total number of consonants in it. 
A consonant is a English alphabet character that is not vowel (a, e, i, o and u). 
Examples of constants are b, c, d, f, g, ..
input will never have spaces or non letter characters

Examples: 

Input: 'snakes'
Output: 4

Input: 'SpamAndEggs'
Output: 8
'''

vowels = ["a", "e", "i", "o", "u"]

def count_const(word, count = 0):
    if word == "": return count

    if word[0].lower() not in vowels: count += 1

    return count_const(word[1:], count)

print(count_const('SpamAndEggs'))
