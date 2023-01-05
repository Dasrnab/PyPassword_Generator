#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
#choosing random leter/numbers/ symbol from the lists:

for char in range(0, nr_letters):
  random_char = random.choice(letters)
  password += random_char
#print(password)

for sym in range(0,nr_symbols +1):
  random_sym = random.choice(symbols)
  password += random_sym
#print(password)

for num in range(0, nr_numbers + 1):
  random_num = random.choice(numbers)
  password += random_num
  
#print(password)
  
#shuffling the list:
random.shuffle(password)
#print(password)
#converting the list into a string:
password_string = ''
for i in password:
  password_string +=i
print(password_string)