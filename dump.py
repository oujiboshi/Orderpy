import core

file_user = 'database/user.csv'
file_admin = 'database/admin.csv'

role = input("Role: ")
username = input("Username: ")
password = input("Password: ")

data = [role,username,password]
core.append_db(file_admin,data,encrypt=True)
watch = core.encryption_db(file_admin,decrypt=True)
print(watch)
# watch = core.encryption_db(file_admin,decrypt=False)
# print(watch)