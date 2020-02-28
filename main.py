#!/usr/bin/python
from socket import *
import time
import tkinter
from tkinter import *

top = tkinter.Tk()
var = StringVar()

def print_to_var(string_to_var):
    tmp = var.get()
    var.set(tmp + "\n" + string_to_var)

def reset_var():
    var.set("");

L1 = tkinter.Label(top, text="IP")
L1.pack()
E1 = tkinter.Entry(top, bd =5)
E1.pack()

L2 = tkinter.Label(top, text="Protocolo")
L2.pack()
E2 = tkinter.Entry(top, bd =5)
E2.pack()

L3 = tkinter.Label(top, text="Da porta")
L3.pack()
E3 = tkinter.Entry(top, bd =5)
E3.pack()

L4 = tkinter.Label(top, text="Ate a porta")
L4.pack()
E4 = tkinter.Entry(top, bd =5)
E4.pack()

L5 = tkinter.Label(top, text="\n(So para Scan\nNetwork)\nDo IP")
L5.pack()
E5 = tkinter.Entry(top, bd =5)
E5.pack()

L6 = tkinter.Label(top, text="Ate o IP")
L6.pack()
E6 = tkinter.Entry(top, bd =5)
E6.pack()

L5 = tkinter.Label(top, textvariable=var, relief=RAISED)

def scanHost():
    reset_var()
    IP_alvo = E1.get()
    protocol = E2.get()
    port_range = [0, 0]
    port_range[0] = int(E3.get())
    port_range[1] = int(E4.get())

    startTime = time.time()

    dct = {"udp" : SOCK_DGRAM,
            "tcp" : SOCK_STREAM}

    IP = gethostbyname(IP_alvo)
    print_to_var ('Starting scan on host: ' + str(IP))

    for port in range(port_range[0], port_range[1]):
      s = socket(AF_INET, dct[protocol])

      conn = s.connect_ex((IP, port))
      try:
          if(conn == 0) :
             print_to_var ('%d:%s:%s:OPEN' % (port, getservbyport(port, protocol), protocol.upper()))
      except(OSError):
          pass

      s.close()
    print_to_var('Time taken:' + str(time.time() - startTime))

def scanNetwork():
    reset_var()

    end_rede = E1.get()
    port_range = [0, 0]
    port_range[0] = int(E3.get())
    port_range[1] = int(E4.get())
    ping_range = [0, 0]
    ping_range[0] = int(E5.get())
    ping_range[1] = int(E6.get())

    startTime = time.time()
    print_to_var ("Scanning in Progress:")

    for ip in range(ping_range[0],ping_range[1] + 1):
       address = ".".join(end_rede.split('.')[0:3]) + "." + str(ip)
       socket_ = socket(AF_INET, SOCK_STREAM)
       setdefaulttimeout(1)

       for port in range(port_range[0], port_range[1]):
           result = socket_.connect_ex((address,port))
           if result == 0:
               print_to_var("Live ->" + str(address))
               break

    print_to_var('Time taken:' + str(time.time() - startTime))

B = tkinter.Button(top, text ="Scan Host", command = scanHost)
B.pack()

c = tkinter.Button(top, text ="Scan Network", command = scanNetwork)
c.pack()

L5.pack()

top.mainloop()
