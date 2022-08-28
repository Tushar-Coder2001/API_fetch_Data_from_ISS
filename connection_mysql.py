#first remove comment from dockerfile...........
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="newuser",   password ="matrix123#", database="iss_data")
mycursor=mydb.cursor()
def ins_mysql(dt,velo,fprint,loc,vis,ts,day,sol_la,sol_lo):
	sql = "INSERT INTO iss_info (Date, Velocity, footprint, location, visibility, time_stamp, daynum, solar_lat, solar_lon) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	val = (dt,velo,fprint,loc,vis,ts,day,sol_la,sol_lo)
	mycursor.execute(sql,val)
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")