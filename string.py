str1 = 'single quoted string'
str2 = "double quoted string"
str3 = """triple quoted string"""

print(str1,str2,str3)

print(str1[0:1])

print("single element from the string using indexing:",str1[0])
print("positive indexing:",str1[0:6])
print("length of string:",len(str1))
print("lower case:",str1.lower())
print("upper case:",str1.upper())
print("title case:",str1.title())