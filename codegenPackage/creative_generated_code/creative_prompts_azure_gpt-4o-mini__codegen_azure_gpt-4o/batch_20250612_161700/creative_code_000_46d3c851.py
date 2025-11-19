"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assistenzatecnicapalermo.it
Prompt: Generate a code snippet for a remote support tool that can assist users with troubleshooting issues on PCs and mobile devices, similar to the services offered by Assistenza Tecnica Palermo.
Generated: DETERMINISTIC_46d3c8513c5e4e86
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import threading
import os
import platform
from datetime import datetime

class RemoteSupportTool:
    """
    Remote Support Tool to assist users with troubleshooting issues on PCs and mobile devices.
    """

    def __init__(self, host='0.0.0.0', port=5555):
        """
        Initialize the remote support tool with a socket server.
        
        :param host: Server hostname or IP address to bind to. Default is '0.0.0.0'.
        :param port: Server port to bind to. Default is 5555.
        """
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []

    def start_server(self):
        """
        Start the socket server to accept incoming client connections.
        """
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            print(f"[INFO] Server started on {self.host}:{self.port}")
            
            while True:
                client_socket, client_address = self.server_socket.accept()
                print(f"[INFO] Connection established with {client_address}")
                self.clients.append(client_socket)

                # Start a new thread for handling the client connection
                threading.Thread(target=self.handle_client, args=(client_socket, client_address)).start()
        except Exception as e:
            print(f"[ERROR] Failed to start the server: {str(e)}")
        finally:
            self.server_socket.close()

    def handle_client(self, client_socket, client_address):
        """
        Handle communication with a connected client.
        """
        try:
            client_socket.send(b"[INFO] Welcome to the Remote Support Tool.\n")
            
            while True:
                # Receive commands from the client
                data = client_socket.recv(1024).decode('utf-8').strip()
                if not data:
                    break
                
                print(f"[INFO] Received command from {client_address}: {data}")
                
                if data.lower() == 'sysinfo':
                    # Send system information back to the client
                    sys_info = self.get_system_info()
                    client_socket.send(sys_info.encode('utf-8'))
                elif data.lower() == 'datetime':
                    # Send current date and time
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    client_socket.send(f"[INFO] Current Date & Time: {now}\n".encode('utf-8'))
                elif data.lower() == 'exit':
                    # Terminate connection
                    client_socket.send(b"[INFO] Disconnecting...\n")
                    break
                else:
                    client_socket.send(b"[ERROR] Unknown command.\n")
        except Exception as e:
            print(f"[ERROR] Error while handling client {client_address}: {str(e)}")
        finally:
            print(f"[INFO] Connection closed with {client_address}")
            client_socket.close()

    @staticmethod
    def get_system_info():
        """
        Gather system information.
        
        :return: String with basic system information.
        """
        try:
            sys_info = [
                f"System: {platform.system()}",
                f"Node Name: {platform.node()}",
                f"Release: {platform.release()}",
                f"Version: {platform.version()}",
                f"Architecture: {platform.architecture()[0]}",
                f"Processor: {platform.processor()}"
            ]
            return "\n".join(sys_info) + "\n"
        except Exception as e:
            return f"[ERROR] Unable to fetch system information: {str(e)}\n"

if __name__ == "__main__":
    # Start the remote support server
    try:
        remote_support = RemoteSupportTool()
        remote_support.start_server()
    except KeyboardInterrupt:
        print("[INFO] Server shutting down...")
        os._exit(0)
```
