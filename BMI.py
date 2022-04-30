#BMI = weight / height**2
#result= whole number

height = input("enter height in m: ")
weight = input("enter weight in kg: ")

#BMI = weight/height**2
#print (BMI)
#Error : unsupported operand type(s) for ** or pow(): 'str' and 'int'

a= int (weight)
b= float (height)
BMI= int(a)/ float (b)**2
#print (BMI)
#result still not the whole number 
result= int (BMI)
print(result)
