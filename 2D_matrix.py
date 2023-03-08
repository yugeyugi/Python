mat=[
    [1,1,1,0,0,0],
    [0,1,0,0,0,0],
    [1,1,1,0,0,0],
    [0,0,2,4,4,0],
    [0,0,0,2,0,0],
    [0,0,1,2,4,0]
]

sum=0
for i in range (0, len(mat)-2):
    for j in range (0, len(mat[i])-2):
        hourglass_sum=mat[i][j]+mat[i][j+1]+mat[i][j+2]+mat[i+1][j+1]+mat[i+2][j]+mat[i+2][j+1]+mat[i+2][j+2]
        sum=max(sum,hourglass_sum)
print(sum)
