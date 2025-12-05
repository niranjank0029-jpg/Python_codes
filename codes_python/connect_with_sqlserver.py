# print('ss')

import pyodbc

driver_name='sql server' 
server_name='DESKTOP-2O13QKB\SQLEXPRESS'
datebase_name='july2025'

connection_string=f"""
driver={driver_name};server={server_name};database={datebase_name};
trust_connection=yes;
"""
conn=pyodbc.connect(connection_string) 
print(conn)

cursor=conn.cursor()
cursor.execute('select * from employees')
row1=cursor.fetchall()
for row in row1:
    print(row)

print("***********************************************************************")

cursor.execute('select * from exams')
row2=cursor.fetchall()

for row in row2:
    print(row)


#method 1
# row=cursor.fetchone()
# print(row)

# while row:
#     print(row)
#     row=cursor.fetchone()


# #method 2
# # for row in cursor:
# #     print(row)

# #method 3

# # for row in row:
# #     print(row)


 