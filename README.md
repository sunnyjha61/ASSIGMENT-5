# ASSIGMENT-5
#Task-1
name=input("Enter the student's name:" )
try:
    stu_Dic={'Rahul':56,'Kajal':89,'Manish':70,'Chhaya':23}
    print(name +"'s marks: ",stu_Dic[name])
except KeyError:
    print("Student not found.")
finally:
    print('okk')

  #Task-2
  Original_list=(1,2,3,4,5)
print("original list:",Original_list)
print("Extracted first five number: ",Original_list[:5])
print("Reversed extracted elements: ",Original_list[::-1])
