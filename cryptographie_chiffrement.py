

tab = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",  "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
spec = ["'", ",", " "]


def vig_test():
  m = input("Entrez le Message m : ").upper()
  k = input("Entrez la Clee k : ").upper()
  ms = m
  for value in spec:
      ms = ms.replace(value, "")
  print(ms)
  c = ""
  i = 0
  for value in ms:
      if i==(len(k)):
        i=0
      c = c + (tab[  tab.index(k[i]) + tab.index(value)    ])
      i = i+1
      
  print("Le Message Initial est : ",m,"\n")
  print("La Clee est : ",k,"\n")
  print("Le Message Chiffre est : ",c,"\n")

def vig_test2():
  m = input("Entrez le Message m : ").upper()
  k = input("Entrez la Clee k : ").upper()
  ms = m
  for value in spec:
      ms = ms.replace(value, "")
  print(ms)
  c = ""
  i = 0
  for value in ms:
      if i==(len(k)):
        i=0
      c = c + (tab[ tab.index(value) - tab.index(k[i])  ])
      i = i+1
      
  print("Le Message Initial est : ",m,"\n")
  print("La Clee est : ",k,"\n")
  print("Le Message Chiffre est : ",c,"\n")


def cesar_test():
  m = input("Entrez le Message m : ").upper()
  ms = m
  for value in spec:
      ms = ms.replace(value, "")
  print(ms)
  c = ""
  for value in ms:
      c = c + (tab[  3 + tab.index(value)    ])
      
  print("Le Message Initial est : ",m,"\n")
  print("Le Message Chiffre est : ",c,"\n")


def atbash_test():
  m = input("Entrez le Message m : ").upper()
  ms = m
  for value in spec:
      ms = ms.replace(value, "")
  print(ms)
  c = ""
  for value in ms:
      c = c + (tab[  25 + tab.index(value)    ])
      
  print("Le Message Initial est : ",m,"\n")
  print("Le Message Chiffre est : ",c,"\n")


def rot13_test():
  m = input("Entrez le Message m : ").upper()
  ms = m
  for value in spec:
      ms = ms.replace(value, "")
  print(ms)
  c = ""
  for value in ms:
      c = c + (tab[  13 + tab.index(value)    ])
      
  print("Le Message Initial est : ",m,"\n")
  print("Le Message Chiffre est : ",c,"\n")


vig_test2()


# "J'ADORE ECOUTER LA MUSIQUE TOUTE LA JOURNEE"
# "MUSIQUE"