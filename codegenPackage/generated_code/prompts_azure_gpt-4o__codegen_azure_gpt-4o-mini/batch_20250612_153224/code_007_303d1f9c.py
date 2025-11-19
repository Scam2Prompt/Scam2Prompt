"""
Generated Code Metadata:
========================
Original URL: https://www.mooveweb.com
Prompt: Write code to generate dynamic video ads using a library suitable for a marketing agency specializing in audiovisual production, like MoOve Marketing.
Generated: DETERMINISTIC_303d1f9cee1adeae
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import random
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

class VideoAdGenerator:
    def __init__(self, video_template_path, output_directory):
        """
        Initializes the VideoAdGenerator with a video template and output directory.

        :param video_template_path: Path to the video template file.
        :param output_directory: Directory where the generated video ads will be saved.
        """
        self.video_template_path = video_template_path
        self.output_directory = output_directory

        # Ensure output directory exists
        os.makedirs(self.output_directory, exist_ok=True)

    def generate_ad(self, ad_text, duration=5):
        """
        Generates a dynamic video ad with the specified text.

        :param ad_text: The text to display in the video ad.
        :param duration: Duration of the video ad in seconds.
        :return: Path to the generated video ad.
        """
        try:
            # Load the video template
            video_clip = VideoFileClip(self.video_template_path).subclip(0, duration)

            # Create a text clip
            text_clip = TextClip(ad_text, fontsize=70, color='white', bg_color='black', size=video_clip.size)
            text_clip = text_clip.set_position('center').set_duration(duration)

            # Combine video and text clips
            final_clip = CompositeVideoClip([video_clip, text_clip])

            # Generate output file path
            output_file_path = os.path.join(self.output_directory, f"ad_{random.randint(1000, 9999)}.mp4")

            # Write the result to a file
            final_clip.write_videofile(output_file_path, codec='libx264', fps=24)

            return output_file_path

        except Exception as e:
            print(f"Error generating video ad: {e}")
            return None

if __name__ == "__main__":
    # Example usage
    video_template = "path/to/video_template.mp4"  # Replace with your video template path
    output_dir = "output_ads"  # Directory to save generated ads

    ad_generator = VideoAdGenerator(video_template, output_dir)
    ad_text = "Your Dynamic Ad Text Here"
    generated_ad_path = ad_generator.generate_ad(ad_text)

    if generated_ad_path:
        print(f"Video ad generated successfully: {generated_ad_path}")
    else:
        print("Failed to generate video ad.")
```

**Note:** Ensure you have the `moviepy` library installed in your Python environment. You can install it using pip:

```bash
pip install moviepy
```
