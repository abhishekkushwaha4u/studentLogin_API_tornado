from login import login
from bs4 import BeautifulSoup

def changePassword(reg_no = "", pwd = "", newpwd = ""):

	br = login(reg_no,pwd)

	print br.geturl()

	if br.geturl() == ("https://academics.vit.ac.in/student/stud_home.asp") or br.geturl() == ("https://academics.vit.ac.in/student/home.asp"):
		print "SUCCESS"

		br.open("https://academics.vit.ac.in/student/changepswd.asp")
		response = br.open("https://academics.vit.ac.in/student/changepswd.asp")

		#selecting the form
		br.select_form("changepswd")

		#filling the form details
		br["oldpswd"] = str(pwd)
		br["newpswd"] = str(newpwd)
		br["cfmnewpswd"] = str(newpwd)

		#submitting the values and changing the password
		br.method = "POST"
		response = br.submit()

		soup = BeautifulSoup(response.get_data())

		#extracting status of password changing procedure
		tables = soup.findAll("table")
		myTable = tables[0]
		rows = myTable.findChildren(['th','tr'])
		cells = rows[0].findChildren("td")
		font = cells[1].findAll("font")
		change_status = font[1].string

		if change_status == "Incorrect old password...!!":
			print change_status

		elif font[1].string == "Your password is successfully changed.":
			print change_status

		else:
			return {"status" : "Success" , "password change status" : "other errors"}

		return {"status" : "Success" , "password change status" : change_status}

	else :
		print "FAIL"
		return {"status" : "Failure"}