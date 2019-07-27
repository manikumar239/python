#Task1
print("numbers divisible by 7 but not 5 multiples \n")
x=2000;
y=3200;
res = []
while x <= y:
    if (x % 5 != 0 and x % 7 ==0):
        res.append(x)
    x += 1
print(res)



#task2
print("\n First name and last name \n")
FirstName = input("enter first name: ")
LastName = input("enter last name: ")
print(LastName," ",FirstName)


#task3
print("\n sphere volume \n") 
r_string = input('enter radius value: ')
r = int(r_string)
res = (4/3) * (22/7) * (r*r*r)
print("volume = ", res)


#task4
print("\n Word reverse \n") 
r_string = input('enter word to reverse: ')
len_string = len(r_string)
rev_string = str()
i = 0
while len_string - 1 >= i:
    rev_string = rev_string + r_string[len_string - 1]
    len_string -= 1
print("reversed string: ",rev_string)


#task5
print("\n Stars \n") 
stars = input("max no. of stars to be printed: ")
int_stars = int(stars)
for x in range(0, int_stars+1):
    if(x == int_stars):
        #print("x value",x)
        for i in range (int_stars, 0 , -1):
            #print("i value", i)
            for z in range (i, 0 , -1):
                if (z == 1):
                    print("*\n")
                else:
                    print("* ", end='')
    else:
        for y in range (0, x):
            if (y == x-1):
                print("*\n")
            else:
                print("* ", end='')
				
				

#task6				
print("print numbers taking from user input \n")
strList = input("enter numbers separated by comma: ")
numList = strList.split(",")
print(numList)



#task7
print("print string\n")
print("WE, THE PEOPLE OF INDIA, \n\t having solemnly resolved to constitute India into a SOVEREIGN,! \n \t \t SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n \t \t and to secure to all its citizens")
