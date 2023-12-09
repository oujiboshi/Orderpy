import csv
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def dd(x):
    print(x)
    exit()
    
def read_db(database):
    data = []
    with open(database,mode='r') as file:
        reader = csv.reader(file)
        for array in reader:
            data.append(array)
    return data

def write_db(database,data,encrypt=False):
    with open(database,mode='w',newline='') as file:
        writer = csv.writer(file)
        if encrypt == True:
            data = encryption(data)
        writer.writerow(data)

def append_db(database,data,encrypt=False):
    with open(database,mode='a',newline='') as file:
        writer = csv.writer(file)
        if encrypt == True:
            data = encryption(data)
        writer.writerow(data)

def encryption(data,shift=16,decrypt=False):
    mod_data = []
    if decrypt == True:
        shift = -shift
    for array in data:
        mod = ""
        for char in array:
            shifting = chr(ord(char) + shift)
            mod += shifting
        mod_data.append(mod)
    return mod_data

def encryption_db(database,shift=16,decrypt=False):
    data = read_db(database)
    mod_data = []
    for array in data:
        mod = encryption(array,shift)
        if decrypt == True:
            mod = encryption(array,shift,decrypt=True)
        mod_data.append(mod)
    return mod_data
