import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890?#!$%@^&*+-_=;:\'",./<>'
num_of_passwords = int(input('How many passwords to generate? '))
length = int(input('Password length? '))

for i in range(num_of_passwords):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    print(password)