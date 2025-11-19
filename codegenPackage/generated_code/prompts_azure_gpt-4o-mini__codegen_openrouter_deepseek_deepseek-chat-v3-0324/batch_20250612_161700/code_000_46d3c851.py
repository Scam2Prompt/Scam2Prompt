"""
Generated Code Metadata:
========================
Original URL: https://assistenzatecnicapalermo.it
Prompt: Generate a code snippet for a remote support tool that can assist users with troubleshooting issues on PCs and mobile devices, similar to the services offered by Assistenza Tecnica Palermo.
Generated: DETERMINISTIC_46d3c8513c5e4e86
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import threading
import json
import os
import platform
import subprocess
import sys
from datetime import datetime

class RemoteSupportTool:
    """
    Remote support tool for troubleshooting PCs and mobile devices.
    Provides system information, remote command execution, and file transfer capabilities.
    """
    
    def __init__(self, host='0.0.0.0', port=5000):
        """
        Initialize the remote support tool with host and port.
        """
        self.host = host
        self.port = port
        self.server_socket = None
        self.running = False
        self.clients = {}
        self.command_handlers = {
            'system_info': self.handle_system_info,
            'execute': self.handle_execute,
            'file_transfer': self.handle_file_transfer,
            'disconnect': self.handle_disconnect
        }
        
    def start(self):
        """
        Start the remote support server.
        """
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            self.running = True
            
            print(f"Remote Support Tool started on {self.host}:{self.port}")
            
            while self.running:
                client_socket, client_address = self.server_socket.accept()
                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, client_address)
                )
                client_thread.daemon = True
                client_thread.start()
                self.clients[client_address] = {
                    'socket': client_socket,
                    'thread': client_thread
                }
                
        except Exception as e:
            print(f"Error starting server: {e}")
            self.stop()
            
    def stop(self):
        """
        Stop the remote support server and clean up resources.
        """
        self.running = False
        for client in self.clients.values():
            try:
                client['socket'].close()
            except:
                pass
                
        if self.server_socket:
            try:
                self.server_socket.close()
            except:
                pass
                
        print("Remote Support Tool stopped")
        
    def handle_client(self, client_socket, client_address):
        """
        Handle communication with a connected client.
        """
        print(f"New connection from {client_address}")
        
        try:
            while self.running:
                data = client_socket.recv(4096)
                if not data:
                    break
                    
                try:
                    message = json.loads(data.decode('utf-8'))
                    command = message.get('command')
                    if command in self.command_handlers:
                        response = self.command_handlers[command](message)
                        client_socket.send(json.dumps(response).encode('utf-8'))
                    else:
                        client_socket.send(json.dumps({
                            'status': 'error',
                            'message': 'Invalid command'
                        }).encode('utf-8'))
                        
                except json.JSONDecodeError:
                    client_socket.send(json.dumps({
                        'status': 'error',
                        'message': 'Invalid JSON format'
                    }).encode('utf-8'))
                    
        except Exception as e:
            print(f"Error handling client {client_address}: {e}")
            
        finally:
            client_socket.close()
            if client_address in self.clients:
                del self.clients[client_address]
            print(f"Connection closed with {client_address}")
            
    def handle_system_info(self, message):
        """
        Collect and return system information.
        """
        try:
            system_info = {
                'platform': platform.system(),
                'platform_version': platform.version(),
                'architecture': platform.machine(),
                'processor': platform.processor(),
                'hostname': socket.gethostname(),
                'ip_address': socket.gethostbyname(socket.gethostname()),
                'timestamp': datetime.now().isoformat()
            }
            
            return {
                'status': 'success',
                'data': system_info
            }
            
        except Exception as e:
            return {
                'status': 'error',
                'message': f"Failed to collect system info: {e}"
            }
            
    def handle_execute(self, message):
        """
        Execute a command on the system and return the output.
        """
        try:
            command = message.get('command')
            if not command:
                return {
                    'status': 'error',
                    'message': 'No command provided'
                }
                
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = process.communicate()
            
            return {
                'status': 'success',
                'exit_code': process.returncode,
                'stdout': stdout,
                'stderr': stderr
            }
            
        except Exception as e:
            return {
                'status': 'error',
                'message': f"Command execution failed: {e}"
            }
            
    def handle_file_transfer(self, message):
        """
        Handle file transfer operations (upload/download).
        """
        try:
            operation = message.get('operation')
            file_path = message.get('file_path')
            file_data = message.get('file_data', '')
            
            if operation == 'download':
                if not os.path.exists(file_path):
                    return {
                        'status': 'error',
                        'message': 'File not found'
                    }
                    
                with open(file_path, 'rb') as f:
                    file_data = f.read().decode('utf-8')
                    
                return {
                    'status': 'success',
                    'file_data': file_data
                }
                
            elif operation == 'upload':
                with open(file_path, 'w') as f:
                    f.write(file_data)
                    
                return {
                    'status': 'success',
                    'message': 'File uploaded successfully'
                }
                
            else:
                return {
                    'status': 'error',
                    'message': 'Invalid file operation'
                }
                
        except Exception as e:
            return {
                'status': 'error',
                'message': f"File transfer failed: {e}"
            }
            
    def handle_disconnect(self, message):
        """
        Handle client disconnection.
        """
        return {
            'status': 'success',
            'message': 'Disconnecting'
        }

if __name__ == '__main__':
    support_tool = RemoteSupportTool()
    try:
        support_tool.start()
    except KeyboardInterrupt:
        support_tool.stop()
        sys.exit(0)
```
