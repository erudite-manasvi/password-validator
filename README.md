# Password Validator

This repository contains the source code of password validator based on python language

# Python installation guide
[Visit](https://www.python.org/downloads) and install stable version of python3 to run this code.

# After Installation Run:-

- Check whether required version is installed 
```bash
python3 --version
```

- Clone this repo
```bash
git clone https://github.com/erudite-manasvi/password-validator.git
```

- cd into password-validator
```bash
python3 main.py
```

# Password Acceptance Criteria
1: PASSWORD LENGTH SHOULD BE OF MINIMUM 12 CHARACTER

2: PASSWORD LENGTH SHOULD NOT BE GREATER THAN 20 CHARACTER

3: PASSWORD MUST CONSIST OF UPPER-CASE CHARACTER [A-Z] 

4: PASSWORD MUST CONSIST OF LOWER-CASE CHARACTER [a-z]

5: PASSWORD MUST CONSIST OF NUMBER [0-9] 

6: PASSWORD MUST CONSIST OF SPECIALCHARACTER - !, @, #, $, %, ^, &, *, (, ), _, -, ~ 

7: PASSWORD SHOULD START WITH EITHER ANY SPECIALCHARACTER OR WITH 2 DIGIT'S NUMBER

8: PASSWORD SHOULD CONTAIN ATLEAST3 UPPER-CASE CHARACTER AND 3 LOWER-CASE CHARACTER

9: PASSWORD SHOULD CONTAIN ATLEAST3 SPECIAL CHARACTER

10: PASSWORD SHOULD NOT CONTAIN 5 SAMECHARACTER\ OR NUMBER CONSECUTIVELY 

11: PASSWORD SHOULD NOT HAVE USERNAMEINTO IT AT ANY POSITION

12: PASSWORD SHOULD NOT CONTAIN 3 SAME SPECIAL CHARACTER'S CONSECUTIVELY

# main.py
- ## main()
     Execution of the whole program start from main function.

     ```python
     username = get_username()
     ```
     get_username() is called and it'll retriev and store the value in username.

     ```python
     while c>0:
        password = get_password()
        password =  password.strip()

        if is_valid_password(password,username):
            print('Password is valid')
            break
        else:
            c-=1
            print(f'Password is not valid. {c} attempts left')
     ```
     As far as count c is not zero this while loop will run & takes password from user, is_valid_password(password,username) run and return true if password is valid else return false.

- ## helper function
  helper is function that takes warning as an argument and returns [decorator](https://www.geeksforgeeks.org/decorators-in-python/).
  when Python encounters the @helper('Password length must be between 12 to 20') line, it translates this into:
  ```python
  within_range = helper('Password length must be between 12 to 20')(within_range)
  ```
  This means that helper is called with the argument 'Password length must be between 12 to 20', and the result of that call (which is the decorator function) is used to wrap within_range.
  - The decorator function takes within_range as its func argument.
  - Inside decorator, the wrapper function is defined, which is designed to replace the original within_range.
  - The wrapper function is returned, effectively replacing within_range with the wrapper function.
 
  Example:-
  ```python
  within_range('mypassword123')
  ```

  Function calls will be:-
  ```python
  within_range('mypassword123')
    -> wrapper('mypassword123')         # wrapper replaces within_range due to decorator
        -> within_range('mypassword123') # original within_range is called
            -> returns True or False    # based on password length check
        -> if True: return True
        -> if False: print 'Password length must be between 12 to 20'
                    return False
   ```

- ## within_range(password)
     This function take password as an argument and check whether it's length is between 12 to 20.
  
- ## contains_uppercase(password) and contains_lowercase(password)
     This function make sure that password contains atleast three upper case and three lower case characters.

- ## contains_digit(password)
     This function contains a check that password must contain a numeric value.

- ## contains_specialchar(password)
     This function check that password contains atleast 3 special characters
          special_chars = ['!','@','#','$','%','^','&','*','(',')','_','-','~']

- ## valid_specialchar(password)
     valid_specialchar(password) make sure that password must not contain three same special characters

- ## start_with(password)
     start_with(password) ensure either password starts with 2 digit or special character

- ## valid_characters_numbers(password)
     This function return false if password consists 5 same characters or numbers else it'll return true.

- ## not_a_username(password,username)
     This function check password against username, Password must not contains username at all.

- ## is_valid_password(password,username)
     This function is responsible for executing all the above defined functions


# common_passwords.py
  This file contains a list of commonly used passwords.
     
