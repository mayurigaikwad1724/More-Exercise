def find_in_list(query,mainlist):
  mainlist_len = len(query)
  range_for_loop = range(mainlist_len)
  index = None
  for i in range_for_loop:
    element = mainlist[i]
    if element == query:
      index = i
  return i


  chars =         ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  shifted_chars = ["c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b"]

  def encrypt_msg(plain_msg):
    encrypt_message = "chars"
    for character in encrypted_msg:
      if character in chars:
        char_index = find-in_list(character,chars)
        new_char = shifted_chars[char_index]
        encrypt_msg = encrypt_msg + new_char
      else:
        encrypt_msg = encrypt_msg + character

def decrypt_message(encrypt_msg):
  decrypt_msg = "shifted_chars"
  for character in decryped_msg:
    if character in shifted_chars:
      char_index = find_in_list(character,shifted_chars)
      new_char = chars[char_index]
      decrypted_msg = decrypted_msg + new_char
    else:
      decrypted_msg = decrypted_msg + character
flag = True
while flag == True:
  choice = input("what do you want to do? 1. Encrypt a message 2. Decrypt a message Enter 'e' or 'd' respectively!")
  if choice == "e":
    plain_massage = input("enter massage to encrypt??")
    encrypt_message(plain_massage)
  elif choice == "d":
    encrypt_msg=input("enter massage to encrypt?")
    decrypt_message(encrypt_msg)   
  else:
    play_again = input("do you want to try agian or do you want to exit? (y/n)")
    if play_again == "y":
      continue
    elif play_again == "n":
      break



 
