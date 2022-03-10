#+-------------------------+
#| lab6c.py - Isaiah Grace |
#+-------------------------+

# Task 3 - For-loops

# A ---
for num in range(1, 11):
    print(num)

for num in reversed(range(1, 11)):
    print(num)

# B ---
for threes in range(0, 101, 3):
    print(threes)

# C ---
fnames = ('John', 'Mary', 'Mohammed', 'Olga')

for names in fnames:
    print(names)

# D ---
for names in fnames:
    print(names)

# E ---
quote = "The-only-way-to-learn-a-new-programming-language-is-to-write-programs-in-it."

print(' '.join(quote.split('-')))

