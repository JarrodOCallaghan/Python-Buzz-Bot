import sys
sys.path.append("src/")
import Generator
import pyttsx3
engine = pyttsx3.init()
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+10)

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-8)



while True:
    userInput = input("Type new, multi or exit: ")
    if userInput.lower() == "e" or userInput.lower() == "exit":
        break
    elif userInput.lower() == "new" or userInput == "n":

        sentence = Generator.generator()
        print(sentence, "\n")
        engine.say(sentence)
        engine.runAndWait()
        
        
