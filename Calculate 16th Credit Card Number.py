kart = list(input())
del kart[15]
sum = 0
j = 1
for i in kart:
    int_i = int(i)
    if j % 2 == 0:
        sum += int_i
    else:
        sum += int_i * 2
        if int_i * 2 > 9:
            sum -= 9
    j += 1

i16 = 10 - (sum % 10)
if i16 == 10:
    i16 = 0
print(i16)