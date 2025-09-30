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
#DECRYPTION MATRIX FUNCTIONS
def matrixTranspose(m):
  am = list()
  
  for i in range(0,3):
    b = list()
    for j in range(0,3):
      b.append(m[j][i])
    am.append(b)
  return am

def matrixCofactor(m):
  cm = list()
  for i in range(0,3):
    b = list()
    for j in range(0,3):
      if((i+j+2)%2 == 0):
        b.append((m[(i+1)%3][(j+1)%3]*m[(i+2)%3][(j+2)%3] - m[(i+1)%3][(j+2)%3]*m[(i+2)%3][(j+1)%3])%26)
      else:
        b.append(((m[(i+1)%3][(j+1)%3]*m[(i+2)%3][(j+2)%3] - m[(i+1)%3][(j+2)%3]*m[(i+2)%3][(j+1)%3]))%26)
    cm.append(b)
  return cm

def matrixAdjoint(m):
  return matrixTranspose(matrixCofactor(m))

def multiplicativeInverse(num):
  for i in range(1,26):
    if((i*num)%26 == 1):
      return i

def matrixDeterminant(m):
  return (m[0][0]*(m[1][1]*m[2][2] - m[2][1]*m[1][2])) - (m[0][1]*(m[1][0]*m[2][2] - m[2][0]*m[1][2])) + (m[0][2]*(m[1][0]*m[2][1] - m[1][1]*m[2][0]))

def matrixInverse(m):
  mi = list()
  mi_det = multiplicativeInverse(matrixDeterminant(m))
  mi_adj = matrixAdjoint(m)
  for i in range(0,3):
    b = list()
    for j in range(0,3):
      b.append(mi_adj[i][j]* mi_det)
    mi.append(b)
  return mi

def hillDecryption():
  key = str(input("Please enter the key of length 9 or lower: ")).lower()
  if (len(key)<9):
    for i in range(0,9-len(key)%9):
      key+= chr(i+97)
  print("New key",key)
  encMsg = str(input("Please enter the encrypted message: ")).lower()
  
  decKeyMatrix = matrixInverse(keyMatrixMaker(key))
  encMsgOrdList = listOrdConverter(encMsg)
  decMsg = ""
  for i in range(0,len(encMsgOrdList)-1,3):
    b= matrixMultiplier(decKeyMatrix,encMsgOrdList[i:i+3])
    for i in b:
      decMsg+=chr(int((i)%26 + 97))
  return decMsg

print("Original Message:", hillDecryption())
