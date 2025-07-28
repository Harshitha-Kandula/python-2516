student_id=int(input("Enter student id: "))
student_name=input("Enter student name: ")
attendance=int(input("Enter student attendance: "))
subject="yes"
no_subjects=0
total_score=0

while subject=="yes" or subject=="Yes":
    no_subjects+=1
    score_each_subject=int(input(f"Enter score for Subject {no_subjects}: "))
    subject=input("Do you want to enter another score (yes/no): ")
    total_score+=score_each_subject
    
average_score=total_score/no_subjects

#==========================#
if average_score>=85:
    performance="Excellent"
elif 70<=average_score<=84:
    performance="Good"
elif 50<=average_score<=69:
    performance="Average"
else:
    performance="Needs Improvement"

#==================================================#
if attendance>=75:
    attendance_performance="OK, ATTENDANCE SATISFIED"
else:
    attendance_performance="WARNING - LOW ATTENDANCE"

#===================================================#

print("=============STUDENT DETAILS==============")
print("STUDENT ID:",student_id)
print("STUDENT NAME:",student_name)
print("STUDENT ATTENDANCE:",attendance)
print("TOTAL SCORE:",total_score)
print("TOTAL NO OF SUBJECTS:",no_subjects)
print("AVERAGE SCORE:",average_score)
print("PERFORMANCE:",performance)
print("ATTENDANCE:",attendance_performance)