import random

def generator():
    baseSentences = []
    buzzwords = []
    names = []
    products = []
    languages = []
    
    try:
        #Import Positive Base Sentences into a list
        textFileRead = open('src/text/BaseSentences.txt', 'r')
        baseSentences = textFileRead.read().split('|')
        
        textFileRead.close()

        #Import Buzzwords into a list
        textFileRead = open('src/text/Buzzwords.txt','r')
        buzzwords = textFileRead.read().split('|')
        
        textFileRead.close()
        
        #Import Names into a list
        textFileRead = open('src/text/Names.txt','r')
        names = textFileRead.read().split('|')
        
        textFileRead.close()
        
        #Import Products into a list
        textFileRead = open('src/text/Products.txt','r')
        products = textFileRead.read().split('|')
        
        textFileRead.close()
        
        #Import Descriptions into a list
        textFileRead = open('src/text/languages.txt','r')
        languages = textFileRead.read().split('|')
        
        textFileRead.close()
        
    except IOError:
        print("Missing the file: " , "File Name")
    
    #Pick a random base sentence
    sentence = baseSentences[random.randint(0, len(baseSentences)-1)]
    
    if sentence.count("<Name>"):
        for x in range(sentence.count("<Name>")):
            sentence = sentence.replace('<Name>',names[random.randint(0, len(names)-1)], 1)
    if sentence.count("<Buzzword>"):
        for x in range(sentence.count("<Buzzword>")):
            sentence = sentence.replace('<Buzzword>',buzzwords[random.randint(0, len(buzzwords)-1)], 1)

    if sentence.count("<Product>"):
        for x in range(sentence.count("<Product>")):
            sentence = sentence.replace('<Product>',products[random.randint(0, len(products)-1)], 1)
        
    if sentence.count("<Language>"):
        for x in range(sentence.count("<Language>")):
            sentence = sentence.replace('<Language>',languages[random.randint(0, len(languages)-1)], 1)
    sentence = sentence.replace('\n', '').replace('\r', '').replace('  ',' ')
    return sentence

