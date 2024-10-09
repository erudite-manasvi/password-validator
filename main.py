from common_passwords import password_list

def helper(warning):
    def decorator(func):
        def wrapper(*args):
            if func(*args): return True
            else:
                print(warning)
                return False
        return wrapper
    return decorator


@helper('Password length must be between 12 to 20')
def within_range(password):
    res = password.strip() # strip remove -> characters from left or right side, if no argument is paased - by default remove whitespace(if present), and returns new string
    return len(res)>=12 and len(res)<=20

@helper('Password include atleast 3 uppercase character')
def contains_uppercase(password):
    c=0
    for ch in password:
        if ch.isupper():c+=1
    
    return c>=3

@helper('Password include atleast 3 lowercase character')
def contains_lowercase(password):
    c=0
    for ch in password:
        if ch.islower():c+=1
    
    return c>=3

@helper('Password must contain numeric value')
def contains_digit(password):
    for ch in password:
        if ch.isdigit():return True

    return False

special_chars = ['!','@','#','$','%','^','&','*','(',')','_','-','~']
@helper('Password include atleast 3 special characters ')
def contains_specialchar(password):
    c = 0

    for ch in password:
        if ch in special_chars:
            c+=1
            if c>=3: return True

    return c>=3

@helper("Password can't have 3 special characters consecutively")
def valid_specialchar(password):
    c=0
    for i in range(len(password)-1):
        if password[i] in special_chars and password[i+1] in special_chars:
            c+=1
            if c>=2:return False
        else:
            c=0
        
    return True

@helper('Password either start with 2 digit or special character')
def start_with(password):
    if password[0] in special_chars: return True
    elif password[0].isdigit() and password[1].isdigit(): return True
    return False

@helper('Password cannot have 5 same characters and numbers consecutively')
def valid_characters_numbers(password):
    char=0
    num=0
    for i in range(len(password)-1):
        if password[i].isalpha() and password[i].lower()==password[i+1].lower():
            char+=1
            if char>=5:return False
        elif password[i].isdigit() and password[i]==password[i+1]:
            num+=1
            if num>=5:return False
        else:
            char=0
            num=0

    return True

@helper("Password can't consist UserName at all")
def not_a_username(password):
    username = get_username()
    u1 =  username.split()
    p1 = ''.join(password.split()).lower()

    for u in u1:
        if u.lower() in p1: return False

    return True

def is_valid_password(password):
    return within_range(password) and contains_uppercase(password) and contains_lowercase(password) and contains_digit(password) and contains_specialchar(password) and valid_specialchar(password) and start_with(password) and valid_characters_numbers(password) and not_a_username(password) and password not in password_list



def get_username():
    return input('Enter Username:-')

def get_password():
    return input('Enter Password:-')

def main():
    c = 3
    while c>0:
        password = get_password()
        print(len(password))

        if is_valid_password(password):
            print('Password is valid')
            break
        else:
            c-=1
            print(f'Password is not valid. {c} attempts left')

if __name__ == '__main__':
    main()