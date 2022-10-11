
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
for i in range (len(num2)):
    if num2[i] not in num1:
        print("False")
        break
else:
    print("True")
# ******************************
# Make your Code
# ******************************

# print ('True') or print ('False')
