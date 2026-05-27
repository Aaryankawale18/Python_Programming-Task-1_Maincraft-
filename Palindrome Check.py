
word = input("Enter a word: ")

reversed_word = word[::-1]

if word == reversed_word:
    print(word, "is a Palindrome")
else:
    print(word, "is not a Palindrome")
