import oracledb as orc
def addbook():
    while(True):
        try:
            con=orc.connect("system/tiger@localhost/XE")
            cur=con.cursor()
            #Accept Book Details from KBD
            print("---------------------------------------------")
            bno=int(input("Enter Book Number:"))
            bname=input("Enter Book Name:")
            price=float(input("Enter Book Price:"))
            pub=input("Enter Publication Name:")
            cur.execute("insert into library values(%d,'%s',%f,'%s')" %(bno,bname,price,pub))
            con.commit()
            print("{} Book Deatils Saved Sucessfully".format(cur.rowcount))
            print("---------------------------------------------")
            ch=input("Do u want to Insert Another Book Deatils(yes/no):")
            if(ch.lower()=="no"):
                print("Thc for this Program")
                break
        except orc.DatabaseError as db:
            print("Problem in Oracle: ",db)
        except ValueError:
            print("Don't enter strs alnums and symbols for book number and price--try again")
