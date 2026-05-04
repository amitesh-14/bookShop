def count_frequency(arr):
    freq={}
    for num in arr:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    return freq
arr=[1,2,2,3,1,4,2]
print(count_frequency(arr))