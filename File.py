filename = "readme.txt"

with open(filename) as fn:
    content = fn.readlines()

print(content)


#---------------

f = open("output.txt","w")
f.write("Pythonprogramminglanugage.com, \n")
f.write("Example program.")
f.close()