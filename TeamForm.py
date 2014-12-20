def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    return alist

def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x: 
            hi = mid
        else:
            return mid
    return -1

def duplicate_list(dupe):
    a = []
    dupe = mergeSort(dupe)
    for j in range(0,len(dupe)-1):
        if (dupe[j]==dupe[j+1]):
            a.append(dupe[j])
    return a

def mergeList(d,s):
    for j in range(0,len(d)):
        if j!=0:
            if (d[j]-d[j-1] == 1):
                b = b+1
                s.insert(b,d[j])
                continue
        b = binary_search(s,d[j])
        p = 0
        if ((b!=-1) & (b==0)):
            s.insert(b+1,d[j])
        if ((b!=-1) & (b!=0)):
            while p!=-1:
                if d[j]-s[b-1]>1:
                    p = -1
                else:
                    if (d[j]-s[b-1]==1)|(d[j]-s[b-1]==0):
                        p = b-1
                        b = b-1
                    else:
                        b = b-1
                if (b<=0):
                    p = -1
            if b!=-1:
                b = b+1
                s.insert(b,d[j])
    return s

import sys
n = input()
if (type(n)!= int):
    print("invalid input:enter integer")
    sys.exit()
for i in range(1,n+1):
    s = raw_input()
    if (type(s)!= str):
        print("invalid string:enter string")
        sys.exit()
    s = map(int, s.split( ))
    n = s[0]
    s = s[1:n+1]
    dupe = []
    dupe = duplicate_list(s)
    s = list(set(s))
    d = list(set(dupe))
    d = mergeSort(d)
    s = mergeSort(s)
    if d!=[]:
        s = mergeList(d,s)
    while dupe!=[]:
        dupe = duplicate_list(dupe)
        d = list(set(dupe))
        d = mergeSort(d)
        if d!=[]:
            s = mergeList(d,s)
    
    minv = len(s)
    p = 0
    for j in range(0,len(s)-1):
        if (s[j+1]-s[j] == 1):
            if j == len(s)-2:
                p = p+2
                if minv>p:
                    minv = p
                continue
            p = p+1
        else:
            p = p+1
            if (j+1 == len(s)-1)|(j==0):
                p = 1
            if minv>p:
                minv = p
            p=0
    print minv







