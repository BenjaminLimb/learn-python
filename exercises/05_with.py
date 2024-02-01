# Raw exception prone code that won't close if the write fails
file = open("temp.txt", "w")
file.write("Hello World!")
file.close()

# Better
file = open("temp.txt","w")
file.write("Hello World!")
file.close()

# with statements reduce boilerplace lines of open, try, finally, close

with open('temp.txt','w') as file:
    file.write("Hello Word!")


