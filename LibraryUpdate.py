import oracledb as orc
def updatebook():
	while(True):
		try:
			con=orc.connect("system/tiger@127.0.0.1/XE")
			cur=con.cursor()
			#accept empno,emp new sal and emp new comp name
			bookno=int(input("Enter Book Number for Updating Other details of Book:"))
			pri=float(input("Enter New Price:"))
			pub=input("Enter New Publication:")
			uq="update library set price=%f,publication='%s' where bno=%d"
			cur.execute(uq %(pri,pub,bookno))
			con.commit()
			if(cur.rowcount>0):
				print("{} Book Record Updated in Oracle DB".format(cur.rowcount))
			else:
				print("Book Number does not Exist")
			print("-"*50)
			ch=input("Do u want to Update Another Book(yes/no):")
			if(ch.lower()=="no"):
				print("Thx for using this Program")
				break
		except orc.DatabaseError as db:
					print("Problem in Oracle DB:",db)
		except ValueError:
					print("Don't Enter Alnums,strs and symbols for Book No and Price")


