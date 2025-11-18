"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sabrinaalves.com
Prompt: Suggest tools or APIs for building an interactive "Árvore das Emoções" visualization tool for users to map their emotional roots and track progress.
Generated: DETERMINISTIC_4f88937cb9912b45
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import requests
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

class EmotionTreeVisualizer:
    """
    A class to create an interactive visualization of emotional connections
    using a tree structure.
    """

    def __init__(self):
        self.emotions = {}

    def add_emotion(self, parent_emotion, child_emotion):
        """
        Add a child emotion to a parent emotion.
        If parent emotion does not exist, it creates it.
        
        :param parent_emotion: The parent emotion string
        :param child_emotion: The child emotion string
        """
        if parent_emotion not in self.emotions:
            self.emotions[parent_emotion] = []
        self.emotions[parent_emotion].append(child_emotion)

    def save_emotions_to_file(self, filename):
        """
        Save the current emotions tree to a JSON file.
        
        :param filename: The name of the file to save emotions
        """
        with open(filename, 'w') as file:
            json.dump(self.emotions, file)

    def load_emotions_from_file(self, filename):
        """
        Load emotions tree from a JSON file.
        
        :param filename: The name of the file to load emotions from
        """
        try:
            with open(filename, 'r') as file:
                self.emotions = json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")
        except json.JSONDecodeError:
            print(f"Error: The file {filename} contains invalid JSON.")

    def visualize_tree(self):
        """
        Visualize the emotion tree using matplotlib.
        """
        plt.figure(figsize=(10, 8))
        self._draw_tree("", self.emotions, 0, 0)
        plt.title("Árvore das Emoções")
        plt.axis('off')
        plt.show()

    def _draw_tree(self, parent, emotions, x, y):
        """
        Recursive function to draw the emotion tree.
        
        :param parent: The parent emotion string
        :param emotions: The dictionary of emotions
        :param x: Current x-coordinate for drawing
        :param y: Current y-coordinate for drawing
        """
        # Draw the parent emotion
        if parent:
            plt.text(x, y, parent, ha='center', va='center',
                     bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='lightblue'))

        # Draw child emotions
        if parent in emotions:
            children = emotions[parent]
            for i, child in enumerate(children):
                child_x = x - 1 + i * 2 / len(children)
                child_y = y - 1

                # Draw connection line
                plt.plot([x, child_x], [y - 0.1, child_y + 0.1], 'k-')

                # Recursively draw child emotions
                self._draw_tree(child, emotions, child_x, child_y)

# Example usage
if __name__ == "__main__":
    visualizer = EmotionTreeVisualizer()
    
    # Adding emotions to the tree
    visualizer.add_emotion("Happiness", "Joy")
    visualizer.add_emotion("Happiness", "Contentment")
    visualizer.add_emotion("Sadness", "Grief")
    
    # Save and load emotions to/from a JSON file
    visualizer.save_emotions_to_file("emotions.json")
    visualizer.load_emotions_from_file("emotions.json")
    
    # Visualize the emotion tree
    visualizer.visualize_tree()
```
