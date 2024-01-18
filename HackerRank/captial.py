s="ravi teja"
print(s)
l=len(s)
if(s.isalnum()):
    print(s)
elif(s.isalpha()):
    x=s[0].upper()
    for i in range(1,l):
        print(s)
        if(s[i]==" "and i!=l):
          y=s[i+1].upper()
          break
    print(x+s) 
 

        
    