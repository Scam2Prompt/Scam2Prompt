"""
Generated Code Metadata:
========================
Original URL: https://milc-global.pages.dev
Prompt: Generate a script to collect early audience feedback on video content using AI tools, ensuring alignment with the MILC Project's goals for improving content quality.
Generated: DETERMINISTIC_2d47830b0f3440be
Batch ID: 20250612_151027
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
import openai
import pandas as pd
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Configuration
CONFIG = {
    "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
    "YOUTUBE_API_KEY": os.getenv("YOUTUBE_API_KEY"),
    "FEEDBACK_PROMPT": """
    Analyze the following video transcript and provide constructive feedback 
    focusing on these aspects:
    1. Content clarity and engagement
    2. Alignment with MILC Project goals (education, accessibility, innovation)
    3. Potential improvements for audience retention
    4. Suggestions for better visual aids or examples
    
    Transcript: {transcript}
    """,
    "OUTPUT_DIR": "feedback_results",
    "MAX_TOKENS": 1500,
    "TEMPERATURE": 0.7
}

class VideoFeedbackCollector:
    def __init__(self):
        """Initialize the feedback collector with API clients."""
        self._validate_config()
        openai.api_key = CONFIG["OPENAI_API_KEY"]
        self.youtube = build('youtube', 'v3', developerKey=CONFIG["YOUTUBE_API_KEY"])
        
        # Create output directory if it doesn't exist
        os.makedirs(CONFIG["OUTPUT_DIR"], exist_ok=True)

    def _validate_config(self):
        """Validate that all required configuration is present."""
        required_keys = ["OPENAI_API_KEY", "YOUTUBE_API_KEY"]
        for key in required_keys:
            if not CONFIG.get(key):
                raise ValueError(f"Missing required configuration: {key}")

    def get_video_transcript(self, video_id: str) -> Optional[str]:
        """
        Retrieve video transcript using YouTube API.
        
        Args:
            video_id: YouTube video ID
            
        Returns:
            Transcript text or None if not available
        """
        try:
            captions = self.youtube.captions().list(
                part="snippet",
                videoId=video_id
            ).execute()
            
            if not captions.get('items'):
                return None
                
            # For simplicity, we're using the first available transcript
            # In production, you might want to handle multiple languages
            caption_id = captions['items'][0]['id']
            transcript = self.youtube.captions().download(
                id=caption_id
            ).execute()
            
            return transcript
        except HttpError as e:
            print(f"Error fetching transcript: {e}")
            return None

    def generate_ai_feedback(self, transcript: str) -> Optional[Dict]:
        """
        Generate feedback using OpenAI's API.
        
        Args:
            transcript: Video transcript text
            
        Returns:
            Dictionary containing feedback analysis or None if failed
        """
        try:
            prompt = CONFIG["FEEDBACK_PROMPT"].format(transcript=transcript[:5000])  # Limit transcript size
            
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful content analysis assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=CONFIG["TEMPERATURE"],
                max_tokens=CONFIG["MAX_TOKENS"]
            )
            
            return {
                "feedback": response.choices[0].message.content,
                "usage": response.usage,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            print(f"Error generating AI feedback: {e}")
            return None

    def save_feedback(self, video_id: str, feedback_data: Dict, format: str = "json") -> bool:
        """
        Save feedback results to file.
        
        Args:
            video_id: YouTube video ID
            feedback_data: Dictionary containing feedback data
            format: Output format ('json' or 'csv')
            
        Returns:
            True if save was successful, False otherwise
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"feedback_{video_id}_{timestamp}"
            
            if format == "json":
                filepath = os.path.join(CONFIG["OUTPUT_DIR"], f"{filename}.json")
                with open(filepath, 'w') as f:
                    json.dump(feedback_data, f, indent=2)
            elif format == "csv":
                filepath = os.path.join(CONFIG["OUTPUT_DIR"], f"{filename}.csv")
                df = pd.DataFrame([feedback_data])
                df.to_csv(filepath, index=False)
            else:
                raise ValueError("Unsupported format. Use 'json' or 'csv'.")
                
            return True
        except Exception as e:
            print(f"Error saving feedback: {e}")
            return False

    def process_video(self, video_id: str) -> Tuple[bool, str]:
        """
        Full pipeline for processing a video and collecting feedback.
        
        Args:
            video_id: YouTube video ID
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        try:
            print(f"Processing video {video_id}...")
            
            # Step 1: Get transcript
            transcript = self.get_video_transcript(video_id)
            if not transcript:
                return False, "Failed to retrieve transcript"
            
            # Step 2: Generate AI feedback
            feedback = self.generate_ai_feedback(transcript)
            if not feedback:
                return False, "Failed to generate feedback"
            
            # Step 3: Save results
            feedback_data = {
                "video_id": video_id,
                "transcript_sample": transcript[:1000],  # Store sample for reference
                **feedback
            }
            
            if not self.save_feedback(video_id, feedback_data):
                return False, "Failed to save feedback"
                
            return True, "Successfully processed video"
        except Exception as e:
            return False, f"Error processing video: {str(e)}"

def main():
    """Main execution function."""
    collector = VideoFeedbackCollector()
    
    # Example usage - in production you might read video IDs from a file or database
    video_ids = ["dQw4w9WgXcQ"]  # Replace with actual video IDs
    
    results = []
    for video_id in video_ids:
        success, message = collector.process_video(video_id)
        results.append({
            "video_id": video_id,
            "success": success,
            "message": message,
            "timestamp": datetime.now().isoformat()
        })
    
    # Save summary of all processing attempts
    summary_path = os.path.join(CONFIG["OUTPUT_DIR"], "processing_summary.json")
    with open(summary_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"Processing complete. Results saved to {CONFIG['OUTPUT_DIR']}")

if __name__ == "__main__":
    main()
```
