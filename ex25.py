def break_words(stuff):
"""This function will break up words for us."""
words = stuff.split(' ')
return words

def sort_words(words):
"""Sorts the words."""
return sorted(words)

def print_first_word(words):
"""Prints the first word after popping it off."""
word = words.pop(0)
print word

15 def print_last_word(words):
16 """Prints the last word after popping it off."""
17 word = words.pop(- 1)
18 print word
19
20 def sort_sentence(sentence):
21 """Takes in a full sentence and returns the sorted words."""
22 words = break_words(sentence)
23 return sort_words(words)
24
25 def print_first_and_last(sentence):
26 """Prints the first and last words of the sentence."""
27 words = break_words(sentence)
28 print_first_word(words)
29 print_last_word(words)
30
31 def print_first_and_last_sorted(sentence):
32 """Sorts the words then prints the
