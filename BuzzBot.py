import sys
sys.path.append("src/")
import Generator

while True:
    userInput = input("Type new, multi or exit: ")
    if userInput.lower() == "e" or userInput.lower() == "exit":
        break
    elif userInput.lower() == "new" or userInput == "n":
        print(Generator.generator(), "\n")
    elif userInput.lower() == "multi" or userInput == "m":
        quantityInput = int(input("Enter number or generated sentences: "))
        for quantity in range(quantityInput):
            print(Generator.generator())
        print("\n")
        
