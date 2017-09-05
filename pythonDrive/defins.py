import os
import config
import string
import random
import hashlib

def changeUP(filepath, to):
    if config.os().lower() == "windows": ch = "\\"
    else: ch = "/"
    pf = os.path.dirname(filepath) + ch
    for x in to:
        pf = pf + x + ch
    os.chdir(pf)

def fileSize(fileobject):
    fileobject.seek(0,2) # move the cursor to the end of the file
    size = fileobject.tell()
    return size

class crypto:    
    def Salt(N):
        return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(N))

    def sha512(string):
        return hashlib.sha512(str(string).encode(config.encoding)).hexdigest()

    def sha256(string):
        return hashlib.sha256(str(string).encode(config.encoding)).hexdigest()
