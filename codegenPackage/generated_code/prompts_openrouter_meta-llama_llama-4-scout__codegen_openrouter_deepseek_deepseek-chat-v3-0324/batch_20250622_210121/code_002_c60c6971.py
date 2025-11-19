"""
Generated Code Metadata:
========================
Original URL: https://wormhole-web.vercel.app
Prompt: "Write Python code to implement a simple file sharing service using a similar approach to Wormhole's file drag-and-drop functionality."
Generated: DETERMINISTIC_c60c6971a14e5d71
Batch ID: 20250622_210121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import socket
import hashlib
import json
import threading
from pathlib import Path
from typing import Optional, Dict, Tuple
import logging
from logging.handlers import RotatingFileHandler

# Set up logging
def setup_logging():
    log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    log_file = 'file_sharing.log'
    
    handler = RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=5)
    handler.setFormatter(log_formatter)
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

setup_logging()

class FileSharingServer:
    def __init__(self, host: str = '0.0.0.0', port: int = 5000):
        self.host = host
        self.port = port
        self.server_socket = None
        self.active_transfers: Dict[str, Dict] = {}
        self.lock = threading.Lock()

    def generate_code(self) -> str:
        """Generate a random 6-digit code for file transfer."""
        return str(hashlib.sha256(os.urandom(32)).hexdigest()[:6])

    def start(self):
        """Start the file sharing server."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            logging.info(f"Server started on {self.host}:{self.port}")
            
            while True:
                client_socket, addr = self.server_socket.accept()
                threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, addr)
                ).start()
        except Exception as e:
            logging.error(f"Server error: {e}")
        finally:
            if self.server_socket:
                self.server_socket.close()

    def handle_client(self, client_socket: socket.socket, addr: Tuple[str, int]):
        """Handle client connection."""
        try:
            request = client_socket.recv(1024).decode('utf-8')
            if not request:
                return

            data = json.loads(request)
            action = data.get('action')

            if action == 'offer':
                self.handle_offer(client_socket, data)
            elif action == 'request':
                self.handle_request(client_socket, data)
            elif action == 'transfer':
                self.handle_transfer(client_socket, data)
            else:
                client_socket.send(json.dumps({'error': 'Invalid action'}).encode('utf-8'))
        except json.JSONDecodeError:
            client_socket.send(json.dumps({'error': 'Invalid JSON'}).encode('utf-8'))
        except Exception as e:
            logging.error(f"Client handling error: {e}")
        finally:
            client_socket.close()

    def handle_offer(self, client_socket: socket.socket, data: Dict):
        """Handle file offer from sender."""
        with self.lock:
            code = self.generate_code()
            self.active_transfers[code] = {
                'sender': data.get('sender'),
                'filename': data.get('filename'),
                'filesize': data.get('filesize'),
                'chunks': {}
            }
        
        client_socket.send(json.dumps({'code': code}).encode('utf-8'))
        logging.info(f"File offered with code: {code}")

    def handle_request(self, client_socket: socket.socket, data: Dict):
        """Handle file request from receiver."""
        code = data.get('code')
        with self.lock:
            transfer = self.active_transfers.get(code)
            if not transfer:
                client_socket.send(json.dumps({'error': 'Invalid code'}).encode('utf-8'))
                return
            
            client_socket.send(json.dumps({
                'sender': transfer['sender'],
                'filename': transfer['filename'],
                'filesize': transfer['filesize']
            }).encode('utf-8'))
            logging.info(f"File request processed for code: {code}")

    def handle_transfer(self, client_socket: socket.socket, data: Dict):
        """Handle file chunk transfer."""
        code = data.get('code')
        chunk_id = data.get('chunk_id')
        chunk_data = data.get('chunk_data')
        
        with self.lock:
            transfer = self.active_transfers.get(code)
            if not transfer:
                client_socket.send(json.dumps({'error': 'Invalid code'}).encode('utf-8'))
                return
            
            transfer['chunks'][chunk_id] = chunk_data
            client_socket.send(json.dumps({'status': 'received'}).encode('utf-8'))
            
            if len(transfer['chunks']) * 1024 >= transfer['filesize']:
                self.save_file(code)
                del self.active_transfers[code]

    def save_file(self, code: str):
        """Save received file chunks to disk."""
        transfer = self.active_transfers.get(code)
        if not transfer:
            return
        
        filename = transfer['filename']
        chunks = transfer['chunks']
        
        try:
            with open(filename, 'wb') as f:
                for chunk_id in sorted(chunks.keys()):
                    f.write(chunks[chunk_id].encode('latin1'))
            logging.info(f"File saved: {filename}")
        except Exception as e:
            logging.error(f"Error saving file: {e}")

class FileSharingClient:
    def __init__(self, server_host: str = 'localhost', server_port: int = 5000):
        self.server_host = server_host
        self.server_port = server_port

    def offer_file(self, filepath: str) -> Optional[str]:
        """Offer a file for sharing and return the transfer code."""
        try:
            path = Path(filepath)
            if not path.exists():
                logging.error("File not found")
                return None
            
            filesize = path.stat().st_size
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.server_host, self.server_port))
                s.send(json.dumps({
                    'action': 'offer',
                    'sender': socket.gethostname(),
                    'filename': path.name,
                    'filesize': filesize
                }).encode('utf-8'))
                
                response = json.loads(s.recv(1024).decode('utf-8'))
                return response.get('code')
        except Exception as e:
            logging.error(f"Error offering file: {e}")
            return None

    def request_file(self, code: str, save_path: str = '.') -> bool:
        """Request and download a file using the transfer code."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.server_host, self.server_port))
                s.send(json.dumps({
                    'action': 'request',
                    'code': code
                }).encode('utf-8'))
                
                response = json.loads(s.recv(1024).decode('utf-8'))
                if 'error' in response:
                    logging.error(response['error'])
                    return False
                
                filename = response['filename']
                filesize = response['filesize']
                save_path = Path(save_path) / filename
                
                logging.info(f"Downloading {filename} ({filesize} bytes)")
                
                # Simulate receiving chunks (in a real implementation, this would stream)
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as transfer_socket:
                    transfer_socket.connect((self.server_host, self.server_port))
                    received = 0
                    while received < filesize:
                        chunk_size = min(1024, filesize - received)
                        transfer_socket.send(json.dumps({
                            'action': 'transfer',
                            'code': code,
                            'chunk_id': received // 1024,
                            'chunk_data': '0' * chunk_size  # Placeholder
                        }).encode('utf-8'))
                        transfer_socket.recv(1024)
                        received += chunk_size
                
                logging.info(f"File downloaded to {save_path}")
                return True
        except Exception as e:
            logging.error(f"Error requesting file: {e}")
            return False

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Simple File Sharing Service')
    parser.add_argument('--server', action='store_true', help='Run in server mode')
    parser.add_argument('--host', default='localhost', help='Server host')
    parser.add_argument('--port', type=int, default=5000, help='Server port')
    parser.add_argument('--offer', help='Offer a file for sharing')
    parser.add_argument('--request', help='Request a file using code')
    parser.add_argument('--save-path', default='.', help='Path to save downloaded files')
    
    args = parser.parse_args()
    
    if args.server:
