import nltk
import re
with open('News-articles-kaggle.txt') as f:
    dataSet = f.read()
class Word:
    def __init__(self, word, noOfRepetitions):
        self.word = word
        self.noOfRepetitions = noOfRepetitions


def unique(list):
    unique_list = []
    for x in list:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


def arrange(list):
    return sorted(list, key=lambda x: x.noOfRepetitions, reverse=True)


def count(triple, uniqueWords):
    counter = 0
    for i in range(0, len(uniqueWords)):
        g = i + 1
        k = i + 2
        if uniqueWords[i].lower() == triple[0].lower() and uniqueWords[g].lower() == triple[1].lower() and uniqueWords[
            k].lower() == triple[2].lower():
            counter = counter + 1
    return counter


def listToString(triple):
    str = ""
    for word in triple:
        str += word + " "
    return str


def trigram(userSearchInput, dataSet):
    wordTokens = re.findall("\w+", dataSet)
    uniqueWords = unique(wordTokens)
    inputTokensTemp = []
    userSearchInput = re.findall("\w+", userSearchInput)
    if len(userSearchInput) > 1:
        triplesList = []
        suggestionList = []
        for word in uniqueWords:
            triple = userSearchInput.copy()
            triple.append(word)
            triplesList.append(triple)
        for triple in triplesList:
            noOfRepetitions = count(triple, uniqueWords)
            word = Word(listToString(triple), noOfRepetitions)
            suggestionList.append(word)
            list_ = arrange(suggestionList)
        return list_[0:4]
    elif (len(userSearchInput)) == 1:
        biSsentenceTokens = re.findall("\w+\s\w+", dataSet)
        uniqueBiSsentence = unique(biSsentenceTokens)
        suggestionList = []
        for biSentence in uniqueBiSsentence:
            biSentenceTokens = nltk.word_tokenize(biSentence)
            if biSentenceTokens[0] == userSearchInput[0]:
                word = Word(listToString(biSentenceTokens), biSsentenceTokens.count(biSentence))
                suggestionList.append(word)
        list_ = arrange(suggestionList)
        return list_[0:5]


def getSuggestions(userSearchInput, dataSet):
    suggestionList = trigram(userSearchInput, dataSet)
    suggestion = ''
    for word in suggestionList:
        print(word.noOfRepetitions)
        suggestion += word.word + '\n'
    return suggestion


