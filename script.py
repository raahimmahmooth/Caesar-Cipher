#to optimization you can only create only one function
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encryption(plane_text,shift_k):#hello
    ciper_text=""
    for char in msg: #h=7 12132
      if char in letters:
        position=letters.index(char)
        #print(position)
        shift=position+shift_key
        #print(shift)
        ciper_text+=letters[shift%26]
      else:
          ciper_text+=char
    print(ciper_text)

def decryption(cipher_text,shift_k):
    plane_text = ""
    for char in msg:#char=k
      if char in letters:
        position = letters.index(char)
        # print(position)
        shift = position - shift_key
        # print(shift)
        plane_text += letters[shift % 26]
      else:
          plane_text+=char
    print(plane_text)
end=False
while not end:
    choice = input("Type 'encrypt' for encryption,type 'decrypt' for decryption:")
    msg = input("type your message:").lower()
    shift_key = int(input("Type the shift number:"))

    if choice == 'encrypt' or choice == 'ENCRYPTION':
        encryption(plane_text=msg, shift_k=shift_key)
    elif choice == 'decrypt' or choice == 'DECRYPTION':
        decryption(cipher_text=msg, shift_k=shift_key)
    else:
        print("wrong input!")
        exit()
    do_again=input("Type 'yes' to continue,type 'no' to exit:")
    if do_again=='no':
        end=True
        print("Have a nice day bye!")



