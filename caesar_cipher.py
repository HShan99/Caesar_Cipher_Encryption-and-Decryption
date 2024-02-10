alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
            'q','r','s','t','u','v','w','x','y','z']

def encryption(plain_text,shift_key):                #The encryption function
    cipher_text=""
    for char in plain_text:                          
        if char in alphabet:                            
            position_of_char = alphabet.index(char)                    #To take characters index position 
            new_position_of_char = (position_of_char + shift_key)%26   #Equation of plain text to cipher text (E= (x+n)%26)
            cipher_text +=alphabet[new_position_of_char]               #New position of the character 
        else:
            cipher_text += char                                        # To take spaces in the text 
    print(f"Cipher text : {cipher_text}")                              # Output of the cipher text


def decryption(cipher_text,shift_key):                                 # The Decryption function 
    plain_text=""
    for char in cipher_text:
        if char in alphabet:
            position_of_char = alphabet.index(char)                     #To take characters index position 
            new_position_of_char = (position_of_char-shift_key)%26      #Equation of cipher text to plain text (E= (x+n)%26)     
            plain_text +=alphabet[new_position_of_char]
        else:
            plain_text += char                                          # To take spaces in the text 
    print(f"Plain text : {plain_text}")                                 #Output of the plain text




End_to_process = False
while not End_to_process:
    User_Choice=input("Type 'encrypt' for Encryption, Type 'decrypt' for Decryption : \n")          #Take user choice Encrypt or Decrypt
    text = input("Type your Message : \n").lower()                                                  #Take message as lower case
    shift = int(input("Enter shift Key : \n"))                                                      #Take key value as int value 
    if User_Choice == "encrypt":
        encryption(plain_text=text,shift_key=shift)                                                 #Calling encryption function
    elif User_Choice == "decrypt":
        decryption(cipher_text=text,shift_key=shift)                                                #Calling Decryption function
    To_continue = input("Type 'yes' to continue, Type 'no' to exit. \n ")
    if To_continue == 'no':
        End_to_process = True
        print("Than you.........")
    