
#        KHOA NGO
#   3. FILE CHALLENGE

#       QUESTIONS
#
# a)    Describe an algorithm to solve this problem.
#       First, read lines from .txt file then append them to an empty list.
#       Each index in the list now contains the unique identifier and the name separated by space.
#       Split the indexes by ' ', once for each index.
#       We now have lists within a list.
#       list[n][0] will contain the unique identifier and list[n][1] will contain the name (n = len(list) - 1)
#       Repeat procedure for the second file.
#       Now we can compare the unique identifiers using for loops.
#       If they match, append the entries from each file into a result list.
#       Print result list.
#
# b)    Write pseudo-code for your algorithm.
#       I wrote my code below in Python so I guess that counts as pseudo-code.
#
# c) What are the pros and cons to your approach?  What computational limitations might force you to do something differently, and what would that be?
#       Pros:
#       I believe this is the simplest method to accomplish the objective.
#       It also allows me to split the first and last names later on if I would like to.
#       Cons:
#       I believe execution speed could suffer when there are huge amount of data
#       as the final part involves comparing every character in each index.
#
#       A potential improvement for dealing with large amount of data is:
#       I noticed there is a single digit at the end of each unique identifier.
#       By splitting that digit out,
#       I can compare to see if the digits from each list matches in the 'for' loop,
#       then if the digits match, we can compare the remaining characters of the unique identifiers.
#       This should improve computational speed for huge data
#       because instead of comparing 'rp1' vs 'st7' for each loop
#       we can simply compare '1' vs '7' and proceed further is they match.

#       SOLUTION

# First, read from .txt then append to list_1 and list_2
# After reading, resulting list is for example
# ['rp1 Mary Smith\n', 'st7 John Doe\n', 'uk9 Alex Johnson']

# I then strip each index by ' ' once.
# Resulting list is thus
# [['rp1', 'Mary Smith'], ['st7', 'John Doe'], ['uk9', 'Alex Johnson']]

with open('.\c3_Data_List\c3_File_1.txt', 'r') as f:
    list_1 = f.readlines()
    f.close()
list_1 = [i.strip('\n').split(' ', 1) for i in list_1]

with open('.\c3_Data_List\c3_File_2.txt', 'r') as f:
    list_2 = f.readlines()
    f.close()
list_2 = [i.strip('\n').split(' ', 1) for i in list_2]

# Check to make sure lists are appended correctly
# Note there are multiple lists contained within list_1 and list_2.

print('File 1:', list_1)
print('File 2:', list_2)

# Initialize list_3 to store results

list_3 = []

# Note that list_1[n][0] and list_2[n][0] always contain the unique identifiers for all n where n = len(list_1) - 1.
# This enables me to easily compare the unique identifier found in the index of each list.
# If they match, append the whole package to list_3.

for i1 in list_1:
    for i2 in list_2:
        if i1[0] == i2[0]:
            list_3.append([i1[0], i1[1], i2[1]])

# Join the index of list_3 by ' ' then print results

list_3 = [' '.join(i) for i in list_3]

print('\nResults:\n %s' % list_3)

# REFERENCES
#https://stackoverflow.com/questions/3142054/python-add-items-from-txt-list-into-a-list
