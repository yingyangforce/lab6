#+---------------------+
#| lab6 - Isaiah Grace |
#+---------------------+

# Task 1 - Slicing

quote = "The-only-way-to-learn-a-new-programming-language-is-to-write-programs-in-it."

#A - print "only-way-to-learn"
print(quote[4:21])

#B - print first half of string
print(quote[:len(quote)//2])

#C - rm last two words, keep period
print(quote[:-7], end=".\n")

#D - print every second letter
print(quote[::2])

#E - print all words that start w/ 'p'
p_list = [print(word) for word in quote.split('-') if word[0] == 'p']

