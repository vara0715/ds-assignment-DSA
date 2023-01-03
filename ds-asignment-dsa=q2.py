def listReversal():
    lst = list(map(int,input("\nEnter the array : ").strip().split()))
    start = 0
    end = len(lst)-1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst
listReversal()
