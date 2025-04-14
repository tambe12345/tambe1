import oracledb as orc
def viewbook():
    try:
        con = orc.connect("system/tiger@localhost/XE")
        cur = con.cursor()
        sq = "select * from library where bno={}".format(int(input("Enter Book Number to view its Details")))
        cur.execute(sq)
        # get the records
        print("*" * 50)
        record = cur.fetchone()
        if(record==None):
            print("Book Does not Exist")
        else:
            print("Book Number:{}".format(record[0]))
            print("Book Name:{}".format(record[1]))
            print("Book Price:{}".format(record[2]))
            print("Book Publication:{}".format(record[3]))
        print("*" * 50)
    except orc.DatabaseError as db:
        print("Problem in Oracle Data Base:", db)
def viewallbooks():
        try:
            con = orc.connect("system/tiger@localhost/orcl")
            cur = con.cursor()
            sq = "select * from library order by bno"
            cur.execute(sq)
            print("*" * 50)
            for colnames in cur.description:
                print(colnames[0],end="\t")
            print()
            # get the records
            print("*" * 50)
            records = cur.fetchall()
            for record in records:
                for val in record:
                    print(val, end="\t")
                print()
            print("*" * 50)
        except orc.DatabaseError as db:
            print("Problem in Oracle Data Base:", db)

