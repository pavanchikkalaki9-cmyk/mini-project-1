import time
def binarysearch(a,low,high,key):
    if low<=high :
        mid=(high+low)//2
        if a[mid]==key:
            print("search is succussfull key found at location:",mid)
            return
        elif key<a[mid]:
            binarysearch(a,low,mid-1,key)
        else:
            binarysearch(a,mid+1,high,key)
    else:
        print("search is unsuccuful:")
a=[]
n=int(input("How many elements:"))
for i in range(n):
    a.append(int(input("enter the numnber:")))
print("the array elemets are:",a)
key=int(input("enter the element to search:"))
start=time.time()
binarysearch(a,0,len(a)-1,key)
end=time.time()
print("Runtime of the program:",end-start)
