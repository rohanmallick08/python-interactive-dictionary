import json
# for sequence matche we can use difflib library (https://docs.python.org/2/library/difflib.html) difflib.get_close_matches(word, possibilities[, n][, cutoff])
import difflib
from difflib import get_close_matches

# Load Data Josn
def loadDictionaryJson():
    return json.load(open("data.json"))
# Function to get input from user and return it.
def getQueryWord():
    q = input("Enter the word : ")
    return q
# Search the word in data.json
def getMeaning(q, dictionary):
    # Check if queried keyword is available in data.json
    if q.lower() in  dictionary:
        meaningList = dictionary[q.lower()]
        return meaningList
    else :
        return []

# Find Simimar matches
def findSimilarWord(q,dictionary):
    similarWord = get_close_matches(q, dictionary.keys())
    return similarWord
# Display Result
def displayResult(query,meanings, dictionary):
    if not meanings:
        # Check For Similar word. This will return list of similar word
        similarWord = findSimilarWord(query, dictionary)
        if not similarWord:
            print("No Word Found. Please try with other word!")
        else:
            getFirstSuggestedWord = similarWord[0]
            # Call getMeaning() to get the word meaning with getFirstSuggestedWord
            meanings = getMeaning(getFirstSuggestedWord, dictionary)
            print("Did you mean : {0}".format(getFirstSuggestedWord))
            for meaning in meanings:
                print(meaning)
    else:
        for meaning in meanings:
            print(meaning)

# Get the word from user
query = getQueryWord();
# Load the dictionary
dictionary = loadDictionaryJson()
# Get the meanings
meanings = getMeaning(query, dictionary)
# Display Result
displayResult(query,meanings, dictionary)
