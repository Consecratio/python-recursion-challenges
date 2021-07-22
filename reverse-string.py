'''
Write a recursive function called reverse that accepts a string and returns a reversed string.

Examples:

input: "computer"
output: "retupmoc"

input: "ab"
output: "ba"

input: "abcdefghijklmnopqrstuvwxyz"
output: "zyxwvutsrqponmlkjihgfedcba"

input: reverse("computer")
output: "computer"
'''

def reverse(word, newWord = "", num = 0):
    if num == len(word): return newWord

    newWord = word[num] + newWord
    
    return reverse(word, newWord, num + 1)


print(reverse(reverse("computer")))