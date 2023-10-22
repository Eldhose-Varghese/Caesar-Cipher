import asci_art
import cipher
import string_joiner

print(asci_art.asci_art_logo)
alphabets = [chr(ord("a")+i) for i in range(26)]
choice=True
while choice==True:
  word = input("Enter your message : ")
  shift = int(input("Enter the number to shift : "))
  option = input("Type E for Encode or Type D for Decode : ")
  result = cipher.cipher(option,word,shift)
  result_as_string=string_joiner.string_joiner(result)
  print(result_as_string)
  user_choice=input("Press y to play again or Press n to quit : ")
  if (user_choice=="n" or user_choice=="N"):
    choice=False
    print("Thanks for Playing !!!")
  else:
    choice=True
    