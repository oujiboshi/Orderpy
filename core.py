import csv
import os

def read_db(database):
    data = []
    with open(database,mode='r') as file:
        reader = csv.reader(file)
        for array in reader:
            data.append(array)
    return data

def write_db(database,data):
    with open(database,mode='w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def append_db(database,data):
    with open(database,mode='a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def clear():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def encryption(data,shift=16):
    encrypt_data = []
    for array in data:
        encrypt = ""
        for char in array:
            code = chr(ord(char) + shift)
            encrypt += code
        encrypt_data.append(encrypt)
    return encrypt_data

def decryption(data,shift=-16):
    return encryption(data,shift)

def decryption_db(database,shift=-16):
    data = read_db(database)
    data_decrypt = []
    i = 0
    for array in data:
        decrypt = encryption(array,shift)
        data_decrypt.append(decrypt)
    return data_decrypt

def dd(x):
    print(x)
    exit()