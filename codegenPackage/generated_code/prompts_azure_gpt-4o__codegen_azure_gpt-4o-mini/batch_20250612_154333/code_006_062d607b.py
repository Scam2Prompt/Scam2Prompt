"""
Generated Code Metadata:
========================
Original URL: https://ferramentaspremimum.shop
Prompt: Develop a script that automates the generation of captions for videos edited in CapCut Pro using ChatGPT's AI capabilities.
Generated: DETERMINISTIC_062d607b8877942d
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openai
import os
import json
import moviepy.editor as mp

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_captions(video_path, output_path, model="gpt-3.5-turbo", max_tokens=150):
    """
    Generate captions for a video using OpenAI's GPT model.

    Parameters:
    - video_path (str): Path to the input video file.
    - output_path (str): Path to save the generated captions.
    - model (str): The OpenAI model to use for caption generation.
    - max_tokens (int): Maximum number of tokens to generate.

    Returns:
    - None
    """
    try:
        # Load the video
        video = mp.VideoFileClip(video_path)
        duration = video.duration

        # Generate a prompt based on the video's duration
        prompt = f"Generate captions for a video of duration {duration} seconds."

        # Call OpenAI API to generate captions
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens
        )

        # Extract the generated captions from the response
        captions = response['choices'][0]['message']['content']

        # Save captions to the output file
        with open(output_path, 'w') as f:
            f.write(captions)

        print(f"Captions generated and saved to {output_path}")

    except FileNotFoundError:
        print(f"Error: The video file '{video_path}' was not found.")
    except openai.error.OpenAIError as e:
        print(f"OpenAI API error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    video_file = "input_video.mp4"  # Replace with your video file path
    captions_file = "captions.txt"    # Output file for captions

    generate_captions(video_file, captions_file)
```
