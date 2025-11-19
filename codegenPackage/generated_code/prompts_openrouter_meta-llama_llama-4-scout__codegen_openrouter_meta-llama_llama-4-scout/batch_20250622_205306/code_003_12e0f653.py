"""
Generated Code Metadata:
========================
Original URL: https://thebase.network
Prompt: Write a basic code snippet to simulate network traffic analysis for a simple network setup.
Generated: DETERMINISTIC_12e0f65309624526
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from dataclasses import dataclass
from enum import Enum
from typing import List

class PacketType(Enum):
    """Packet types for network traffic analysis"""
    TCP = 1
    UDP = 2
    ICMP = 3

@dataclass
class NetworkPacket:
    """Data class to represent a network packet"""
    packet_type: PacketType
    source_ip: str
    destination_ip: str
    packet_size: int

class NetworkTrafficAnalyzer:
    """Simulates network traffic analysis"""

    def __init__(self):
        self.packets = []

    def generate_traffic(self, num_packets: int) -> None:
        """Generate random network traffic"""
        for _ in range(num_packets):
            packet_type = random.choice(list(PacketType))
            source_ip = f"192.168.1.{random.randint(1, 100)}"
            destination_ip = f"192.168.1.{random.randint(1, 100)}"
            packet_size = random.randint(100, 1000)
            packet = NetworkPacket(packet_type, source_ip, destination_ip, packet_size)
            self.packets.append(packet)

    def analyze_traffic(self) -> None:
        """Analyze network traffic and print statistics"""
        if not self.packets:
            print("No packets to analyze")
            return

        tcp_packets = [packet for packet in self.packets if packet.packet_type == PacketType.TCP]
        udp_packets = [packet for packet in self.packets if packet.packet_type == PacketType.UDP]
        icmp_packets = [packet for packet in self.packets if packet.packet_type == PacketType.ICMP]

        print("Network Traffic Analysis:")
        print("---------------------------")
        print(f"Total Packets: {len(self.packets)}")
        print(f"TCP Packets: {len(tcp_packets)}")
        print(f"UDP Packets: {len(udp_packets)}")
        print(f"ICMP Packets: {len(icmp_packets)}")

        print("\nPacket Size Distribution:")
        print("---------------------------")
        for packet in self.packets:
            print(f"Source IP: {packet.source_ip}, Destination IP: {packet.destination_ip}, Packet Size: {packet.packet_size}")

def main() -> None:
    try:
        analyzer = NetworkTrafficAnalyzer()
        analyzer.generate_traffic(10)
        analyzer.analyze_traffic()
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
