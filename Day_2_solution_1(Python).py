string=input()
d="aeiou"
h=[]
for i in range(len(string)):
    if(string[i]in d):
        h.append(string[i])
r= [] 
[r.append(x) for x in h if x not in r]
j=sorted(r)
if(len(j)!=0):
    print(*j,sep="")
else:
    print("Thank You")
