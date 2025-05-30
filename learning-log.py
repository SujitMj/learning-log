'''
#Greet a Person (Beginner)

def greet(name,/):
    print("Hello, {}!".format(name))
    print("Hello, ", name+"!")
    print("Hello, "+name+"!")


greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!

#Find the Maximum of Three Numbers (Intermediate)

def find_max(numbers):
    temp = 0
    for num in numbers:
        if num > temp:
            temp = num
        else:
            continue
    print(f"Max number is {temp}")
    

numbers = []
limit = int(input("Enter Limit: "))

for x in range(limit):
    num = int(input("Enter number: "))
    numbers.append(num)

find_max(numbers)
'''

#Count Vowels in a String (Intermediate)

def count_vowels(text):
    vowels = 0
    for alphabets in text: 
        if alphabets == 'a' or alphabets == 'A' or alphabets == "E" or alphabets == "e" or alphabets == 'I' or alphabets == 'i' or alphabets == 'O' or alphabets == 'o' or alphabets == 'U' or alphabets == 'u':
            vowels += 1
        else:
            continue
    
    print(vowels)

text = input("Enter text: ")

count_vowels(text)




