student_name=input("Enter Student name:")
student_grade=int(input("Enter Student grade:"))
base_tuition_fee=int(input("Enter Base tuition fee:"))
academic_topper=input("Is Student Academic topper ?(yes or no):").lower()
discount_percentage=0

if 1<=student_grade<=12:
    if 9<=student_grade<=12:
        if academic_topper=="yes":
            discount_percentage=20
        else:
            discount_percentage=10
    if 6<=student_grade<=8:
        discount_percentage=5
    if student_grade==10:
        discount_percentage+=3
    if student_grade==12:
        discount_percentage+=5
    total_fee=base_tuition_fee-base_tuition_fee*(discount_percentage/100)
    amount_saved=base_tuition_fee*(discount_percentage/100)

    print("Student name :",student_name)
    print("Grade level :",student_grade)
    print("Academic topper status :",academic_topper)
    print("Base tuition fee :",base_tuition_fee)
    print("Total discount percentage :",discount_percentage)
    print("Discount amount saved :",amount_saved)
    print("Final tuition fee after discount :",total_fee)

else:
    print("Invalid Grade")
