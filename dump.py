import core

# db = core.read_csv('database/user.csv')
# encrypt = core.encryption('database/user.csv',shift=0)
# decrypt = core.decryption('database/user.csv',shift=0)
# print(encrypt)
# print(decrypt)

# data = ['user','aku','boshi']
# encrypt = core.encryption(data)
# print(encrypt)
# decrypt = core.decryption(encrypt)
# print(decrypt)

file = 'database/user.csv'

role = input("Role: ")
username = input("Username: ")
password = input("Password:")

data = [role,username,password]
secure = core.encryption(data)
print(secure)
original = core.decryption(secure)
print(original)
# decrypt = core.decryption_db(file)
# print(decrypt)
