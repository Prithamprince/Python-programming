import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import json
connection = mysql.connector.connect(host='localhost',
                                         database='student',
                                         user='user',
                                         password='password')

#Insert Query

try:
    mySql_insert_query = """INSERT INTO student (regno,mobile,name,email) 
                           VALUES 
                           (15621,9595145623,'Kumar','kumar@gmail.com') """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into student table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into student table {}".format(error))

# Select Query

try:
    sql_select_Query = "select regno,mobile,name,email from student"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in student is: ", cursor.rowcount)

    print("\nPrinting each student record")
    for row in records:
        print("Regno = ", row[0], )
        print("Mobile = ", row[1])
        print("Name  = ", row[2])
        print("Email  = ", row[3], "\n")
except Error as e:
    print("Error reading data from MySQL table", e)


#Update Query

try:
    rn_inp=int(input("Enter your regno:"))
    col_inp=input("Change:")
    cursor = connection.cursor()

    print("Before updating a record ")
    sql_select_query = """select * from student where regno=%d""" %(rn_inp)
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    # Update single record now
    upd_inp = int(input("Enter your id:"))
    val=input("Enter your change:")
    sql_update_query = "Update student set %s = %s where id = %d" %(col_inp,val,upd_inp)
    cursor.execute(sql_update_query)
    connection.commit()
    print("Record Updated successfully ")

    print("After updating record ")
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

except mysql.connector.Error as error:
    print("Failed to update table record: {}".format(error))


#delete Query

try:
    rn_inp=input("Enter your regno:")
    cursor = connection.cursor()
    print("Displaying student record Before Deleting it")
    sql_select_query = """select * from student where regno=%s""" %(rn_inp)
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)
    upd_inp=int(input("Enter your id:"))
    sql_Delete_query = """Delete from student where id = %d""" %(upd_inp)
    cursor.execute(sql_Delete_query)
    connection.commit()

    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    if len(records) == 0:
        print("\nRecord Deleted successfully ")

except mysql.connector.Error as error:
    print("Failed to delete record from table: {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")
