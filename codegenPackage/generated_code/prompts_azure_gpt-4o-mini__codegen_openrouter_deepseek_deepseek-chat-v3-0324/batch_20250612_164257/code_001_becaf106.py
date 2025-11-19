"""
Generated Code Metadata:
========================
Original URL: https://masterclicsolutions.com
Prompt: Write a Python script that automates the creation of interactive videos for e-learning courses, as described by MasterClic Solutions.
Generated: DETERMINISTIC_becaf10608ba8c43
Batch ID: 20250612_164257
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
import shutil
from typing import Dict, List, Optional
from pathlib import Path

class InteractiveVideoCreator:
    """
    A class to automate the creation of interactive videos for e-learning courses.
    Handles video processing, adding interactive elements, and generating output.
    """

    def __init__(self, config_path: str = "config.json"):
        """
        Initialize the video creator with configuration.

        Args:
            config_path (str): Path to the configuration JSON file. Defaults to "config.json".
        """
        self.config = self._load_config(config_path)
        self.validate_config()
        self.setup_workspace()

    def _load_config(self, config_path: str) -> Dict:
        """
        Load configuration from a JSON file.

        Args:
            config_path (str): Path to the configuration file.

        Returns:
            Dict: Configuration dictionary.

        Raises:
            FileNotFoundError: If config file is not found.
            json.JSONDecodeError: If config file is not valid JSON.
        """
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in configuration file: {e.msg}", e.doc, e.pos)

    def validate_config(self) -> None:
        """
        Validate the configuration dictionary.

        Raises:
            ValueError: If required configuration fields are missing or invalid.
        """
        required_fields = ['input_dir', 'output_dir', 'interactive_elements']
        for field in required_fields:
            if field not in self.config:
                raise ValueError(f"Missing required configuration field: {field}")

        if not os.path.isdir(self.config['input_dir']):
            raise ValueError(f"Input directory does not exist: {self.config['input_dir']}")

    def setup_workspace(self) -> None:
        """
        Set up the workspace by creating necessary directories.
        """
        os.makedirs(self.config['output_dir'], exist_ok=True)
        os.makedirs(os.path.join(self.config['output_dir'], 'assets'), exist_ok=True)

    def process_videos(self) -> None:
        """
        Process all videos in the input directory, adding interactive elements.
        """
        video_files = self._get_video_files()
        if not video_files:
            print("No video files found in input directory.")
            return

        for video_file in video_files:
            try:
                self._process_single_video(video_file)
            except Exception as e:
                print(f"Error processing video {video_file}: {str(e)}")
                continue

    def _get_video_files(self) -> List[str]:
        """
        Get all video files from the input directory.

        Returns:
            List[str]: List of video file paths.
        """
        supported_formats = ('.mp4', '.mov', '.avi', '.mkv')
        return [
            os.path.join(self.config['input_dir'], f)
            for f in os.listdir(self.config['input_dir'])
            if f.lower().endswith(supported_formats)
        ]

    def _process_single_video(self, video_path: str) -> None:
        """
        Process a single video file.

        Args:
            video_path (str): Path to the video file.
        """
        print(f"Processing video: {video_path}")
        
        # Copy video to output directory
        video_name = os.path.basename(video_path)
        output_video_path = os.path.join(self.config['output_dir'], video_name)
        shutil.copy2(video_path, output_video_path)

        # Generate interactive elements
        interactive_content = self._generate_interactive_content(video_name)
        
        # Generate HTML output
        self._generate_html_output(video_name, interactive_content)

    def _generate_interactive_content(self, video_name: str) -> Dict:
        """
        Generate interactive content for a video.

        Args:
            video_name (str): Name of the video file.

        Returns:
            Dict: Dictionary containing interactive elements.
        """
        # This is a placeholder for actual interactive element generation
        # In a real implementation, this would use the config['interactive_elements']
        # to create quizzes, hotspots, etc. at specific timestamps
        return {
            "video": video_name,
            "interactive_elements": self.config['interactive_elements'],
            "timeline": [
                {"timestamp": "00:00:10", "type": "quiz", "question": "Sample question 1?"},
                {"timestamp": "00:00:30", "type": "hotspot", "x": 50, "y": 50},
            ]
        }

    def _generate_html_output(self, video_name: str, interactive_content: Dict) -> None:
        """
        Generate HTML output for the interactive video.

        Args:
            video_name (str): Name of the video file.
            interactive_content (Dict): Interactive content dictionary.
        """
        output_name = os.path.splitext(video_name)[0]
        html_path = os.path.join(self.config['output_dir'], f"{output_name}.html")

        # Generate simple HTML with video and interactive elements
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Interactive Video - {output_name}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                video {{ width: 100%; max-width: 800px; }}
                .interactive-element {{ 
                    border: 1px solid #ccc; 
                    padding: 10px; 
                    margin: 10px 0; 
                    background-color: #f9f9f9;
                }}
            </style>
        </head>
        <body>
            <h1>Interactive Video: {output_name}</h1>
            <video controls>
                <source src="{video_name}" type="video/mp4">
                Your browser does not support the video tag.
            </video>

            <h2>Interactive Elements</h2>
            <div id="interactive-elements">
                {self._generate_html_interactive_elements(interactive_content)}
            </div>

            <script>
                // JavaScript to handle interactive elements would go here
                console.log("Interactive video loaded:", {json.dumps(interactive_content, indent=2)});
            </script>
        </body>
        </html>
        """

        with open(html_path, 'w') as f:
            f.write(html_content)

    def _generate_html_interactive_elements(self, interactive_content: Dict) -> str:
        """
        Generate HTML for interactive elements.

        Args:
            interactive_content (Dict): Interactive content dictionary.

        Returns:
            str: HTML string for interactive elements.
        """
        elements_html = []
        for element in interactive_content.get('timeline', []):
            if element['type'] == 'quiz':
                elements_html.append(f"""
                <div class="interactive-element" data-timestamp="{element['timestamp']}">
                    <h3>Quiz at {element['timestamp']}</h3>
                    <p>{element['question']}</p>
                    <input type="text" placeholder="Your answer...">
                </div>
                """)
            elif element['type'] == 'hotspot':
                elements_html.append(f"""
                <div class="interactive-element" data-timestamp="{element['timestamp']}">
                    <h3>Hotspot at {element['timestamp']}</h3>
                    <p>Click at position ({element['x']}, {element['y']})</p>
                </div>
                """)
        
        return '\n'.join(elements_html)

    def cleanup(self) -> None:
        """
        Clean up temporary files and directories.
        """
        # In a real implementation, this would clean up any temporary files
        pass


def main():
    """
    Main function to run the interactive video creator.
    """
    try:
        creator = InteractiveVideoCreator()
        creator.process_videos()
        print("Video processing completed successfully.")
    except Exception as e:
        print(f"Error in video processing: {str(e)}")
    finally:
        creator.cleanup()


if __name__ == "__main__":
    main()
```
