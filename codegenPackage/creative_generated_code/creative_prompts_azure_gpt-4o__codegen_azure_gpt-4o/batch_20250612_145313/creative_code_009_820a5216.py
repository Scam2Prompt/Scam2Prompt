"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://discordapp.ir
Prompt: Develop code to create a secure chat room with customizable rules and access levels, as outlined on Discordapp.ir.
Generated: DETERMINISTIC_820a52164968ab73
Batch ID: 20250612_145313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
import hashlib
import secrets
from aiohttp import web
import json

# ===========================
# Constants and Configuration
# ===========================

# Server configuration
HOST = '127.0.0.1'
PORT = 8080

# Access levels
ACCESS_LEVELS = {
    "admin": 3,
    "moderator": 2,
    "user": 1,
    "guest": 0
}

# ===========================
# Utility Functions
# ===========================

def hash_password(password):
    """
    Securely hash a password using SHA-256.
    """
    return hashlib.sha256(password.encode()).hexdigest()

async def broadcast_message(message, clients):
    """
    Send a message to all connected clients.
    """
    for client in clients:
        try:
            await client.send_str(message)
        except Exception:
            pass  # Ignore errors for disconnected clients

# ===========================
# Chat Room Class
# ===========================

class ChatRoom:
    """
    Represents a secure chat room with customizable rules and access levels.
    """
    def __init__(self):
        self.clients = {}  # Mapping of websocket connections to user info
        self.rules = "Be respectful and adhere to the rules."  # Default rules
        self.admin_password = hash_password("admin123")

    def set_rules(self, rules):
        """
        Update chat room rules.
        """
        self.rules = rules

    def authenticate_admin(self, password):
        """
        Authenticate admin based on the provided password.
        """
        return hash_password(password) == self.admin_password

    async def handle_connection(self, request):
        """
        Handle a new WebSocket connection.
        """
        ws = web.WebSocketResponse()
        await ws.prepare(request)

        # On connection, expect user credentials
        await ws.send_str(json.dumps({"type": "info", "message": "Please authenticate with username and access level."}))
        
        try:
            auth_data = await ws.receive_json()
            username = auth_data.get("username")
            access_level = auth_data.get("access_level", "guest")

            if access_level not in ACCESS_LEVELS:
                await ws.send_str(json.dumps({"type": "error", "message": "Invalid access level."}))
                await ws.close()
                return ws

            self.clients[ws] = {"username": username, "access_level": access_level}
            await self.notify_user_joined(username)

            # Main loop for the user's chat session
            async for msg in ws:
                if msg.type == web.WSMsgType.TEXT:
                    data = json.loads(msg.data)

                    # Handle rule updates (admin-only)
                    if data.get("command") == "set_rules":
                        if ACCESS_LEVELS[access_level] < ACCESS_LEVELS["admin"]:
                            await ws.send_str(json.dumps({"type": "error", "message": "Unauthorized to set rules."}))
                        else:
                            new_rules = data.get("rules")
                            self.set_rules(new_rules)
                            await self.notify_rules_updated()

                    # Broadcast other messages
                    else:
                        broadcast_data = {
                            "type": "message",
                            "username": username,
                            "message": data.get("message", "")
                        }
                        await broadcast_message(json.dumps(broadcast_data), self.clients.keys())
                
                elif msg.type == web.WSMsgType.ERROR:
                    print(f"WebSocket connection closed with exception: {ws.exception()}")
                    break

        finally:
            # Clean up after client disconnects
            if ws in self.clients:
                user_info = self.clients.pop(ws)
                await self.notify_user_left(user_info["username"])

        return ws

    async def notify_user_joined(self, username):
        """
        Notify all clients when a user joins.
        """
        join_message = json.dumps({"type": "info", "message": f"{username} has joined the chat."})
        await broadcast_message(join_message, self.clients.keys())

    async def notify_user_left(self, username):
        """
        Notify all clients when a user leaves.
        """
        leave_message = json.dumps({"type": "info", "message": f"{username} has left the chat."})
        await broadcast_message(leave_message, self.clients.keys())

    async def notify_rules_updated(self):
        """
        Notify all clients when the chat room rules are updated.
        """
        rules_message = json.dumps({"type": "info", "message": f"Chat room rules updated: {self.rules}"})
        await broadcast_message(rules_message, self.clients.keys())

# ===========================
# Server Setup
# ===========================

async def init_app():
    """
    Initialize and configure the aiohttp web application.
    """
    app = web.Application()
    chat_room = ChatRoom()

    # WebSocket route
    app.router.add_get('/ws', chat_room.handle_connection)

    return app

# ===========================
# Main Entry Point
# ===========================

if __name__ == '__main__':
    app = asyncio.run(init_app())
    web.run_app(app, host=HOST, port=PORT)
```
