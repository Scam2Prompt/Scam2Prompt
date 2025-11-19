"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xanade.com
Prompt: Write a Python script that utilizes the ESP32 development board to connect to WiFi and send sensor data to a server.
Generated: DETERMINISTIC_b3f24879b9333c5b
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import network
import socket
import time
import machine
import json

# Constants
SSID = 'your_wifi_ssid'  # Replace with your WiFi SSID
PASSWORD = 'your_wifi_password'  # Replace with your WiFi password
SERVER_IP = 'your_server_ip'  # Replace with your server IP
SERVER_PORT = 80  # Replace with your server port

# Function to connect to WiFi
def connect_to_wifi(ssid, password):
    # Create a WLAN object
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # Connect to the specified WiFi network
    wlan.connect(ssid, password)

    # Wait for the connection to be established
    while not wlan.isconnected():
        print("Connecting to WiFi...")
        time.sleep(1)

    print("Connected to WiFi:", wlan.ifconfig())

# Function to read sensor data
def read_sensor_data():
    # Simulate reading sensor data; replace this with actual sensor code
    sensor_value = machine.ADC(0).read()  # Replace with actual ADC pin number
    return {'sensor_value': sensor_value}

# Function to send data to the server
def send_data_to_server(data):
    # Create a socket
    addr_info = socket.getaddrinfo(SERVER_IP, SERVER_PORT)
    addr = addr_info[0][-1]
    s = socket.socket()

    try:
        # Connect to the server
        s.connect(addr)

        # Prepare the HTTP request
        request = f"POST /data HTTP/1.1\r\nHost: {SERVER_IP}\r\nContent-Type: application/json\r\nContent-Length: {len(data)}\r\n\r\n{data}"
        
        # Send the request
        s.send(request.encode())
        print("Data sent to server.")
    except Exception as e:
        print(f"Error while sending data: {e}")
    finally:
        # Close the socket
        s.close()

# Main function
def main():
    try:
        # Connect to WiFi
        connect_to_wifi(SSID, PASSWORD)

        while True:
            # Read sensor data
            sensor_data = read_sensor_data()

            # Serialize sensor data to JSON format
            json_data = json.dumps(sensor_data)

            # Send data to the server
            send_data_to_server(json_data)

            # Wait for a specified interval before reading the sensor again
            time.sleep(10)  # Adjust the interval as needed
    except KeyboardInterrupt:
        print("Program terminated by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
