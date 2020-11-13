# Module 1
# Excerise 1
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)

# Excerise 2
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

# Excercise 3
country  = str(input("What country are you from: "))

print('I have heard that '+ country + ' is a beautiful country.')

# Excercise 4
# n = int(input("Input a number: "))

n = 4

# use for loop to iterate 10 times
for i in range(1,11):
   print(n,'x',i,'=',n*i)

  # Excercise 5
   # n = int(input("Input a number: "))

n = 4

# use for loop to iterate 10 times
for i in range(1,11):
   print(n,'x',i,'=',n*i)

   #Excercise 5
   for i in range(1,11):
    for j in range (1,11):
        print(i*j, end='\t')
    print ('')