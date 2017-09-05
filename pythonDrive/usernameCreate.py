import sys
import os
import config
import defins    

"""
Files + Dirs to create:
[x] $username/
[x] $username/sha512.csv        -Sha512 digest of the password + hash
[x] $username/sha256.csv        -Sha256 digest of the password + hash
[x] $username/config.txt        -Config file
[x] $username/block.txt         -Block list
[x] $username/messages.enc      -Encrypted messages file
[x] $username/token.cookie      -Login token for auth

Hash CSV files:
$salt,$hexdigest,$peper

Notes:
Hash CSV files are not RFC 4180 compliant, however they are simply
containers for hashes and salts with only one record.
Non-hash CSV files are RFC 4180 compliant. 
"""

Fcreate = ["sha512.csv", "sha256.csv", "config.txt", "block.txt",
           "messages.enc", "token.cookie"]

##sys.argv = ["python", $username, $password, [optional]]
sys.argv = ["python", "username", "password"]
argv = sys.argv[:]
username = argv[1]
password = argv[2]

defins.changeUP(__file__, ["db"])

if not os.path.exists(username):
    os.makedirs(username)
    defins.changeUP(__file__, ["db", username])#
    
    for x in Fcreate:
        f = open ( x, "wb" );
        f.write("None".encode())
        f.close();
    del x

    salt = defins.crypto.Salt(config.saltLengh)
    pper = defins.crypto.Salt(config.pepperLengh)
    
    hsh = defins.crypto.sha512(salt+password+pper)
    f = open ( "sha512.csv", "wb" )
    f.write(str(salt+","+hsh+","+pper).encode(config.encoding))
    f.close()

    salt = defins.crypto.Salt(config.saltLengh)
    pper = defins.crypto.Salt(config.pepperLengh)
    
    hsh = defins.crypto.sha256(salt+password+pper)
    f = open ( "sha256.csv", "wb" )
    f.write(str(salt+","+hsh+","+pper).encode(config.encoding))
    f.close()

    del salt, pppr, password

    

