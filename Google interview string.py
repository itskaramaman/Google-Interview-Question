
#This problem was asked by Google.

#The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

#Given two strings, compute the edit distance between them.

a=list(input())
b=list(input())
count=0
if len(a)<len(b):
    a,b=b,a
for i in range(len(a)):
    try:
        if b[i]!=a[i]:
            count=count+1
    except:
        count=count+1
print(count)        
        
        
        
