#import bcrypt
#import time
import hashlib
#from urllib.parse import urlparse
import re
import base64

_valid_pass = \
    re.compile(r"""^[a-z]                          # start with lowercase
                   [a-zA-Z0-9]*                    # contains lower and upper case and numbers
                   (?:(?:[A-Z][a-zA-Z0-9]*[0-9])|  # uppercase lowercae number OR
                   (?:[0-9][a-zA-Z0-9]*[A-Z]))     # number lowercase uppercase
                   [a-zA-Z0-9]*$""",               # check for lower and upper case or numbers at the end
               re.VERBOSE)

def generate(master, domain, length=10, algorithm='md5'):

    password = master + ":" + domain
    count = 0
    while count < 10 or not _valid_pass.match(password[:length]):
        password = hashlib.new(algorithm, password.encode('utf-8')).digest()
        password = base64.b64encode(password, b'98').decode('ascii')
        password = password.replace('=', 'A')
        count += 1
    
    return password[:length]

generate("ola", "kease", 10)