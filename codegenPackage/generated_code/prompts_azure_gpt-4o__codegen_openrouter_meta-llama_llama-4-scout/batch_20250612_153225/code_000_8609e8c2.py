"""
Generated Code Metadata:
========================
Original URL: https://trindadetelecom.com.br
Prompt: Write a Python script to calculate internet latency (ping) for online gaming based on server response times, and include recommendations for reducing latency as described by Trindade Telecom.
Generated: DETERMINISTIC_8609e8c292aedcbb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import platform
import subprocess
import statistics

def calculate_latency(host: str) -> float:
    """
    Calculate the internet latency (ping) to a given host.

    Args:
    host (str): The hostname or IP address to ping.

    Returns:
    float: The average latency in milliseconds.
    """

    # Ping command is different for Windows and Unix/Linux
    if platform.system().lower() == 'windows':
        ping_cmd = ['ping', '-n', '4', host]
    else:
        ping_cmd = ['ping', '-c', '4', host]

    try:
        # Execute the ping command
        output = subprocess.check_output(ping_cmd).decode('utf-8')

        # Parse the output to extract the latency values
        latency_values = []
        for line in output.split('\n'):
            if 'time=' in line:
                latency = float(line.split('time=')[1].split('ms')[0])
                latency_values.append(latency)

        # Calculate the average latency
        if latency_values:
            average_latency = statistics.mean(latency_values)
            return average_latency
        else:
            print(f"Failed to retrieve latency values for {host}.")
            return None

    except subprocess.CalledProcessError as e:
        print(f"Error executing ping command: {e}")
        return None

def get_recommendations(latency: float) -> str:
    """
    Provide recommendations for reducing latency based on Trindade Telecom's guidelines.

    Args:
    latency (float): The current latency in milliseconds.

    Returns:
    str: Recommendations for reducing latency.
    """

    if latency is None:
        return ""

    recommendations = ""

    if latency > 100:
        recommendations += " High latency detected. Consider the following:\n"
        recommendations += "  * Use a wired connection instead of Wi-Fi.\n"
        recommendations += "  * Close unnecessary applications and background processes.\n"
        recommendations += "  * Upgrade your internet plan to a faster speed.\n"
        recommendations += "  * Use a gaming VPN or proxy server.\n"
    elif latency > 50:
        recommendations += " Moderate latency detected. Consider the following:\n"
        recommendations += "  * Optimize your router's settings for gaming.\n"
        recommendations += "  * Use Quality of Service (QoS) settings to prioritize gaming traffic.\n"
        recommendations += "  * Consider upgrading your router or modem.\n"
    else:
        recommendations += " Low latency detected. You're good to go!"

    return recommendations

def main():
    host = input("Enter the hostname or IP address to ping: ")
    latency = calculate_latency(host)

    if latency is not None:
        print(f"Average latency to {host}: {latency:.2f} ms")
        print(get_recommendations(latency))

if __name__ == "__main__":
    main()
```
