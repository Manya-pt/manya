f=open("file1.txt","w")
seq=["first line\n","second line\n","third line\n","fourth line\n","fifth line\n",]
f.writeliens(seq)
f.close()
f=open("file1.txt","r")
line=f.readlines()
print("line:",line)
f.close()
