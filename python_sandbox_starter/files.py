# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')

# Get info
print('Name:\t\t', myFile.name)
print('Is closed:\t', myFile.closed)
print('Mode:\t\t', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')    # Must be set to 'a' for append, otherwise will write over existing file
myFile.write(' I also like PHP')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)