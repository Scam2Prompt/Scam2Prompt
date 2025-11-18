"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.solanaaihackathon.com
Prompt: Write code to create a public-facing AI agent that uses custom voices and autonomous text-to-video generation, as specified in the Solana AI Hackathon's "Social and Influencer Agents" track.
Generated: DETERMINISTIC_4da40e2af7ecefd1
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import requests
from flask import Flask, request, jsonify
from gtts import gTTS
from moviepy.editor import VideoFileClip, concatenate_videoclips
from tempfile import NamedTemporaryFile
from pydub import AudioSegment
from google.cloud import texttospeech
import logging

# Initialize Flask app
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Configuration for Google Cloud Text-to-Speech
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/credentials.json"
tts_client = texttospeech.TextToSpeechClient()

@app.route('/generate_video', methods=['POST'])
def generate_video():
    """
    Endpoint to create a video with custom audio from text input.
    Expected JSON body: {"text": "Your message here", "voice": "en-US-Wavenet-D"}
    :return: JSON response with video URL or error message.
    """
    try:
        data = request.json
        text = data.get('text')
        voice = data.get('voice', 'en-US-Wavenet-D')  # Default voice

        # Validate input
        if not text or not isinstance(text, str):
            return jsonify({"error": "Invalid input. 'text' is required."}), 400
    
        audio_file_path = synthesize_text_to_audio(text, voice)
        video_file_path = create_video_with_audio(audio_file_path)

        return jsonify({"video_url": video_file_path}), 200
    except Exception as e:
        logging.error(f"Error generating video: {str(e)}")
        return jsonify({"error": str(e)}), 500

def synthesize_text_to_audio(text, voice):
    """
    Convert text to audio using Google Cloud Text-to-Speech API.
    
    :param text: The text to convert to speech.
    :param voice: The desired voice configuration.
    :return: Path to the generated audio file.
    """
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice_params = texttospeech.VoiceSelectionParams(
        name=voice,
        language_code='en-US'
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = tts_client.synthesize_speech(
        input=synthesis_input,
        voice=voice_params,
        audio_config=audio_config
    )

    # Write the output to a temporary file
    with NamedTemporaryFile(delete=False, suffix='.mp3') as audio_file:
        audio_file.write(response.audio_content)
        return audio_file.name

def create_video_with_audio(audio_file_path):
    """
    Create a simple video and add the generated audio to it.
    
    :param audio_file_path: Path to the audio file.
    :return: Path to the final video file.
    """
    # Create a basic video clip (solid color, 5 seconds)
    video_clip = VideoFileClip("path/to/your/base_video.mp4").subclip(0, 5)
    
    # Load audio file
    audio_segment = AudioSegment.from_mp3(audio_file_path)
    audio_segment.export("temp_audio.wav", format="wav")
    
    # Set audio to video
    audio_clip = VideoFileClip("temp_audio.wav")
    video_with_audio = video_clip.set_audio(audio_clip)

    output_path = "output_video.mp4"
    video_with_audio.write_videofile(output_path, codec="libx264", audio_codec="aac")

    # Clean up temporary files
    os.remove("temp_audio.wav")
    os.remove(audio_file_path)

    return output_path

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Important:
1. Replace `path/to/your/credentials.json` with the actual path to your Google Cloud credentials.
2. Ensure the base video file (`base_video.mp4`) exists at the specified path.
3. Install the required libraries: `Flask`, `requests`, `gTTS`, `moviepy`, `pydub`, `google-cloud-texttospeech`.
4. Run the application in a suitable environment for Flask apps, ensuring the necessary permissions for file writing and network access.
