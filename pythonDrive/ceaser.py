import defins
import config

def xor(a, b):
    return not a == b

def bitXor(a, b):
    return a ^ b

def byes(by, target, i=0):
    i = i+1;
    by = defins.crypto.sha512(by)
    if i == target: return by
    else: return byes(i, target, i=i)

def lcsGen(string):
    pass

import hashlib;

##Debug functions I used during development.
def xor(a, b): return not a == b;
def quick(a): return int (a.hex(), base= 16);

##Type in the password you want to encrypt or decrypt the file with. In this case, this is the key.
pas = hashlib.sha512(input("password to encrypt/decrypt files with> ").encode("UTF8")).digest();

##Opens the required files.
#File to read is the file to which the algo is applied to
f1 = open (input("file to read> "), "rb" );

#File to write is the file where the data is going to be wrote to
f2 = open (input("file to write> "), "wb" );

#Position on the SHA512 in relation to the location of the file the algo is reading.
pos = 0;
while True:
    x = f1.read(1);         #Read a byte ( 2 hex chars )
    if x == b"": break;     #This checks for EOF
    work = hex ( int ( x.hex(), base=16 ) ^ int ( pas[pos:(pos)+1].hex(), base=16 ) )[2:]; #Applies Xor for the byte.
    if len(work) == 1:
        #Sometimes, the Xor return lengh is < 1 which causes problems for bytes.fromhex() function,
        #an extra 0 has to be added at the start for consistency.
        work = "0" + work;
    f2.write(bytes.fromhex ( work ) );  ##Writes to file from the hex values.
    pos+= 1;
    if pos == 64: pos = 0;              ##The key's bit length is 512, so 512 / 8 = 64 bytes.
                                        #Cannot go over 64 as it would cause an out of index or range error.

f2.close();
f1.close(); ##Neatly closes file :)
