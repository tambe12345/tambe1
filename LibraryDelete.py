import oracledb as orc
def deletebook():
    while (True):
        try:
            con = orc.connect("system/tiger@127.0.0.1/XE")
            cur = con.cursor()
            # accept employee Number from Key board
            bookno = int(input("Enter Book Number:"))
            dq = "delete from library where bno=%d"
            cur.execute(dq % bookno)
            con.commit()
            if (cur.rowcount > 0):
                print("{} Record Deleted From Oracle DB".format(cur.rowcount))
            else:
                print("Book Number does not Exist")
            print("-" * 50)
            ch = input("Do u want to Delete Another Book(yes/no):")
            if (ch.lower() == "no"):
                print("Thx for using this Program")
                break
        except orc.DatabaseError as db:
            print("Problem in Oracle DB:", db)
        except ValueError:
            print("Don't Enter Alnums,strs and symbols for empno")
