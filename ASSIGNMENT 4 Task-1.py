try:
    File1 = open('Sample.txt', 'r')
    print("Reading File Content:\n")

    reading_file = File1.readline()
    print('Line1:\t', reading_file.strip())

    reading_file1 = File1.readline()
    print('Line2:\t', reading_file1.strip())

    File1.close()
except FileNotFoundError:
    print("Error: File 'sample.txt' not found.")