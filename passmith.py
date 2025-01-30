import os
import re
import itertools

def openDict(path):
    """Open the dictionary and return the file object to the main."""
    try:
        with open(path, "r") as file_ob:  # Ensuring file closes automatically
            print("Dictionary opened successfully.")
            return file_ob
    except IOError:
        print("Dictionary not found at the given path.")
        return False

def fixString(string):
    """Removes unwanted characters from the string."""
    return string.replace("/", "").replace("-", "").replace(".", "")

def dictToFile(dictionary, name):
    """Save dictionary into an external file."""
    with open(name, "w") as dFile:
        for word in dictionary:
            dFile.write(word + '\n')
    return name

def addSpice(dictionary,extensions):
    """Add externsions to the start and end of each password."""
    new_words = set()
    
    for word in dictionary:
        for ext in extensions:
            new_words.add(word + ext)
            new_words.add(ext + word)

    dictionary.update(new_words)  # Add new generated words

def createDict(data):
    """Generate permutations and combinations of provided data."""
    myDict = set()  # Use set to avoid duplicates
    max_complexity = 3

    # Generate permutations for 1 field and up to max_complexity fields
    for r in range(1, max_complexity + 1):
        for combination in itertools.combinations(data, r):
            for perm in itertools.permutations(combination):
                word = ''.join(perm)
                myDict.add(word)
                myDict.add(word.lower())
                myDict.add(word.upper())
                myDict.add(word.title())

    return myDict

def main():
    print("[+] Welcome to Dictionary Maker Tool")
    print("[+] Insert information in lowercase (we'll handle the rest)")
    print("[+] If any information is unknown, just press ENTER)\n")

    info = []

    a = input(">First Name: ")
    file_name = fixString(a) + "_words_list.txt"
    info.append(fixString(a))

    a = input(">Last Name: ")
    info.append(fixString(a))

    a = input(">Nickname: ")
    info.append(fixString(a))

    a = input(">Phone number (example: 0501234567): ")
    info.append(fixString(a))

    a = input(">Birthdate (Format: DD/MM/YYYY): ")
    info.append(fixString(a))
    info.append(fixString(a)[:4])  # Extract date without year
    info.append(fixString(a)[-4:])  # Extract year

    while True:
        a = input(">More known information (Pet name, partner name, etc. Leave blank to finish): ")
        if a == '':
            break
        info.append(fixString(a))

    dictionary = createDict(info)  # Create dictionary from information
    
    extensions = ["1", "123", "321", "!", "?"] # Add other prefixes and postfixes here
    
    addSpice(dictionary,extensions)  # Add prefixes and postfixes using extensions list 
    dictToFile(dictionary, file_name)  # Save to file

    print(f"Dictionary file '{file_name}' is ready.")

if __name__ == "__main__":
    main()
