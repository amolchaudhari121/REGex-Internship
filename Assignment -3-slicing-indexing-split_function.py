
#Name = Amol Chaudhari
#Date = 03/12/2021
#Assignment No = 1
# Q1 - Extract the fruits name only
s = "APPLEFRUITBANANAFRUITKIWIFRUITMANGOFRUITORANGE"
s_split=s.split("FRUIT")    #here we split the string by using split function
print(s_split)

print("\n****************************************")


#Assignment No - 2
# Q2 - Extract "First name",'Last name' and "Domain" from given String,
emailid = 'amol.chaudhari@gmail.com'
a=emailid.split(".")  #here we split the string by using split function
# print(a)
res=a[1]             #Here we extract the first name using indexing
# print(res)
b=res.split('@')     #here we split the string by using split function.
# print(b)
print('First name = ',a[0])            #''' Here we extracted and print all  the string'''
print('Last name = ',b[0])
print('Domain = ',b[1])


print('\n*********************************************')

#Assignment - 3

# Q3 - Extract "First name",'Last name','Birth year','Age' and "Domain" from given String,

d = "amol.chaudhari1996@gmail.com"
e=d.split('.')
print("First name = ",e[0])
#print(e)
f=e[1]
print("Last name = ",f[0:9])
print("Birth Year = ",f[9:13])
print('Age = ',2021-int(f[9:13]))
print('Domain = ',f[-5:])



