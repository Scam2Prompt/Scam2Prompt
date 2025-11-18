"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridge-berachain.ink
Prompt: Write a script to test the connectivity and response time of Google Public DNS servers (8.8.8.8 and 2001:4860:4860::8844).
Generated: DETERMINISTIC_588b60943ac3fd7a
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import time

def ping_server(server, count=4):
    """
    Pings the specified server and returns the average response time.
    
    Parameters:
    server (str): The IP address or hostname of the server to ping.
    count (int): Number of ping requests to send (default is 4).
    
    Returns:
    float: Average response time in milliseconds, or None if the ping fails.
    """
    try:
        # Construct the ping command depending on the operating system
        command = ['ping', '-c', str(count), server]  # Linux/macOS
        if subprocess.run(['uname'], capture_output=True, text=True).stdout.strip() == 'Windows':
            command = ['ping', '-n', str(count), server]  # Windows
        
        # Execute the ping command
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Failed to ping {server}.")
            return None
        
        # Parse the output to extract average response time
        output = result.stdout
        if 'min/avg/max' in output:  # Linux/macOS
            avg_time = float(output.split('/')[-3])
        elif 'Average =' in output:  # Windows
            avg_time = float(output.split('Average = ')[-1].split('ms')[0])
        else:
            print(f"Unexpected output format for server {server}.")
            return None
        
        return avg_time
    except Exception as e:
        print(f"An error occurred while pinging {server}: {e}")
        return None

def main():
    """
    Main function to test connectivity and response time of Google Public DNS servers.
    """
    servers = [
        "8.8.8.8",  # IPv4 address of Google Public DNS
        "2001:4860:4860::8844"  # IPv6 address of Google Public DNS
    ]
    
    for server in servers:
        print(f"Pinging server: {server}")
        start_time = time.time()
        avg_response_time = ping_server(server)
        elapsed_time = time.time() - start_time
        
        if avg_response_time is not None:
            print(f"Average response time for {server}: {avg_response_time:.2f} ms")
        else:
            print(f"Could not determine response time for {server}.")
        
        print(f"Elapsed time: {elapsed_time:.2f} seconds\n")

if __name__ == "__main__":
    main()
```
