name=input("Enter the student's name:" )
try:
    stu_Dic={'Rahul':56,'Kajal':89,'Manish':70,'Chhaya':23}
    print(name +"'s marks: ",stu_Dic[name])
except KeyError:
    print("Student not found.")
finally:
    print('okk')