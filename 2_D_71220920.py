print ("~~~~Table Matematika nich~~~~")
print("1. perkalian")
print("2. pemabagian")
pil = int(input("Masukan model matematika yang di inginkan 1/2: "))
if pil == 1:
  bilangan = int(input("Tabel perkalian: "))
  for i in range(1, 11):
    hasil = bilangan*i
    print(bilangan, 'x', i, '=', bilangan*i) 

elif pil == 2:
  bilangan = int(input("Tabel pembagian: "))
  for i in range(1, 11):
    hasil = bilangan/i
    print(bilangan, 'x', i, '=', bilangan/i)

