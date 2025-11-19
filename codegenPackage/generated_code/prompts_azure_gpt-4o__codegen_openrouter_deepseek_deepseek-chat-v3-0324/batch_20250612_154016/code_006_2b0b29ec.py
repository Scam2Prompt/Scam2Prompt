"""
Generated Code Metadata:
========================
Original URL: https://fun-virtuals-agent.pages.dev
Prompt: Suggest tools or frameworks to implement a meme generator and music generator for sentient agents, as mentioned in the Fun Virtuals Agent functionalities.
Generated: DETERMINISTIC_2b0b29ecc2fb5f8f
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Required imports
from flask import Flask, request, jsonify, send_file
from PIL import Image, ImageDraw, ImageFont
import textwrap
import random
import os
import uuid
from gtts import gTTS
import pygame
import io

# Initialize Flask app
app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
MEME_FOLDER = 'memes'
AUDIO_FOLDER = 'audio'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(MEME_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Meme Generator Endpoint
@app.route('/generate_meme', methods=['POST'])
def generate_meme():
    try:
        # Check if image file is present
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        
        file = request.files['image']
        
        # Check if file is allowed
        if file.filename == '' or not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type'}), 400
        
        # Get text parameters
        top_text = request.form.get('top_text', '')
        bottom_text = request.form.get('bottom_text', '')
        
        # Save uploaded file temporarily
        temp_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(temp_path)
        
        # Open image and prepare for editing
        img = Image.open(temp_path)
        draw = ImageDraw.Draw(img)
        
        # Get image dimensions
        width, height = img.size
        
        # Load font (using default if not found)
        try:
            font = ImageFont.truetype("impact.ttf", size=int(height/10))
        except:
            font = ImageFont.load_default()
        
        # Process top text
        if top_text:
            lines = textwrap.wrap(top_text, width=20)
            y = 10
            for line in lines:
                text_width, text_height = draw.textsize(line, font=font)
                x = (width - text_width) / 2
                draw.text((x, y), line, font=font, fill="white", stroke_width=2, stroke_fill="black")
                y += text_height
        
        # Process bottom text
        if bottom_text:
            lines = textwrap.wrap(bottom_text, width=20)
            y = height - (len(lines) * 30) - 20
            for line in lines:
                text_width, text_height = draw.textsize(line, font=font)
                x = (width - text_width) / 2
                draw.text((x, y), line, font=font, fill="white", stroke_width=2, stroke_fill="black")
                y += text_height
        
        # Save meme
        meme_filename = f"meme_{uuid.uuid4().hex}.jpg"
        meme_path = os.path.join(MEME_FOLDER, meme_filename)
        img.save(meme_path)
        
        # Clean up temp file
        os.remove(temp_path)
        
        return send_file(meme_path, mimetype='image/jpeg')
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Music Generator Endpoint
@app.route('/generate_music', methods=['POST'])
def generate_music():
    try:
        # Get text input
        text = request.form.get('text', '')
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        # Generate speech from text
        tts = gTTS(text=text, lang='en')
        
        # Save audio file
        audio_filename = f"audio_{uuid.uuid4().hex}.mp3"
        audio_path = os.path.join(AUDIO_FOLDER, audio_filename)
        tts.save(audio_path)
        
        # Initialize pygame mixer
        pygame.mixer.init()
        
        # Play the audio
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
        
        # Return the audio file
        return send_file(audio_path, mimetype='audio/mpeg')
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```
