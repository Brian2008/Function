def words():
    fileName=input("Enter The File Name ->")

    numberOfWords=0
    file=open(fileName,"r")
    for line in file:
        print(line)
        strings=line.split()
        print(strings)
        numberOfWords=numberOfWords+len(strings)
    print("number of words are ")
    print(numberOfWords)
words()
    