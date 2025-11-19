"""
Generated Code Metadata:
========================
Original URL: https://cpanel.solanaaihackathon.com
Prompt: Write a Python script to create a meme-generating AI agent that uses Solana's blockchain infrastructure, focusing on humor and creativity, as described in the "Meme Agents" track of the Solana AI Hackathon.
Generated: DETERMINISTIC_7f84260de97b867e
Batch ID: 20250612_150227
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.imgflip.com/caption_image": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.imgflip.com/get_memes": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.mainnet-beta.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
import random
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer

# Constants
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"
MEME_API_URL = "https://api.imgflip.com/get_memes"
FONT_PATH = "arial.ttf"  # Ensure this font is available in your environment
FONT_SIZE = 40

# Initialize Solana client
solana_client = Client(SOLANA_RPC_URL)

def fetch_memes():
    """Fetches a list of memes from the Imgflip API."""
    try:
        response = requests.get(MEME_API_URL)
        response.raise_for_status()
        memes = response.json().get('data', {}).get('memes', [])
        return memes
    except requests.RequestException as e:
        print(f"Error fetching memes: {e}")
        return []

def create_meme(template_id, top_text, bottom_text):
    """Creates a meme image using the specified template and text."""
    meme_url = f"https://api.imgflip.com/caption_image"
    payload = {
        'template_id': template_id,
        'username': 'your_username',  # Replace with your Imgflip username
        'password': 'your_password',  # Replace with your Imgflip password
        'text0': top_text,
        'text1': bottom_text
    }
    
    try:
        response = requests.post(meme_url, data=payload)
        response.raise_for_status()
        meme_image_url = response.json().get('data', {}).get('url')
        return meme_image_url
    except requests.RequestException as e:
        print(f"Error creating meme: {e}")
        return None

def download_image(url):
    """Downloads an image from a URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return Image.open(BytesIO(response.content))
    except requests.RequestException as e:
        print(f"Error downloading image: {e}")
        return None

def add_text_to_image(image, top_text, bottom_text):
    """Adds top and bottom text to the image."""
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    
    # Calculate text size and position
    top_text_size = draw.textsize(top_text, font=font)
    bottom_text_size = draw.textsize(bottom_text, font=font)
    
    # Draw top text
    draw.text(((image.width - top_text_size[0]) / 2, 10), top_text, font=font, fill="white")
    
    # Draw bottom text
    draw.text(((image.width - bottom_text_size[0]) / 2, image.height - bottom_text_size[1] - 10), bottom_text, font=font, fill="white")

def send_solana_transaction(recipient, amount):
    """Sends SOL to a specified recipient on the Solana blockchain."""
    try:
        # Create a transaction
        transaction = Transaction()
        transaction.add(transfer(TransferParams(from_pubkey=solana_client.get_account_info(recipient)['result']['value']['owner']),
                                  to_pubkey=recipient,
                                  lamports=amount))
        
        # Send the transaction
        response = solana_client.send_transaction(transaction, opts=TxOpts(skip_preflight=True))
        return response
    except Exception as e:
        print(f"Error sending transaction: {e}")
        return None

def main():
    """Main function to generate a meme and send SOL."""
    memes = fetch_memes()
    if not memes:
        print("No memes available.")
        return
    
    # Select a random meme
    selected_meme = random.choice(memes)
    meme_template_id = selected_meme['id']
    top_text = "When you code all night"
    bottom_text = "And it finally works!"
    
    # Create the meme
    meme_url = create_meme(meme_template_id, top_text, bottom_text)
    if not meme_url:
        print("Failed to create meme.")
        return
    
    # Download the meme image
    meme_image = download_image(meme_url)
    if not meme_image:
        print("Failed to download meme image.")
        return
    
    # Add text to the image
    add_text_to_image(meme_image, top_text, bottom_text)
    
    # Save the meme image locally
    meme_image.save("meme.png")
    print("Meme created and saved as meme.png")
    
    # Send SOL transaction (example values)
    recipient_address = "recipient_public_key"  # Replace with actual recipient public key
    amount_to_send = 1000000  # Amount in lamports (1 SOL = 1,000,000,000 lamports)
    transaction_response = send_solana_transaction(recipient_address, amount_to_send)
    if transaction_response:
        print(f"Transaction successful: {transaction_response}")

if __name__ == "__main__":
    main()
```

**Note:** Replace `your_username`, `your_password`, and `recipient_public_key` with actual values. Ensure you have the required libraries installed (`requests`, `Pillow`, `solana`).
