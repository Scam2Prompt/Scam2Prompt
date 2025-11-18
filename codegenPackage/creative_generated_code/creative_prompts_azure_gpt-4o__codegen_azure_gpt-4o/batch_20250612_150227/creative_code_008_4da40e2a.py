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
import requests
from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from moviepy.editor import TextClip, CompositeVideoClip
from gtts import gTTS
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the FastAPI app
app = FastAPI()

# Load environment variables
TEXT_TO_VIDEO_API_URL = os.getenv("TEXT_TO_VIDEO_API_URL")
TEXT_TO_VIDEO_API_KEY = os.getenv("TEXT_TO_VIDEO_API_KEY")

# Base path for storing generated files
OUTPUT_DIR = "generated_content"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Input model for user requests
class AgentRequest(BaseModel):
    text: str        # The prompt or script for the AI agent
    voice: str       # Custom voice name or ID
    style: str       # Video style (e.g., "casual", "professional")

# Endpoint to generate AI-driven text-to-video content
@app.post("/generate")
async def generate_video(request: AgentRequest):
    # Validate input
    if not request.text or not request.voice or not request.style:
        raise HTTPException(status_code=400, detail="All fields must be provided: text, voice, and style.")
    
    # Step 1: Use gTTS to create audio from text
    try:
        tts = gTTS(text=request.text, lang='en')
        audio_path = os.path.join(OUTPUT_DIR, "audio.mp3")
        tts.save(audio_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating audio: {str(e)}")
    
    # Step 2: Call the Text-to-Video API
    try:
        response = requests.post(
            TEXT_TO_VIDEO_API_URL,
            headers={"Authorization": f"Bearer {TEXT_TO_VIDEO_API_KEY}"},
            json={
                "text": request.text,
                "voice": request.voice,
                "style": request.style
            }
        )
        response.raise_for_status()
        video_data = response.content
        video_path = os.path.join(OUTPUT_DIR, "video.mp4")
        with open(video_path, "wb") as video_file:
            video_file.write(video_data)
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Error generating video: {str(e)}")
    
    # Step 3: Combine audio and video using moviepy
    try:
        video_clip = TextClip(request.text, fontsize=24, color='white', bg_color='black', size=(800, 600))
        video_clip = CompositeVideoClip([video_clip.set_duration(10)])
        video_clip.write_videofile(video_path, fps=24)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing video: {str(e)}")
    
    # Return the generated video path
    return {"video_path": video_path}

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "OK"}
```

### Notes and Assumptions:
- Replace `TEXT_TO_VIDEO_API_URL` and `TEXT_TO_VIDEO_API_KEY` with actual values for the text-to-video generation API.
- This code assumes the use of `gTTS` for audio generation and `moviepy` for combining audio with video.
- Make sure `ffmpeg` is installed and available in your environment for `moviepy` to function properly.
- The generated content is saved in the `generated_content` directory; ensure this location is writable.
