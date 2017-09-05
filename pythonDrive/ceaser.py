import defins
import config
import sys
##import hashlib

#argv= ["python", "username", "password"]
argv = sys.argv[:]

def xor(a, b):
    return not a == b

def bitXor(a, b):
    return a ^ b

def byes(by, i=0):
    global config
    i+= 1;
    by = defins.crypto.sha512(by)
    if i == config.encryptionRounds: return by
    else: return byes(i, target, i=i)

def quick(a): return int(a.hex(), base=16);

##Opens the required files.

def ceaser(hexhash, file, output=None, ret=True):
    pas = hexhash
    del hexhash
    
    #File to read is the file to which the algo is applied to
    f1 = open (file, "rb" );

    #File to write is the file where the data is going to be wrote to
    if output:
        f2 = open (output, "wb" );
    else:
        f2 = None

    pos = 0; #Position on the SHA512 in relation to the location of the file the algo is reading.
    paslen = len(pas) #Lengh of crypto hash.

    bs=b""
    vchange = -1 #future feature
    
    while True:
        x = f1.read(1);         #Read a byte (2 hex chars)
        if x == b"": break;     #This checks for EOF

        work = hex ( quick(x) ^ quick(pas[pos:(pos)+1])) [2:]; #Applies Xor for the byte.
        if len(work) == 1: work = "0" + work; #makes sure it passes down 2 byes down to bytes.fromhex()

        if output: f2.write(bytes.fromhex(work));       ##Writes to file from the hex values.
        if ret: bs+= bytes.fromhex(work);               ##Writes to memory bytecodes
        
        pos+= 1;
        if pos == paslen or pos == vchange:
            pos = 0;
            #hash should change here to disallow cryptanalisis
            
    if output:
        f2.close();
        
    f1.close(); ##Neatly closes file :)
    
    del f1, f2
    if ret: return bs;
    
