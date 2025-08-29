# โปรแกรมแสดงข้อความต้อนรับนักศึกษา โดยรับชื่อ และชั้นปีทางแป้นพิมพ์แล้วแสดงข้อความต้อนรับ ดังนี้

student_name = input("กรุณาป้อนชื่อนักศึกษา: ")
year = input("กรุณาป้อนชั้นปี (1-4): ")
if year == "1":
    print("Welcome Freshman")
elif year == "2":
    print("Welcome Sophomore")
elif year == "3":
    print("Welcome Junior")
elif year == "4":
    print("Welcome Senior")
else:
    print("Oh, no