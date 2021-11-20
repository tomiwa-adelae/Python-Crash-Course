# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people  = ['John', 'Brad', 'Sara', 'Susan']

# # Simple for loop
# for person in people :
#     print(f'Current person: {person}')

# break
# for person in people :
#     if person == 'Sara':
#         break
#     print(f'Current person: {person}')


# # continue
# for person in people :
#     if person == 'Sara':
#         continue
#     print(f'Current person: {person}')

# Range
# for i in range(len(people)):
#     print(people[i])

# # Custom Range
# for i in range(0, 11):
#     print(i)


# While loops execute a set of statements as long as a condition is true.

count = 0 
while count <= 10:
    print(f'Count: {count}')
    count += 1