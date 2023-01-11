num1 = 1122334455666
num2 = 2.3
num3 = 1j
num1_str = str(num1)
len_str=len(num1_str)
print(len_str)
print(num1_str[2])
print(num1_str[2:6])
print(str(num2) in num1_str)
print(str(num3) in num1_str)
string_with_0 = '0' + num1_str
print(string_with_0)
print(string_with_0[:5])
print(string_with_0[5:])
print(string_with_0[-4:-1])



