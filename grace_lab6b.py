#+-------------------------+
#| lab6b.py - Isaiah Grace |
#+-------------------------+

# Task 2 - Tuples

fnames = ('John', 'Mary', 'Mohammed', 'Olga')
lnames = ('Hollis', 'Redwater', 'Lee', 'Smith')


# A ---

index = 0
while index < 4:
    print(f"{fnames[index]} {lnames[index]}")
    index += 1


# B ---

index = -1
while index > -5:
    print(f"{fnames[index]} {lnames[abs(index) - 1]}")
    index -= 1


# C ---

first_n_last = zip(fnames, lnames)

init_tuple = ((names[0][0] + names[1][0]) for names in first_n_last)

for inits in init_tuple:
    print(inits)

# D ---

for firsts in fnames:
    for lasts in lnames:
        print(f"{firsts} {lasts}")
        


