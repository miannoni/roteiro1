from socket import *
import time
import os
import platform
import subprocess
from datetime import datetime

def scanHost(IP_alvo, protocol, port_range):

    startTime = time.time()

    dct = {"udp" : SOCK_DGRAM,
            "tcp" : SOCK_STREAM}

    IP = gethostbyname(IP_alvo)
    print ('Starting scan on host: ', IP)

    for port in range(port_range[0], port_range[1]):
      s = socket(AF_INET, dct[protocol])

      conn = s.connect_ex((IP, port))
      try:
          if(conn == 0) :
             print ('%d:%s:%s:OPEN' % (port, getservbyport(port, protocol), protocol.upper()))
      except(OSError):
          pass

      s.close()
    print('Time taken:', time.time() - startTime)

def scanNetwork(end_rede, ping_range, port_range):

    startTime = time.time()
    print ("Scanning in Progress:")

    for ip in range(ping_range[0],ping_range[1] + 1):
       address = ".".join(end_rede.split('.')[0:3]) + "." + str(ip)
       socket_ = socket(AF_INET, SOCK_STREAM)
       setdefaulttimeout(1)

       for port in range(port_range[0], port_range[1]):
           result = socket_.connect_ex((address,port))
           if result == 0:
               print("Live ->", address)
               break

    print('Time taken:', time.time() - startTime)

ip = "172.20.10.2"
prot = "tcp"

scanNetwork(ip, [0, 10], [0, 1050])
scanHost(ip, prot, [0, 2000])


#
