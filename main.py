
print("=" * 50)
print("         PREPTRACK APPLICATION")
print("=" * 50)
print()

while True:
    student_name = input("Enter Student Name: ")
    if student_name:
        break
    print("Student name cannot be empty.")

registration_number = input("Enter Registration Number: ")
while True:
    graduation_year=int(input("Enter graduation year:"))
    if graduation_year>=2025 and graduation_year<=2027:
        break
    else:
        print("Invalid input. Please enter a valid graduation year (between 2025 and 2027).")
graduation_eligible=(graduation_year>=2025 and graduation_year<=2027)
while True:
    attendance_percentage = float(input("Enter Attendance Percentage: "))
    if 0 <= attendance_percentage <= 100:
        break
    print("Invalid attendance percentage. Please enter a value between 0 and 100.")

while True:
    project_completion = input("Enter Project completion status (yes/no): ").lower()
    if project_completion == "yes":
        project_status = "Completed"
        break
    elif project_completion == "no":
        project_status = "In Progress"
        break
    print("Invalid project completion status. Please enter 'yes' or 'no'.")

while True:
    profile_verification = input("Enter Profile verification status (yes/no): ").lower()
    if profile_verification == "yes":
        profile_status = True
        break
    elif profile_verification == "no":
        profile_status = False
        break
    print("Invalid profile verification status. Please enter 'yes' or 'no'.")

total_score=attempted_days=absent_days=passed_days=failed_days=0
strong_days=satisfactory_days=improvement_days=critical_days=0
highest_score=lowest_score=0
highest_score_day=lowest_score_day=0
first_attempt_found=False
critical_score_found=False
first_critical_day=0
first_critical_score=0

for day in range(1,8):
    while True:
        score=int(input(f"Enter Day {day} score (0-100 or -1 for absent): "))
        if score==-1 or 0<=score<=100:
            break
        print("Invalid score. Enter -1 or a value between 0 and 100.")
    if score==-1:
        absent_days+=1
        print(f"Day {day} Result: Absent")
        continue

    attempted_days+=1
    total_score+=score
    if score>=60:
        passed_days+=1
    else:
        failed_days+=1

    if score>=75:
        strong_days+=1
        print(f"Day {day} Result: Strong")
    elif score>=60:
        satisfactory_days+=1
        print(f"Day {day} Result: Satisfactory")
    elif score>=40:
        improvement_days+=1
        print(f"Day {day} Result: Needs Improvement")
    else:
        critical_days+=1
        print(f"Day {day} Result: Critical")
        if not critical_score_found:
            critical_score_found=True
            first_critical_day=day
            first_critical_score=score

    if not first_attempt_found:
        highest_score=lowest_score=score
        highest_score_day=lowest_score_day=day
        first_attempt_found=True
    else:
        if score>highest_score:
            highest_score=score
            highest_score_day=day
        if score<lowest_score:
            lowest_score=score
            lowest_score_day=day

average_score= total_score/attempted_days if attempted_days else 0
attendance_eligible=attendance_percentage>=75
practice_count_eligible=attempted_days>=6
average_eligible=average_score>=70
critical_score_clear=not critical_score_found
passed_days_eligible=passed_days>=4

placement_ready=(graduation_eligible and attendance_eligible and practice_count_eligible and average_eligible and critical_score_clear and passed_days_eligible and project_status=="Completed" and profile_status)

if attempted_days==0:
    final_status="Practice Not Evaluated"; primary_blocker="No practice attempted"; next_action="Attempt the required coding practices"
elif critical_score_found:
    final_status="Critical Support Required"; primary_blocker="Critical score found"; next_action="Revise the concepts from the first critical day"
elif attempted_days<6:
    final_status="Practice Incomplete"; primary_blocker="Fewer than six practices attempted"; next_action="Complete at least six practice days"
elif passed_days<4:
    final_status="Insufficient Passed Practices"; primary_blocker="Less than four passed practices"; next_action="Pass at least four coding practices"
elif average_score<70:
    final_status="Practice Improvement Required"; primary_blocker="Average score below 70"; next_action="Improve the average score to at least 70"
elif attendance_percentage<75:
    final_status="Attendance Improvement Required"; primary_blocker="Attendance below 75"; next_action="Improve attendance to at least 75 percent"
elif not graduation_eligible:
    final_status="Graduation Criteria Not Met"; primary_blocker="Graduation year not eligible"; next_action="Check the eligible graduation-year requirement"
elif project_status!="Completed":
    final_status="Application On Hold"; primary_blocker="Project incomplete"; next_action="Complete the required project"
elif not profile_status:
    final_status="Application On Hold"; primary_blocker="Profile not verified"; next_action="Complete profile verification"
else:
    final_status="Ready for Mock Interview"; primary_blocker="None"; next_action="Proceed to placement mock interviews"

print("\n"+"="*50)
print("              PREPTRACK REPORT")
print("="*50)
print("STUDENT PROFILE")
print(f"Student Name         : {student_name}")
print(f"Registration Number  : {registration_number}")
print(f"Graduation Year      : {graduation_year}")
print(f"Attendance           : {attendance_percentage}")
print(f"Project Completed    : {project_status}")
print(f"Profile Verified     : {profile_status}")

print("\nPRACTICE SUMMARY")
print(f"Total Practice Days      : 7")
print(f"Attempted Days           : {attempted_days}")
print(f"Absent Days              : {absent_days}")
print(f"Passed Days              : {passed_days}")
print(f"Failed Days              : {failed_days}")
print(f"Strong Days              : {strong_days}")
print(f"Satisfactory Days        : {satisfactory_days}")
print(f"Needs Improvement Days   : {improvement_days}")
print(f"Critical Days            : {critical_days}")

print("\nPERFORMANCE ANALYSIS")
print(f"Total Score      : {total_score}")
print(f"Average Score    : {average_score:.2f}")

if attempted_days==0:
    print("Highest Score     : Not Available")
    print("Highest Score Day : Not Available")
    print("Lowest Score      : Not Available")
    print("Lowest Score Day  : Not Available")
else:
    print(f"Highest Score     : {highest_score}")
    print(f"Highest Score Day : Day {highest_score_day}")
    print(f"Lowest Score      : {lowest_score}")
    print(f"Lowest Score Day  : Day {lowest_score_day}")

print("\nCRITICAL SCORE INFORMATION")
print(f"Critical Score Found : {critical_score_found}")
if critical_score_found:
    print(f"First Critical Day   : Day {first_critical_day}")
    print(f"First Critical Score : {first_critical_score}")
else:
    print("First Critical Day   : Not Applicable")
    print("First Critical Score : Not Applicable")

print("\nFINAL DECISION")
print(f"Final Status    : {final_status}")
print(f"Primary Blocker : {primary_blocker}")
print(f"Next Action     : {next_action}")
print("="*50)