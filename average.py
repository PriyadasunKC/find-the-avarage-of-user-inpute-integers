# average programme
count = 0
sum = 0
average = 0

number = int(input("Enter Integer : "))
while(number != -1):
    count += 1
    sum += number
    number = int(input("Enter Integer : "))

average = sum/count
print("Average : {}".format(average))
