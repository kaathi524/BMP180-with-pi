import time
import requests
import smbus
AC6 = 17251
AC5 = 24907
MC = -11786
MD = 2877
#float T
#float temp

dev_address = 0x77

i2c = smbus.SMBus(1)

while(1):
	time.sleep(0.4)

	i2c.write_byte_data(dev_address, 0xF4 , 0x2E)
	time.sleep(0.005)

	msb =i2c.read_byte_data(dev_address, 0xF6)
#print "msb", msb
	lsb = i2c.read_byte_data(dev_address, 0xF7)
#print "lsb", lsb
	UT= (256*msb) + lsb

#print "UT", UT
	x1= (UT-AC6)*AC5 /32768
#print "x1", x1
	x2=MC *2048/(x1 + MD)
#print "X2", x2
	B5 = x1 + x2
#print "B5", B5
	T= (B5 +8)/16
#print "T", T
	T=float(T)
	temp =(T/10)
	temp=float(temp)
	print "T" ,'%.2f' % temp
	temp =str(temp)
	time1= time.strftime("%H:%M  %p")
	print time1
	url = "http://opendata.fsftn.org/input/vrz4ol0JKLspYLxrOoMatq3qBNVJ?private_key=reyOZAgd4btwqjNP9ZA6tYwYEOZB&temp="+temp+"&time="+time1
	requests.get(url)
	time.sleep(10)
