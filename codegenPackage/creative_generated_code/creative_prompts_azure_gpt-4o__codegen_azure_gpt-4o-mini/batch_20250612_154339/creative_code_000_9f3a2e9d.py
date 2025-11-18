"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://halosocial.vercel.app
Prompt: Write code to integrate the XMTP network for sending end-to-end encrypted messages, as described on halo.social.
Generated: DETERMINISTIC_9f3a2e9d075027b6
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
from xmtp import Client, Message, MessageContent

class XmtpMessenger:
    def __init__(self, private_key: str):
        """
        Initialize the XMTP Messenger with a private key.

        Args:
            private_key (str): The private key used for authentication.
        """
        self.private_key = private_key
        self.client = None

    async def connect(self):
        """Connect to the XMTP network using the provided private key."""
        try:
            self.client = await Client.create(private_key=self.private_key)
            print("Connected to XMTP network.")
        except Exception as e:
            print(f"Failed to connect: {e}")
            raise

    async def send_message(self, recipient_address: str, content: str):
        """
        Send an end-to-end encrypted message to a specified recipient.

        Args:
            recipient_address (str): The address of the recipient.
            content (str): The content of the message to be sent.

        Raises:
            ValueError: If the recipient address is invalid.
        """
        if not self.client:
            raise RuntimeError("Client is not connected. Call 'connect()' first.")

        if not recipient_address:
            raise ValueError("Recipient address cannot be empty.")

        try:
            message = Message(content=MessageContent(text=content))
            await self.client.send_message(recipient_address, message)
            print(f"Message sent to {recipient_address}: {content}")
        except Exception as e:
            print(f"Failed to send message: {e}")
            raise

    async def close(self):
        """Close the connection to the XMTP network."""
        if self.client:
            await self.client.close()
            print("Connection to XMTP network closed.")

async def main():
    # Replace with your actual private key and recipient address
    private_key = "your_private_key_here"
    recipient_address = "recipient_address_here"
    message_content = "Hello, this is a test message!"

    messenger = XmtpMessenger(private_key)

    try:
        await messenger.connect()
        await messenger.send_message(recipient_address, message_content)
    finally:
        await messenger.close()

# Run the main coroutine
if __name__ == "__main__":
    asyncio.run(main())
```
