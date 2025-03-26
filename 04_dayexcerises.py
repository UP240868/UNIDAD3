#1
print('30\tdays\tof\tpython')
#2
print('coding\tfor\teveryone')
#3
company=('Coding\tFor\teveryone')
#4
print(company)
#5
print(len(company))
#6
print(company.upper())
#7
print(company.lower())
#8
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9
print(company[0:6])
#10
print(company.index('Coding'))
#11
print(company.replace('Coding' , 'python'))
#12
print(company.replace('everyone' , 'All'))
#13
print(company.split())
#14
e='Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(e.split())
#15
print('Coding for all'[0])
#16
print('Coding for all'[13])
#17
print('Coding for all'[11])
#18
print('Python For Everyone'.replace('Python For Everyone', 'PFE'))
#19
print('Coding For All'.replace('Coding For All', 'CFA'))
#20
print(company.index('C'))
#21
print(company.index('F'))
#22
print('Coding For All People'.rfind('l'))
#23
print("You cannot end a sentence with because because because is a conjunction".index('because'))
#24
print("You cannot end a sentence with because because because is a conjunction".rindex('because'))
#25
print("You cannot end a sentence with because because because is a conjunction"[31:54])
#26
print("You cannot end a sentence with because because because is a conjunction".find('because'))
#27
print("You cannot end a sentence with because because because is a conjunction"[31:54])
#28
print(company.startswith('Coding'))
#29
print(company.endswith('coding'))
#30
print('   Coding For All      '.strip())
#31
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
#32
print('Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon', sep='# ')
#33
print('I am enjoying 30 days of python.\nI am enjoying building the challenges.\n')
#34
print('Name\tAge\tCountry\nAsabeneh\t250\tFinland')
#35
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius', radius, 'is', area)
#36
Suma = 8 + 6
Resta = 8 - 6
Multiplicacion = 8 * 6
Division = 8 / 6
Modulo = 8 % 6
Division_entera = 8 // 6
Potencia = 8 ** 6

print('8 + 6 =', Suma)
print('8 - 6 =', Resta)
print('8 * 6 =', Multiplicacion)
print('8 / 6 =', Division)
print('8 % 6 =', Modulo)
print('8 // 6 =', Division_entera) 
print('8 ** 6 =', Potencia)