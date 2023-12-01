lista = ["ab","cd"]
listb = []
for i in lista:
    sum=0
    for j in i:
        ascii=ord(j)
        sum = sum+ascii
    listb.append(ascii)
print(listb)
