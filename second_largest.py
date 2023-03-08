arr=[234,12,674,123,456,78,94]

f_l=0
s_l=-1

for i in range (0, len(arr)):
    if(arr[i]>arr[f_l]):
        s_l=f_l
        f_l=i
    elif(arr[i]<arr[f_l]):
        if(arr[i]>arr[s_l]):
            s_l=i
print(arr[s_l])