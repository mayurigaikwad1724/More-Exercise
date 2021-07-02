string_list=["Rishabh","Rishabh","abhishek","Rishabh","Divyashish","Divyashish"]
i=0
a=[]
while i<len(string_list):
    j=0
    while j<len(string_list):
        if string_list[i]==string_list[j]not in a:
            a.append(string_list[j])
        j=j+1
    i=i+1
print(a)