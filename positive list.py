list1=[2,4,-6,-8,9,7]
list2=[]
for i in list1:
    if i>0:
        list2.append(i)
print(f"positive list= {list2}")


list1=[2,4,-6,-8,9,7]
list2=[i for i in list1 if(i>0)];
list3=[i for i in list1 if(i<0)];
print(f"positive list= {list2}")
print(f"negative list={list3})
    
