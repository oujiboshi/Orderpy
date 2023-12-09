import core

db_admin = 'database/admin.csv'
db_user = 'database/user.csv'

def authentication(role,username,password,switch=False):
    data = core.encryption_db(role,decrypt=True)
    for array in data[1:]:
        roles,usrname,passwd = array[0],array[1],array[2]
        if usrname == username and passwd == password:
            switch = True
            global account_access
            account_access = array
    return switch

def account_logged():
    try:
        return account_access[:2]
    except NameError:
        return None

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
            input()
            return 0
        else:
            print("Login Gagal")
            attempts -= 1
            input()
            core.clear()

    print("<Attempts Out>")
    exit()

def account_requirement(database,username,usr_req=True):
    data = core.encryption_db(database,decrypt=True)

    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = alphabet_lower.upper()
    number = '1234567890'
    symbol = '!@#$?'

    # < USERNAME REQUIREMENTS >
    # Check duplicate
    for check in data[1:]:
        usrname = check[1]
        if usrname == username.strip():
            usr_req = False
    # Check length
    if len(username) not in range(3,21):
        usr_req = False
    # Check symbol
    for char in username:
        if char not in alphabet_lower + alphabet_upper + number:
            usr_req = False
    # Check first number on username
    if username[0].isdigit() == True:
        usr_req = False
    
    # < PASSWORD REQUIREMENTS >


    return usr_req

def register_session():
    username = input("Username: ").strip()
    tes = account_requirement(db_user,username)
    print(tes)
    exit()

def main_gate():
    core.clear()
    match input("[1]Login [2]Register\n> "):
        case '1':
            core.clear()
            login_session()
        case '2':
            core.clear()
            register_session()

if __name__ == '__main__':
    main_gate()