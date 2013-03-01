#Basic bubble sort project
def bubble_sort(n):
    nlen = len(n)
    for i in range (0,nlen):
        for j in range(0,(nlen-i-1)):
            if(n[j]>n[j+1]):
                temp = n[j]
                n[j]=n[j+1]
                n[j+1]=temp
    return n