from Crypto.Cipher import DES
import os
import sys, getopt
#DES, MODE_ECB, PKCS #5, pass.encode('utf-8'), len(pass) = 8


#input bytes
def pad(text):
    len_temp = 8 - len(text) % 8                #length of temp
    padding = len_temp*str(len_temp)            #temp = 5 ==> padding = '55555' (str)
    text = text + padding.encode('utf-8')       #encode('utf-8') --> b'55555' ==>padded_text = text + ...
    return text                                 

# input bytes, str
def encrypt(text, key):
    if type(text) != bytes:
        text = text.encode('utf-8')
    padded_text = pad(text)                     #<class 'bytes'>
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    result = cipher.encrypt(padded_text)        
    return result                               #<class 'bytes'>


# input bytes, str
def decrypt(cipher_text, key):
    pt = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    result = pt.decrypt(cipher_text)               

    temp = int(chr(result[-1]))                 #length of temp
    result_without_temp = result[:-temp]        #remove temp

    return result_without_temp                  #return bytes

# input str, str
def encrypt_file(file_name, key):
    with open(file_name, 'rb') as f:
        text = f.read()                          #<class 'bytes'>
    result = encrypt(text, key)                  #<class 'bytes'>
    os.remove(file_name)

    with open(file_name + '.enc', 'wb') as f_enc:
        f_enc.write(result)


# input str, str
def decrypt_file(file_name, key):
    with open(file_name, 'rb') as f:
        cipher_text = f.read()
    result = decrypt(cipher_text, key)
    os.remove(file_name)
    with open(file_name[:-4], "wb") as f_dec:  #encoding='utf-8'     --> ghi unicode
        f_dec.write(result)                     #write() argument must be str, not bytes



def main(argv):
    filename = ''
    key = ''
    mode = ''

    try:
        opts, args = getopt.getopt(argv,"hi:k:m:",["ifile=","key=","mode="])   #sau dau :/= bat buoc phai co gia tri
    except getopt.GetoptError:
        print('1712601.py -i <filename> -k <key: 8 bytes> -m <mode: e/d>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('1712601.py -i <filename> -k <key: 8 bytes> -m <mode: e/d>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            filename = arg
        elif opt in ("-k", "--key"):
            key = arg
        elif opt in ("-m", "--mode"):
            mode = arg
    if mode == 'e':
        encrypt_file(filename,key)
        print('check file.enc in current working directory')
    elif mode == 'd':
        decrypt_file(filename,key)
        print('decrypted')
    else:
        print('1712601.py -i <filename> -k <key: 8 bytes> -m <mode: e/d>')
        sys.exit(2)
    
    
if __name__ == "__main__":
   main(sys.argv[1:])