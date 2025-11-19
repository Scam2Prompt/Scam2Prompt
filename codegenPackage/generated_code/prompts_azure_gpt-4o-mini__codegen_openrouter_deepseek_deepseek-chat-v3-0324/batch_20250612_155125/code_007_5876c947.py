"""
Generated Code Metadata:
========================
Original URL: https://cadv.io
Prompt: Create a tutorial on how to navigate through a 3D model in cadvio using Oculus Rift support.
Generated: DETERMINISTIC_5876c94776e9e6fc
Batch ID: 20250612_155125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import cadvio
import oculus

class OculusRiftNavigator:
    """
    A class to handle 3D model navigation in cadvio using Oculus Rift.
    """
    
    def __init__(self, model_path):
        """
        Initialize the navigator with the 3D model.
        
        Args:
            model_path (str): Path to the 3D model file.
        """
        try:
            # Initialize cadvio with the model
            self.model = cadvio.load_model(model_path)
            if not self.model:
                raise ValueError("Failed to load 3D model")
                
            # Initialize Oculus Rift
            self.oculus = oculus.init()
            if not self.oculus:
                raise RuntimeError("Failed to initialize Oculus Rift")
                
            # Set up initial camera position
            self.camera_position = [0, 0, 0]
            self.camera_rotation = [0, 0, 0]
            
            # Movement speed
            self.move_speed = 0.1
            self.rotation_speed = 1.0
            
        except Exception as e:
            print(f"Initialization error: {str(e)}")
            raise

    def update_camera(self):
        """
        Update camera position and rotation based on Oculus Rift input.
        """
        try:
            # Get headset orientation
            head_rotation = self.oculus.get_rotation()
            
            # Apply rotation to camera
            self.camera_rotation = [
                head_rotation[0] * self.rotation_speed,
                head_rotation[1] * self.rotation_speed,
                head_rotation[2] * self.rotation_speed
            ]
            
            # Get controller input for movement
            move_input = self.oculus.get_controller_input()
            
            # Calculate movement vector based on head orientation
            forward_vector = self._calculate_forward_vector()
            
            # Apply movement
            self.camera_position[0] += forward_vector[0] * move_input[1] * self.move_speed
            self.camera_position[1] += forward_vector[1] * move_input[1] * self.move_speed
            self.camera_position[2] += forward_vector[2] * move_input[1] * self.move_speed
            
            # Apply strafing
            right_vector = self._calculate_right_vector()
            self.camera_position[0] += right_vector[0] * move_input[0] * self.move_speed
            self.camera_position[1] += right_vector[1] * move_input[0] * self.move_speed
            self.camera_position[2] += right_vector[2] * move_input[0] * self.move_speed
            
            # Update cadvio camera
            cadvio.set_camera_position(*self.camera_position)
            cadvio.set_camera_rotation(*self.camera_rotation)
            
        except Exception as e:
            print(f"Camera update error: {str(e)}")

    def _calculate_forward_vector(self):
        """
        Calculate forward vector based on current rotation.
        
        Returns:
            list: Normalized forward vector [x, y, z]
        """
        try:
            yaw = self.camera_rotation[1]
            pitch = self.camera_rotation[0]
            
            x = -math.sin(math.radians(yaw)) * math.cos(math.radians(pitch))
            y = math.sin(math.radians(pitch))
            z = -math.cos(math.radians(yaw)) * math.cos(math.radians(pitch))
            
            # Normalize vector
            length = math.sqrt(x*x + y*y + z*z)
            if length > 0:
                return [x/length, y/length, z/length]
            return [0, 0, -1]
        except Exception as e:
            print(f"Vector calculation error: {str(e)}")
            return [0, 0, -1]

    def _calculate_right_vector(self):
        """
        Calculate right vector based on current rotation.
        
        Returns:
            list: Normalized right vector [x, y, z]
        """
        try:
            yaw = self.camera_rotation[1]
            
            x = math.cos(math.radians(yaw))
            y = 0
            z = -math.sin(math.radians(yaw))
            
            # Normalize vector
            length = math.sqrt(x*x + y*y + z*z)
            if length > 0:
                return [x/length, y/length, z/length]
            return [1, 0, 0]
        except Exception as e:
            print(f"Vector calculation error: {str(e)}")
            return [1, 0, 0]

    def run(self):
        """
        Main navigation loop.
        """
        try:
            while True:
                # Update camera position
                self.update_camera()
                
                # Render the scene
                cadvio.render()
                
                # Check for exit condition
                if self.oculus.should_exit():
                    break
                    
        except KeyboardInterrupt:
            print("Navigation stopped by user")
        except Exception as e:
            print(f"Runtime error: {str(e)}")
        finally:
            # Clean up
            self.oculus.shutdown()
            cadvio.cleanup()

# Example usage
if __name__ == "__main__":
    try:
        navigator = OculusRiftNavigator("path/to/your/model.cadvio")
        navigator.run()
    except Exception as e:
        print(f"Failed to start navigation: {str(e)}")
```
