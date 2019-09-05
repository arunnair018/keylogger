import time
import os
while True:
	if int(time.strftime("%M"))%10 == 0:
		print(time.strftime("%M")+'hello world')
		time.sleep(60)