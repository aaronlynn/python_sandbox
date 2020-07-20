# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)

# Get value
print(fruits[1])

# Can't change value (following line throws TypeError)
#fruits[0] = 'Pears'

# Delete tupe
del fruits2

# Get length
print(len(fruits))

###########################################################################################################

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mangos'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grapes')

# Remove from set
fruits_set.remove('Grapes')

# Add duplicate
fruits_set.add('Apples')

# Clear set
# fruits_set.clear()

# Delete set
# del fruits_set

print(fruits_set)