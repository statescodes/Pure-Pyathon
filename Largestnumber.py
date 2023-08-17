 # if.. else.. else statement
 # create a program for grades input with the following
 #     80-100-A
 #     60-79-B
 #     50-59 -C
 #     30-49-D
 #     Below 30-Fail
 # negative and above 100-invalid input

num=int(input("Enter the first num:"))
num2=int(input("Enter the second num:"))
num3=int(input("Enter the third num:"))
num4=int(input("Enter the forth num:"))

if num>num3 and num2>num3 and num>num4:
    print(num,"Is greater")
elif num2>num and num2>num3 and num2>num4:
    print(num2,"is greater")
elif num3>num and num3>num2 and num3>num4:
    print(num3,"Is greater")


else:
    input("invalid input")



