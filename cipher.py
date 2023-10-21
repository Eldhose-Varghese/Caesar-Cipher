def cipher(option_fun,word_fun,shift_fun):
  result_to_return=[]
  if option_fun.upper()=="E":
      for i in list(word_fun):
        if i==" ":
          result_to_return.append(" ")
        else:
          if (ord(i)+shift_fun)<123:
            result_to_return.append(chr(ord(i)+shift_fun))
          else:
            num=(ord(i)+shift_fun)-123+97
            result_to_return.append(chr(num))
      return result_to_return
  elif option_fun.upper()=="D":
    for i in list(word_fun):
      if i==" ":
        result_to_return.append(" ")
      else:
        if (ord(i)-shift_fun)>97:
          result_to_return.append(chr(ord(i)-shift_fun))
        else:
          num=97-(ord(i)-shift_fun)
          if num!=0:
            result_to_return.append(chr(122-num+1))
          else:
            result_to_return.append(chr(97))
    return result_to_return