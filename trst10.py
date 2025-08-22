


numbers = []
print('ป้อนตัวจำ 5 ตัว')
for i in range(5):
    number = int(input('ป้อนตัวจำ ' + str(i+1) + ' : '))
    numbers.append(number)


sum_of_numbers = sum(numbers)
average_of_numbers = sum_of_numbers/5



print('=====================================')
print(f"ผลรวมของตัวเลขคือ 5 ตัว {sum_of_numbers}") 
print(f"ค่าเฉลี่ยของตัวเลขทั้งหมดคือ {average_of_numbers/5}")
print('=====================================')