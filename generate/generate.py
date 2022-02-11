import os
import qrcode
import datetime

folName = "qrc"
if not os.path.isdir(folName):
	os.makedirs(folName)

n = int(input("Enter no. of students: "))
for i in range(n):
	details = input("Enter name, ID, branch, studying year, month, year of completion(seperate data with commas): ")
	img = qrcode.make(details + "," + str(datetime.datetime.today().date()))
	img.save(folName+'/'+details.split(",")[1])
print(f"\nSaved qrcodes with filenames as [ID]")