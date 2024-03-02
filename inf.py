num =0
iseven = True
f = open("a.py","w")
f.write("num = 0\n")
f.write("print(\"enter a num:\")\n")
f.write("num = (int)(input())\n")
for i in range(900000):
    f.write(f"if  num == {i}:\n")
    if iseven:
        f.write(" print(\"even\")\n")
    if not iseven:
             f.write(" print(\"odd\")\n")
    iseven =  not iseven
    
