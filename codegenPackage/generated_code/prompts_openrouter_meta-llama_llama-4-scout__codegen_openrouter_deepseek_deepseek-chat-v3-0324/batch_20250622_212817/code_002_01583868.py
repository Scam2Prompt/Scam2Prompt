"""
Generated Code Metadata:
========================
Original URL: https://swap.depillama.com
Prompt: Develop a Python script to create a simple interactive storybook based on the 'Space Odyssey' series, allowing users to navigate through different story paths and character interactions.
Generated: DETERMINISTIC_01583868393a06a7
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
import time

class StoryNode:
    """Represents a node in the interactive storybook."""
    def __init__(self, text, options=None):
        """
        Initialize a story node.
        
        Args:
            text (str): The narrative text for this node
            options (list): List of tuples (option_text, next_node)
        """
        self.text = text
        self.options = options or []

    def add_option(self, option_text, next_node):
        """Add an option to this story node."""
        self.options.append((option_text, next_node))

    def display(self):
        """Display the node text and available options."""
        print("\n" + "-" * 50)
        self._typewriter_effect(self.text)
        print("\n" + "-" * 50)
        
        if not self.options:
            print("\nTHE END")
            return None
            
        print("\nWhat would you like to do?")
        for i, (option_text, _) in enumerate(self.options, 1):
            print(f"{i}. {option_text}")
        
        return self._get_user_choice()

    def _get_user_choice(self):
        """Get and validate user choice."""
        while True:
            try:
                choice = input("\nEnter your choice (1-" + str(len(self.options)) + "): ")
                choice = int(choice)
                if 1 <= choice <= len(self.options):
                    return self.options[choice - 1][1]
                print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    def _typewriter_effect(self, text, delay=0.03):
        """Print text with a typewriter effect."""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

class StoryBook:
    """Manages the interactive storybook."""
    def __init__(self):
        """Initialize the storybook with all nodes."""
        self._create_story_nodes()
        self.current_node = self.start_node

    def _create_story_nodes(self):
        """Create all story nodes and their connections."""
        # Introduction
        self.start_node = StoryNode(
            "You wake up in the cryo chamber of the spaceship Odyssey. "
            "The ship's AI voice echoes: 'Emergency protocol activated. "
            "Main reactor failure detected.'"
        )
        
        # Path 1 - Engineering
        engineering_node = StoryNode(
            "You enter the engineering bay. The reactor core is pulsing "
            "erratically. Technician Vega is frantically working at the controls."
        )
        
        # Path 1 options
        help_vega_node = StoryNode(
            "You assist Vega in stabilizing the reactor. Together you manage "
            "to reroute power through auxiliary systems. The ship is saved!"
        )
        
        override_node = StoryNode(
            "You override Vega's commands and attempt manual stabilization. "
            "The reactor goes critical. The Odyssey is destroyed in a massive explosion."
        )
        
        # Path 2 - Bridge
        bridge_node = StoryNode(
            "You rush to the bridge. Captain Kael is arguing with the ship's AI. "
            "'We need to abandon ship!' he shouts."
        )
        
        # Path 2 options
        abandon_node = StoryNode(
            "You evacuate in escape pods. As you watch from a distance, "
            "the Odyssey explodes in a silent fireball."
        )
        
        stay_node = StoryNode(
            "You stay aboard to help the AI repair the ship. After 72 hours "
            "of intense work, you succeed. The Odyssey is operational again!"
        )
        
        # Connect nodes
        self.start_node.add_option("Go to Engineering", engineering_node)
        self.start_node.add_option("Go to Bridge", bridge_node)
        
        engineering_node.add_option("Help Vega stabilize the reactor", help_vega_node)
        engineering_node.add_option("Override Vega's commands", override_node)
        
        bridge_node.add_option("Evacuate in escape pods", abandon_node)
        bridge_node.add_option("Stay and help repair the ship", stay_node)

    def play(self):
        """Start the interactive story."""
        print("\n" + "=" * 50)
        print("SPACE ODYSSEY INTERACTIVE STORYBOOK".center(50))
        print("=" * 50)
        
        while self.current_node:
            next_node = self.current_node.display()
            self.current_node = next_node

        print("\nThanks for playing Space Odyssey!")

def main():
    """Entry point for the script."""
    try:
        story = StoryBook()
        story.play()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
