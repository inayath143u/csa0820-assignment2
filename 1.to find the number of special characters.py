#finding special character
n="Modi Birthdat @September 17,#&$%"
count=0
for i in range(0,len(n)):
    if n[i]>=chr(65) and n[i]<=chr(90):
        continue
    elif n[i]>=chr(97) and n[i]<=chr(122):
        continue
    elif n[i]>=chr(48) and n[i]<=chr(57):
        continue
    elif n[i]==" ":
        continue
    else:
        count=count+1 
        
print("special character are",count)
