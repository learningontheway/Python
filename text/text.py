text='''use text to  
     say 'HelloWord'2\n'''
with open ("word.txt","w") as f:
    f.write(text)
    f.close()
f= open ("word.txt","r")
for line in  f.readlines():
    print(line,end="")

