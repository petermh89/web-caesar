def alphabet_position(letter):   
    # returns the 0-based numerical position of that letter within the alphabet

    ord_let = ord(letter.lower()) - 97
    return ord_let
  




def rotate_character(char, rot):
    #this fuction shifts the variable char by the variable rot number of times
   
    shift_ = alphabet_position(char)
    new_ord = (shift_ + rot) % 26
    new_num = new_ord + 97
    
    new_let = chr(new_num)
    
    
    if char.isupper(): 
        newer_let = new_let.upper()    
        return newer_let   
        
    else:
            
        return new_let   

def encrypt(text, rot):
    """This function rotates each letter in a text statement by the rot number"""

    new_text = ""
    for i in text:
        if i.isalpha():
            x = rotate_character(i, rot)
            new_text = new_text + x
            
        else:
            new_text = new_text + i 
    print()
    
    return new_text           




def main():
    mess = input('What message do you want to encrypt?')
    rot_by = int(input('set your rotation'))
    print(encrypt(mess, rot_by))

    
    

if __name__ == "__main__":
    main()

