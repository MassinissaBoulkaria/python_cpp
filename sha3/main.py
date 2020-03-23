import sha3

def AfficheHash(hash):
    print("\"",hash,"\"", " => ","\"", sha3.hash(hash),"\"")


ListStr=["","a","abc","message digest","abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789","1234567890123456789012345678901234567890123456789$

for str in ListStr :
    AfficheHash(str)
