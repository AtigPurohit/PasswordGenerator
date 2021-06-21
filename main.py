import random
import array

length = 12

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

combined = digits + lowercase + uppercase + symbols

rand_dig = random.choice(digits)
rand_lw  = random.choice(lowercase)
rand_up = random.choice(uppercase)
rand_symb = random.choice(symbols)

temp = rand_up+rand_lw+rand_symb+rand_dig

for x in range(length - 4):
    temp = temp + random.choice(combined)

temp_pass = array.array('u', temp)
random.shuffle(temp_pass)

password = ""
for x in temp_pass:
        password = password + x

print(password)