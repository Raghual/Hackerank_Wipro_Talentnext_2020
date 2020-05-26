str1=input()
str1=str1.lower()
str2=input()
str2=str2.lower()
a=str1+str2
p=sorted(a)
r= [] 
[r.append(x) for x in p if x not in r]
print(*r,sep="")


