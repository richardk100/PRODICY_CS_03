# Password strength Checker Progran

import re 

#Password must be at least 8 characters
password = input('Enter Password:')

if len(password) < 8:
    print('Password must be atleast 8 characters long')

#Password must at least contain one uppercase letter
elif not re.search('[A-Z]', password):
    print('Password must contain at least one uppercase letter')

#Password must at least contain one lowercase letter

elif not re.search('[a-z]', password):
    print('Password must contain at least one lowercase letter')

#Password must at contain at least one number
elif not re.search('[0-9]', password):
    print('Password must contain at least one number')


#Password must contain at least one special character
elif not re.search('[!-()]', password):
    print('Password must contain at least one special character')


else:
    print('Password is strong')