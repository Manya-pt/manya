f1=open("abc.txt","w")
print("name of the file:",f1.name)
print("closed or not:",f1.closed)
print("opening mode:",f1.mode)



f=open("text.txt","w")
f.write("my first file\n")
f.close()
print("file",f.name,"closed")
