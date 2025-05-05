
user = input("Enter text to write to the file:\t")
print("Data Successfully written to output.txt.")

file1 = open('Output.txt', 'a')
appending_file = file1.write(user + '\n')
file1.close()


user2 = input("Enter additional text to append:\t")
print('Data successfully appended.')

file1 = open('Output.txt', 'a')
appending_file2 = file1.write(user2 + '\n')
file1.close()


print("Final content of 'Output.txt':\n")

file1 = open('Output.txt', 'r')
reading_file = file1.read()
print(reading_file)
file1.close()
