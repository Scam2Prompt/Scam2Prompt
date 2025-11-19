"""
Generated Code Metadata:
========================
Original URL: https://getpromo.me
Prompt: "Develop a simple video script using CreateStudio for a 3D explainer video about environmental conservation."
Generated: DETERMINISTIC_855ab81783525714
Batch ID: 20250622_211832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries for video creation
import createstudio as cs

def create_environmental_conservation_video():
    """
    Creates a 3D explainer video about environmental conservation using CreateStudio.
    """

    # Initialize the CreateStudio project
    project = cs.Project(title="Environmental Conservation Explainer Video")

    try:
        # Set the video duration (in seconds)
        project.set_duration(120)

        # Add a background scene
        background = cs.Background(color="lightblue")
        project.add_background(background)

        # Add a title to the video
        title = cs.Text("Environmental Conservation", font_size=48, color="green")
        project.add_element(title, position=(0.5, 0.9))  # Centered at the top

        # Add a 3D model of the Earth
        earth_model = cs.Model("3D_Earth")
        project.add_element(earth_model, position=(0.5, 0.5), scale=0.5)

        # Add a voiceover explaining the importance of conservation
        voiceover = cs.Audio("voiceover_environmental_conservation.mp3")
        project.add_audio(voiceover)

        # Add animated text explaining key points
        key_points = [
            "Reduce, Reuse, Recycle",
            "Protect Wildlife",
            "Save Water",
            "Plant Trees"
        ]

        for index, point in enumerate(key_points):
            text_element = cs.Text(point, font_size=36, color="darkgreen")
            project.add_element(text_element, position=(0.5, 0.7 - index * 0.1))  # Stacked vertically

        # Add a call to action at the end
        call_to_action = cs.Text("Join Us in Protecting Our Planet!", font_size=40, color="red")
        project.add_element(call_to_action, position=(0.5, 0.1))  # Centered at the bottom

        # Export the video
        project.export(format="mp4", quality="high")

        print("Video created successfully!")

    except cs.CreateStudioError as e:
        print(f"An error occurred while creating the video: {e}")

if __name__ == "__main__":
    create_environmental_conservation_video()
```
