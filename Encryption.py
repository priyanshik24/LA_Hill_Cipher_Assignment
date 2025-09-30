def keyMatrixMaker(key):
  keyList = list()
  tempKeyList = list(key.lower())
  a = list()
  for i in tempKeyList:
    a.append(ord(i)-97)
  for i in range(0,9,3):
    keyList.append(a[i:i+3])
  return keyList

def matrixMultiplier(a,b):
  c = list()
  for i in range(0,3):
    val = 0
    for j in range(0,3):
      val+= a[i][j]*b[j]
    c.append(val)
  return c

def listOrdConverter(l):
  lr = list()
  for i in l:
    lr.append(ord(i)-97)    
  return lr

def matrixInverseChecker(m):
  if((m[0][0]*(m[1][1]*m[2][2] - m[2][1]*m[1][2])) - (m[0][1]*(m[1][0]*m[2][2] - m[2][0]*m[1][2])) + (m[0][2]*(m[1][0]*m[2][1] - m[1][1]*m[2][0])) == 0):
    return False
  else:
    return True

def hillCipherEncryption():
  
  #Fetching key
  key = str(input("Please enter the key of length 9 or lower: ")).lower()
  if (len(key)<9):
    for i in range(0,9-len(key)%9):
      key+= chr(i+97)
  print("New key",key)
  
   #Fetching msg
  msg = str(input("Please enter your message: ")).lower()
  
  #Making sure msg length is in multiple of 3
  while(len(msg)%3 != 0):
    msg+="z"
    
  msgOrdList = listOrdConverter(msg)
  keyMatrix = keyMatrixMaker(key)
  if(matrixInverseChecker(keyMatrix)):
    encMsg = ""
    for i in range(0,len(msgOrdList)-1,3):
      b= matrixMultiplier(keyMatrix,msgOrdList[i:i+3])
      for i in b:
        encMsg+=chr((i)%26+97)
    return encMsg
  
  else:
    print("Sorry, Use another key as Key Matrix is not inverse, hence it won`t be decrypted!")
    
print("Encoded Message: ",hillCipherEncryption())
