# โปรแกรมคำนวณค่าคอมมิชชั่นของพนักงานขาย โดยป้อนรหัสพนักงาน ชื่อพนักงาน และจำนวนเงินซึ่งเป็นยอดขายของพนักงาน จากผู้ใช้ทางแป้นพิมพ์ และคำนวณค่าคอมมิชชั่น จากเงื่อนไข ดังนี้

emp_id = input("กรุณาป้อนรหัสพนักงาน: ")
emp_name = input("กรุณาป้อนชื่อพนักงาน: ")
sales = float(input("กรุณาป้อนยอดขาย: "))
if sales <= 1000:
    commission = 0.0
elif sales <= 2000:
    commission = sales * 0.01
elif sales <= 3000:
    commission = sales * 0.03
else:
    commission = sales * 0.05
print(f"พนักงาน {emp_id} {emp_name} ได้ค่าคอมมิชชั่น {commission:.2f} บาท")

