a = [0,1,3,7,10,11,13]
b = [2,4,12]

def merge(left, right, arr):

    nl, nr = len(left), len(right)
    i, j, k = 0,0,0

    while i<nl and j<nr:
        if left[i] < right[j]:
            arr[k] = left[i]
            i+=1
            k+=1
        else:
            arr[k] = right[j]
            j+=1
            k+=1

    while (i<nl):   #left over in Left sublist
        arr[k] = left[i]
        i+=1
        k+=1
    
    while(j<nr):    #left over in Right sublist
        arr[k] = right[j]
        j+=1
        k+=1       

    return arr

def mergeSort(A):

    n = len(A)
    if n < 2:   # n = 0,1
        return
    else:
        mid = n//2
        left = A[:mid]  # 0 - mid-1
        right = A[mid:] # mid - n-1
        mergeSort(left)
        mergeSort(right)
        merge(left, right, A)

    return A

myarr = [1,10,2,6,9,4,5,11,67,21,77,10,56,10,10]
print(mergeSort(myarr))
