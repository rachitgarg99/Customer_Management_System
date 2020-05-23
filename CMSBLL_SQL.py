import pickle
import pymysql


class Customer:
    con = pymysql.connect(host="localhost", user="root", password="root", )
    cur = con.cursor()
    cussList = []

    def __init__(self):
        self.id = 0
        self.age = 0
        self.name = 0

    def addCustomer(self):
        # Customer.cussList.append(self)  # Will add the address of the object in cussList List
        # Customer.cur.execute(f"insert into abc.tb1 values({self.id},{self.age},{self.name})")
        try:
            sql = "insert into abc.tb1 values(%s, %s, %s)"
            tuples = (self.id, self.age, self.name)
            Customer.cur.execute(sql, tuples)
            Customer.con.commit()
            return "done"

        except pymysql.Error as e:
            return e

    def searchCustomer(self):
        try:
            Customer.cur.execute(f"select * from abc.tb1 where id={self.id}")
            data = Customer.cur.fetchone()

            self.age = data[1]
            self.name = data[2]

            return f"For ID : {self.id} the details are:\nNAME ---> {self.name}\nAGE ---> {self.age}\n "

        except:
            return "Not Found"

    def deleteCustomer(self):
        try:
            Customer.cur.execute(f"DELETE FROM abc.tb1 where id={self.id}")
            Customer.con.commit()
            return "done"
        except pymysql.Error as e:
            return e

    def modifyCustomer(self):
        try:
            sql = "update abc.tb1 set age = %s , namei = %s where id = %s"
            tuples = (self.age, self.name, self.id)
            Customer.cur.execute(sql, tuples)
            Customer.con.commit()
            return "done"

        except pymysql.Error as e:
            return e

    def displayCustomer(self):
        Customer.cur.execute("select * from abc.tb1")
        return Customer.cur

