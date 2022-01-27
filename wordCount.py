# Maria Corona
# SID 80560734
# Project 0

import re

def main():
    txt = readFile() #reads file and returns plaing text

    new_text = specialCharacters(txt) #new text with no special characters

    myList = whiteSpace(new_text) #list of words separated by whitespace

    myDictionary = wordCount(myList) #dictionary with counts using keys and values

    writeFile(myDictionary) #writes file

def readFile():
    f = open("declaration.txt", "r")
    txt = f.read()
    return txt


def whiteSpace(myText):
    x = re.split("\s", myText)
    return x


def specialCharacters(myTxt): #removes special characters
    #some are replaced with blank, some are replaced with empty
    x = re.sub(",", " ", myTxt)
    x = re.sub("-", " ", x)
    x = re.sub(";", "", x)
    x = re.sub(":", "", x)
    x = re.sub("\.", "", x)
    x = re.sub("\"", "", x)
    x = re.sub("'", " ", x)

    return x


def wordCount(myList):
    myDictionary = {}

    for theWord in myList:
        word = theWord.lower() #to lowercase
        if word != "":
            if word in myDictionary: #if the word is in the dictionary
                myDictionary[word] += 1 #increase count
            else:
                myDictionary[word] = 1 #if not set to 1

    # print(myDictionary) #testing code
    return myDictionary #returns dictionary

def writeFile(myDictionary):
    myText = ""
    myconcatenated = ""
    f = open("myfile.txt", "w") #if file exists, overwrites

    for key, value in sorted(myDictionary.items()): #this sorts the dictionary alphabetiacally using the key (word)
        myText = str(key) + " " + str(value) + "\n"; #takes key = word and value = count and formats
        myconcatenated = myconcatenated + myText #Concatenates

    f.write(myconcatenated) #writes file
    f.close()#closes

if __name__ == "__main__":
    main()

