"""
Generated Code Metadata:
========================
Original URL: https://jeremiefremont.com
Prompt: Describe the role of a sound designer in creating an immersive experience for a TV documentary series like "Race for a vaccine" or "Hondelatte raconte".
Generated: DETERMINISTIC_8c906a69c4b54220
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SoundDesigner:
    """
    A class to represent a sound designer responsible for creating immersive audio experiences
    for TV documentary series.
    """

    def __init__(self, project_name):
        """
        Initializes the SoundDesigner with a project name.

        Args:
            project_name (str): The name of the documentary project.
        """
        self.project_name = project_name
        self.audio_elements = []
        self.final_mix = None

    def add_audio_element(self, audio_file):
        """
        Adds an audio element to the project.

        Args:
            audio_file (str): The path to the audio file to be added.

        Raises:
            FileNotFoundError: If the audio file does not exist.
        """
        try:
            # Simulate checking if the audio file exists
            if not self._file_exists(audio_file):
                raise FileNotFoundError(f"Audio file {audio_file} not found.")
            self.audio_elements.append(audio_file)
            print(f"Added audio element: {audio_file}")
        except Exception as e:
            print(f"Error adding audio element: {e}")

    def create_final_mix(self):
        """
        Creates the final mix of all audio elements.

        Raises:
            ValueError: If no audio elements are added.
        """
        if not self.audio_elements:
            raise ValueError("No audio elements to mix.")
        
        # Simulate mixing audio elements
        self.final_mix = "Final mix of " + ", ".join(self.audio_elements)
        print("Final mix created.")

    def _file_exists(self, file_path):
        """
        Simulates checking if a file exists.

        Args:
            file_path (str): The path to the file.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        # In a real implementation, you would check the filesystem.
        # Here we simulate that all files exist for demonstration purposes.
        return True

    def export_final_mix(self, output_file):
        """
        Exports the final mix to a specified output file.

        Args:
            output_file (str): The path where the final mix will be saved.

        Raises:
            ValueError: If the final mix has not been created.
        """
        if self.final_mix is None:
            raise ValueError("Final mix has not been created yet.")
        
        # Simulate exporting the final mix
        print(f"Exporting final mix to {output_file}...")
        # Here you would include the actual export logic.
        print("Export complete.")

# Example usage
if __name__ == "__main__":
    try:
        sound_designer = SoundDesigner("Race for a Vaccine")
        sound_designer.add_audio_element("background_music.mp3")
        sound_designer.add_audio_element("interview_clip.wav")
        sound_designer.create_final_mix()
        sound_designer.export_final_mix("final_documentary_mix.mp3")
    except Exception as e:
        print(f"An error occurred: {e}")
```
