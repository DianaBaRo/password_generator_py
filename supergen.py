#import bcrypt
#import time
import hashlib
from urllib.parse import urlparse
import re

def generate(master, url, length=10, algorithm='md5'):

    #.encode to prevent typeError : Unicode-objects must be encoded before hashing
    password = (master + ":" + url).encode('utf-8')

    #salt = bcrypt.gensalt(rounds=16)
    #hashed = bcrypt.hashpw(password, salt)

    count = 0
    
    hashed = hashlib.md5(password).hexdigest()

    return hashed[:length]
    

def password_check(password):
    reg = """^[a-z]                          # start with lowercase
                   [a-zA-Z0-9]*                    # stuff
                   (?:(?:[A-Z][a-zA-Z0-9]*[0-9])|  # uppercase stuff number OR
                   (?:[0-9][a-zA-Z0-9]*[A-Z]))     # number stuff uppercase
                   [a-zA-Z0-9]*$"""

    #compiling regex
    pat = re.compile(reg)

    #searching regex
    mat = re.search(pat, password)

    #validating conditions
    if mat:
        True
        print("Password OK")
    else:
        False
        print("Password not OK")

generate("ola", "kease", 10)
password_check("aywFd0bmnJ")