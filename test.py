#%%
matrix = [[2,4],[4,5],[6,5],[5,6]]
ls = []
j = 1
for i in range(len(matrix)):
    print(i,j)
    if(matrix[i][1] == matrix[j][0]):
        ls.append((matrix[i][1],matrix[j][0]))
    if(j!=len(matrix)-1):
        j+=1
print(ls)
# %%
