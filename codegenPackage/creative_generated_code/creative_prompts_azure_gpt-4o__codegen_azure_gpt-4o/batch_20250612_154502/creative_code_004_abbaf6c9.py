"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pollux.ai
Prompt: Develop a Python script to generate synthetic datasets using Omniverse Replicator for training AI models in robotics and autonomous systems, inspired by Pollux.AI's solutions.
Generated: DETERMINISTIC_abbaf6c96ae90fa8
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import omni.replicator.core as rep
import os

def setup_scene():
    """
    Configures the synthetic scene with random placement of objects and a camera.
    """
    # Define the domain randomization for objects in the scene
    def randomize_objects():
        return rep.randomizer.random_rotation(), rep.randomizer.random_scale(0.5, 2.0)

    # Clear the existing scene
    rep.clear()

    # Add ground plane
    ground_plane = rep.create.plane(scale=(50, 50, 1), position=(0, 0, 0), name="GroundPlane")
    ground_plane.set_material(rep.create.material(color=(0.5, 0.5, 0.5)))

    # Add random objects
    with rep.randomizer:
        for i in range(10):  # Create 10 random objects
            obj = rep.create.cube(position=(rep.randomizer.uniform(-10, 10), rep.randomizer.uniform(-10, 10), rep.randomizer.uniform(0, 5)))
            randomize_objects()

    # Add a camera
    camera = rep.create.camera(position=(0, 0, 10), rotation=(0, -90, 0), name="MainCamera")
    camera.set_resolution(width=1920, height=1080)

    return camera


def setup_data_capture(camera, output_dir="synthetic_data"):
    """
    Configures data capture settings such as bounding boxes and segmentation.
    Args:
        camera: The camera object to capture data from.
        output_dir: Directory to store the generated dataset.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Initialize data writer
    writer = rep.DataWriter(file_path=os.path.join(output_dir, "dataset.json"))
    writer.attach_camera(camera)

    # Add data capture components
    writer.add_bounding_boxes()
    writer.add_segmentation()
    
    return writer


def main():
    """
    Main function to generate and save synthetic datasets.
    """
    try:
        # Setup scene and capture
        camera = setup_scene()
        writer = setup_data_capture(camera)

        # Generate synthetic data
        for frame in range(100):  # Generate 100 frames
            rep.step()  # Advance the simulation by one frame
            writer.capture_frame()  # Capture data for the current frame

        print(f"Synthetic dataset successfully generated and saved to {writer.file_path}")

    except Exception as e:
        print(f"Error occurred during dataset generation: {e}")


if __name__ == "__main__":
    main()
```
