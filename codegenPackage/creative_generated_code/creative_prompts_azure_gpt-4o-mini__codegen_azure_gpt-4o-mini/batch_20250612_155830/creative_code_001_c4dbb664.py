"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://segroegg.gitbook.io
Prompt: Write a code snippet to check the eligibility of a machine for joining the Aethir network.
Generated: DETERMINISTIC_c4dbb6647a4658e7
Batch ID: 20250612_155830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Machine:
    def __init__(self, cpu_count, ram_size, disk_space, network_speed):
        """
        Initializes the Machine object with its specifications.

        :param cpu_count: Number of CPU cores
        :param ram_size: RAM size in GB
        :param disk_space: Disk space in GB
        :param network_speed: Network speed in Mbps
        """
        self.cpu_count = cpu_count
        self.ram_size = ram_size
        self.disk_space = disk_space
        self.network_speed = network_speed

    def is_eligible_for_aethir(self):
        """
        Checks if the machine meets the eligibility criteria for joining the Aethir network.

        Eligibility criteria:
        - Minimum 4 CPU cores
        - Minimum 16 GB RAM
        - Minimum 100 GB disk space
        - Minimum 10 Mbps network speed

        :return: True if eligible, False otherwise
        """
        try:
            if self.cpu_count < 4:
                raise ValueError("Insufficient CPU cores. Required: 4, Found: {}".format(self.cpu_count))
            if self.ram_size < 16:
                raise ValueError("Insufficient RAM. Required: 16 GB, Found: {} GB".format(self.ram_size))
            if self.disk_space < 100:
                raise ValueError("Insufficient Disk Space. Required: 100 GB, Found: {} GB".format(self.disk_space))
            if self.network_speed < 10:
                raise ValueError("Insufficient Network Speed. Required: 10 Mbps, Found: {} Mbps".format(self.network_speed))

            return True  # Machine meets all criteria

        except ValueError as e:
            print("Eligibility Check Error: ", e)
            return False  # Machine does not meet criteria


# Example usage
if __name__ == "__main__":
    # Create a Machine object with specifications
    my_machine = Machine(cpu_count=8, ram_size=32, disk_space=200, network_speed=20)

    # Check eligibility for Aethir network
    if my_machine.is_eligible_for_aethir():
        print("The machine is eligible to join the Aethir network.")
    else:
        print("The machine is not eligible to join the Aethir network.")
```
