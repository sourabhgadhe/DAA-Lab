import random

def partition(arr,low,high):
    pivot_index=random.randint(low,high)
    arr[pivot_index],arr[low]=arr[low],arr[pivot_index]
    pivot=arr[low]
    start=low+1
    end=high
    while True:
        while start<=end and arr[start]<=pivot:
            start=start+1
        while start<=end and arr[end]>=pivot:
            end=end-1
        if start<end:
            arr[start],arr[end]=arr[end],arr[start]
        else:
            break
    arr[low],arr[end]=arr[end],arr[low]
    return end


def sort(arr,start,end):
    if start<end:
        idx=partition(arr,start,end)
        sort(arr,start,idx-1)
        sort(arr,idx+1,end)

        
def printarr(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
    print()



n=int(input("Enter total no. of terms: "))
arr=[]

print("Enter the terms: ")
for i in range(n):
    no=int(input())
    arr.append(no)


sort(arr,0,len(arr)-1)
print("\nThe sorted array is: ")
printarr(arr,len(arr))