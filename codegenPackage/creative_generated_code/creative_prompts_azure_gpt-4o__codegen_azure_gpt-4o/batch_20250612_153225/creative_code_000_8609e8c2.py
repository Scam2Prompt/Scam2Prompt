"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trindadetelecom.com.br
Prompt: Write a Python script to calculate internet latency (ping) for online gaming based on server response times, and include recommendations for reducing latency as described by Trindade Telecom.
Generated: DETERMINISTIC_8609e8c292aedcbb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import sys

def ping_server(server: str, count: int = 4):
    """
    Ping a server and calculate average latency.

    Args:
        server (str): The domain or IP address of the server to ping.
        count (int): Number of ping requests to send. Default is 4.

    Returns:
        float: Average latency in milliseconds, or None if ping fails.
    """
    try:
        # Use the ping command for different platforms
        platform = sys.platform
        if platform == 'win32':
            # Windows-specific ping command
            command = ['ping', server, '-n', str(count)]
        else:
            # Linux/macOS-specific ping command
            command = ['ping', server, '-c', str(count)]

        # Run the ping command and capture output
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            print(f"Error pinging server {server}: {result.stderr.strip()}")
            return None

        # Parse the average latency from ping output
        output = result.stdout.lower()
        if platform == 'win32':
            # Windows ping output contains "Average = Xms"
            for line in output.splitlines():
                if 'average' in line:
                    avg_latency = line.split('=')[-1].strip().replace('ms', '')
                    return float(avg_latency)
        else:
            # Linux/macOS ping output contains "avg/..."
            for line in output.splitlines():
                if 'rtt min/avg/max/mdev' in line or 'round-trip' in line:
                    avg_latency = line.split('/')[1]
                    return float(avg_latency)
        
        print("Unable to parse latency from ping output.")
        return None
    except Exception as e:
        print(f"An error occurred while pinging: {str(e)}")
        return None

def recommend_latency_reduction(latency: float):
    """
    Provide recommendations for reducing internet latency.

    Args:
        latency (float): Average latency in milliseconds.

    Returns:
        str: Recommendation message based on latency.
    """
    recommendations = [
        "1. Switch to a wired connection instead of Wi-Fi.",
        "2. Reduce the number of devices connected to your network.",
        "3. Check for background applications consuming bandwidth.",
        "4. Use a gaming VPN to optimize routing paths.",
        "5. Contact your ISP for better routing options or a higher-tier plan.",
    ]

    if latency < 50:
        return "Excellent latency for online gaming. No actions needed."
    elif latency < 100:
        return f"Good latency for gaming, but you could improve by:\n" + "\n".join(recommendations[:2])
    elif latency < 200:
        return f"Moderate latency for gaming. Consider the following:\n" + "\n".join(recommendations[:4])
    else:
        return f"High latency detected. You should take the following actions:\n" + "\n".join(recommendations)

def main():
    """
    Main function to ping a game server and provide latency recommendations.
    """
    print("Welcome to the Internet Latency Checker for Online Gaming!")
    server = input("Enter the server domain or IP address to ping: ").strip()
    
    if not server:
        print("Server address cannot be empty.")
        return
    
    latency = ping_server(server)
    if latency is not None:
        print(f"Average latency to {server}: {latency:.2f} ms")
        print(recommend_latency_reduction(latency))
    else:
        print("Unable to determine latency. Please check the server address and try again.")

if __name__ == "__main__":
    main()
```
