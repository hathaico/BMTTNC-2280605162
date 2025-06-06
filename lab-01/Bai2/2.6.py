input_str= input("Nhập X, Y :")
dimension= [int(x) for x in input_str.split(",")]
rowNum= dimension[0]
colNum= dimension[1]
multilist= [[0 for j in range(colNum)] for i in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col
print(multilist)