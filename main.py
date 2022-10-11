
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
for i in range (len(num2)):
    if num2[i] not in num1:
        break
if i==len(num2):
    print("True")
else:
    print("False")
# ******************************
# Make your Code
# ******************************

# print ('True') or print ('False')
