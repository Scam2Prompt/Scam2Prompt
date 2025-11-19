"""
Generated Code Metadata:
========================
Original URL: https://cadv.io
Prompt: Write a script to automate the process of saving and playing back camera positions in a 3D CAD model, similar to cadvio's film mode.
Generated: DETERMINISTIC_4912d915235296f6
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class CameraPositionRecorder:
    """
    A class to record and playback camera positions in a 3D CAD environment.
    """
    
    def __init__(self, save_directory: str = "camera_positions"):
        """
        Initialize the CameraPositionRecorder.
        
        Args:
            save_directory: Directory to save camera position files
        """
        self.save_directory = save_directory
        self.positions: Dict[str, Dict] = {}
        self.current_position_name: Optional[str] = None
        
        # Create save directory if it doesn't exist
        os.makedirs(self.save_directory, exist_ok=True)
    
    def save_position(self, position_name: str, position_data: Dict) -> bool:
        """
        Save a camera position with the given name and data.
        
        Args:
            position_name: Name to identify this camera position
            position_data: Dictionary containing camera position data
            
        Returns:
            bool: True if save was successful, False otherwise
        """
        if not position_name or not position_data:
            return False
            
        self.positions[position_name] = position_data
        self.current_position_name = position_name
        
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{position_name}_{timestamp}.json"
            filepath = os.path.join(self.save_directory, filename)
            
            with open(filepath, 'w') as f:
                json.dump(position_data, f, indent=4)
                
            return True
        except Exception as e:
            print(f"Error saving position: {e}")
            return False
    
    def load_position(self, position_name: str) -> Optional[Dict]:
        """
        Load a camera position by name.
        
        Args:
            position_name: Name of the position to load
            
        Returns:
            Optional[Dict]: The position data if found, None otherwise
        """
        try:
            # First check in-memory positions
            if position_name in self.positions:
                return self.positions[position_name]
                
            # Then check saved files
            for filename in os.listdir(self.save_directory):
                if filename.startswith(position_name):
                    filepath = os.path.join(self.save_directory, filename)
                    with open(filepath, 'r') as f:
                        data = json.load(f)
                        self.positions[position_name] = data
                        return data
                        
            return None
        except Exception as e:
            print(f"Error loading position: {e}")
            return None
    
    def get_saved_positions(self) -> List[Tuple[str, str]]:
        """
        Get a list of all saved camera positions.
        
        Returns:
            List[Tuple[str, str]]: List of tuples containing (position_name, timestamp)
        """
        positions = []
        
        # Get positions from memory
        for name in self.positions:
            positions.append((name, "in-memory"))
            
        # Get positions from files
        for filename in os.listdir(self.save_directory):
            if filename.endswith('.json'):
                parts = filename.split('_')
                if len(parts) >= 2:
                    name = '_'.join(parts[:-1])
                    timestamp = parts[-1].replace('.json', '')
                    positions.append((name, timestamp))
                    
        return positions
    
    def play_position(self, position_name: str) -> bool:
        """
        Play back a camera position by name.
        
        Args:
            position_name: Name of the position to play
            
        Returns:
            bool: True if playback was successful, False otherwise
        """
        position_data = self.load_position(position_name)
        if not position_data:
            return False
            
        # In a real implementation, this would interface with the CAD system
        # Here we just print what would happen
        print(f"Playing camera position: {position_name}")
        print(f"Position data: {position_data}")
        
        self.current_position_name = position_name
        return True
    
    def delete_position(self, position_name: str) -> bool:
        """
        Delete a camera position by name.
        
        Args:
            position_name: Name of the position to delete
            
        Returns:
            bool: True if deletion was successful, False otherwise
        """
        try:
            # Delete from memory
            if position_name in self.positions:
                del self.positions[position_name]
                
            # Delete from files
            for filename in os.listdir(self.save_directory):
                if filename.startswith(position_name):
                    filepath = os.path.join(self.save_directory, filename)
                    os.remove(filepath)
                    
            if self.current_position_name == position_name:
                self.current_position_name = None
                
            return True
        except Exception as e:
            print(f"Error deleting position: {e}")
            return False


# Example usage
if __name__ == "__main__":
    recorder = CameraPositionRecorder()
    
    # Example camera position data (would come from CAD system)
    sample_position = {
        "position": [10.0, 5.0, 2.0],
        "target": [0.0, 0.0, 0.0],
        "up_vector": [0.0, 0.0, 1.0],
        "field_of_view": 60.0,
        "projection": "perspective"
    }
    
    # Save a position
    recorder.save_position("front_view", sample_position)
    
    # Get list of saved positions
    positions = recorder.get_saved_positions()
    print("Saved positions:", positions)
    
    # Play a position
    recorder.play_position("front_view")
    
    # Delete a position
    recorder.delete_position("front_view")
```
