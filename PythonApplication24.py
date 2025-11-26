f = open('cmp142.txt','w')
f.write("We are created the txt named with a cmp142\n") #question 5.a
f.write("File is a named we are used for storage some informations\n") #question 1
f.write("File is a where is our informations storaged place\n") #question 1
f.write("File Modes are functions of file handling which is we are trying to storage") #question 1
f.write("Binary file is writing the 0 and 1.Why we need binary files?\n") #question 1
f.write("Because binary files can be read generally.If we say the system read the image in binary it can.\n") #question 1
f.write("If we didn't use binary we cant read images.It gonna try read by like text.So its going to be exception\n") #question 1
f.write(" but binary files if you want write you can write on them because binary file uses raw data(reads byte to byte).\n") #question 1
f.write("what happens when you open a file using 'r' mode?\n") #question 4
f.write("r mode is only read mode.you can't write or any changes on this mode.You can only read.") #question 4
f.close()              #question 5.b

f = open('cmp142.txt','a')
f.write('"W" and "A" modes same with if you dont have a named file they creates.They bought writes.But the difference is\n') #question 3a
f.write('W is when you used Reset old informations and start from zero.Append is continoue to old writings\n') #question 3a
f.close()

f= open('cmp142.txt','a')
f.write('File handling is a way of how to control files and informations.\n') #question 1-2
f.write("When the program ends all data is lost because RAM can't storage.RAM only holds quick informations.\n ") # question 6.a - 2
f.write("This is why file handling is important.If you want storage some information you need to use file handling method\n") #question 1-2
f.write("With file handling you can storage,manipulate information so you can control information and\n") #question 6.b
f.write("you are taking from volatile memory(RAM) to persistent memory(file)") #question 6.b
f.close()

f = open(r'cmp142.txt') # I prefered show to all outputs than screenshots
print(f.read())
f.close()


name= input("Please Entry name\n") #question 7.a
age = input("How old are you?\n") #question 7.b


f = open('users.txt','a') #we opened with append mode because we dont want to truncate old informations
f.write("(" + name + ",")
f.write(age + ") ")             
f.close()           #question 7.b

f = open('users.txt','r')
print(f.read())         #question 7.c
f.close()      

f = open('cmp142.txt','a+')
over_ride =f.tell()
f.write ("if we have lots of student records we have to use append 'a' mode because write mode gonna be truncate\n")
f.write(" and all scores gonna be lost for a forever. but when we use append mode we start place on where we stop.\n")
f.write("this mean we can add informations without delete all of old informations.Actually,\n")
f.write ("we are not deleting old information we just start to change first character but it's also meaning lost information!\n")
f.write("Bora Akin,K20210538")
f.seek(over_ride)
print(f.read())
f.close()


