"""
Generated Code Metadata:
========================
Original URL: https://cpanel.solanaaihackathon.com
Prompt: Write code to create a public-facing AI agent that uses custom voices and autonomous text-to-video generation, as specified in the Solana AI Hackathon's "Social and Influencer Agents" track.
Generated: DETERMINISTIC_4da40e2af7ecefd1
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import time
import requests
from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
from elevenlabs import generate, play, set_api_key
from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_videoclips
import openai
from solana.rpc.api import Client
from solana.publickey import PublicKey
from solana.keypair import Keypair
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'mp3', 'wav'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

# API Keys
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
SOLANA_RPC_URL = os.getenv('SOLANA_RPC_URL')
WALLET_PRIVATE_KEY = os.getenv('WALLET_PRIVATE_KEY')

# Initialize APIs
set_api_key(ELEVENLABS_API_KEY)
openai.api_key = OPENAI_API_KEY
solana_client = Client(SOLANA_RPC_URL)

# Voice configuration
VOICE_CONFIG = {
    "default": {
        "voice_id": "EXAVITQu4vr4xnSDxMaL",
        "stability": 0.75,
        "similarity_boost": 0.75
    }
}

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def generate_voice(text, voice_config=None):
    """Generate voice audio from text using ElevenLabs API"""
    if voice_config is None:
        voice_config = VOICE_CONFIG["default"]
    
    try:
        audio = generate(
            text=text,
            voice=voice_config["voice_id"],
            model="eleven_monolingual_v1",
            stability=voice_config["stability"],
            similarity_boost=voice_config["similarity_boost"]
        )
        return audio
    except Exception as e:
        raise Exception(f"Voice generation failed: {str(e)}")

def generate_text(prompt):
    """Generate text using OpenAI API"""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        raise Exception(f"Text generation failed: {str(e)}")

def create_video(images, audio_path, output_path):
    """Create video from images and audio"""
    try:
        # Create image sequence clip
        clip = ImageSequenceClip(images, fps=24)
        
        # Add audio
        audio_clip = AudioFileClip(audio_path)
        final_clip = clip.set_audio(audio_clip)
        
        # Write video file
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
        return output_path
    except Exception as e:
        raise Exception(f"Video creation failed: {str(e)}")

def process_payment(sender_wallet, recipient_wallet, amount):
    """Process payment on Solana blockchain"""
    try:
        sender_keypair = Keypair.from_secret_key(bytes.fromhex(sender_wallet))
        recipient_pubkey = PublicKey(recipient_wallet)
        
        transaction = Transaction().add(
            transfer(
                TransferParams(
                    from_pubkey=sender_keypair.public_key,
                    to_pubkey=recipient_pubkey,
                    lamports=int(amount * 10**9)  # Convert SOL to lamports
                )
            )
        )
        
        # Send transaction
        result = solana_client.send_transaction(transaction, sender_keypair)
        return result["result"]
    except Exception as e:
        raise Exception(f"Payment processing failed: {str(e)}")

@app.route('/generate-content', methods=['POST'])
def generate_content():
    """Endpoint to generate AI content (text, voice, video)"""
    try:
        data = request.json
        if not data or 'prompt' not in data:
            return jsonify({"error": "Prompt is required"}), 400
        
        # Generate text
        generated_text = generate_text(data['prompt'])
        
        # Generate voice
        voice_config = data.get('voice_config', VOICE_CONFIG["default"])
        audio = generate_voice(generated_text, voice_config)
        
        # Save audio temporarily
        audio_path = os.path.join(app.config['UPLOAD_FOLDER'], f"audio_{int(time.time())}.mp3")
        with open(audio_path, 'wb') as f:
            f.write(audio)
        
        # Generate video (placeholder for actual implementation)
        # In production, you would use actual images from your content generation pipeline
        images = [os.path.join('assets', 'placeholder.jpg')]  # Replace with actual images
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], f"video_{int(time.time())}.mp4")
        create_video(images, audio_path, video_path)
        
        # Clean up temporary files
        os.remove(audio_path)
        
        return send_file(video_path, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/process-payment', methods=['POST'])
def handle_payment():
    """Endpoint to process payments on Solana"""
    try:
        data = request.json
        if not data or 'recipient' not in data or 'amount' not in data:
            return jsonify({"error": "Recipient and amount are required"}), 400
        
        tx_hash = process_payment(WALLET_PRIVATE_KEY, data['recipient'], float(data['amount']))
        return jsonify({"transaction_hash": tx_hash})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=os.getenv('DEBUG', 'False') == 'True')
```
