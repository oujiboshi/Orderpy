import core

db_admin = 'database/admin.csv'
db_user = 'database/user.csv'

def authentication(role,username,password,switch=False):
    data = core.encryption_db(role,decrypt=True)
    for array in data[1:]:
        roles,usrname,passwd = array[0],array[1],array[2]
        if usrname == username and passwd == password:
            switch = True
            global access
            access = array
    return switch

def login_session(role=db_user):
    attempts = 3
    while attempts > 0:
        username = input('Username: ')
        if username == '/admin':
            core.clear()
            print("<Administrator>")
            login_session(role=db_admin)
            return 0
        elif username == '/user':
            core.clear()
            login_session()
            return 0
        password = input('Password: ')
        verify = authentication(role,username,password)
        if verify == True:
            print("Login Berhasil")
            print(access)
            input()
            return 0
        else:
            print("Login Gagal")
            attempts -= 1
            input()
            core.clear()

    print("<Attempts Out>")
    exit()

def register_session():
    pass

def main_gate():
    core.clear()
    match input("[1]Login [2]Register\n> "):
        case '1':
            core.clear()
            login_session()
        case '2':
            register_session()

if __name__ == '__main__':
    main_gate()