"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken.media
Prompt: Generate a script for an explainer video that simplifies a complex topic, incorporating Kraken Media's approach to engaging storytelling and clear value demonstration.
Generated: DETERMINISTIC_63901ec31493545a
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import textwrap

class VideoScriptGenerator:
    """
    A class to generate an explainer video script.
    """

    def __init__(self, topic, complexity_level):
        """
        Initialize the VideoScriptGenerator with a topic and its complexity level.
        
        Args:
            topic (str): The complex topic to be simplified.
            complexity_level (str): The level of complexity (easy, medium, hard).
        """
        self.topic = topic
        self.complexity_level = complexity_level
        self.script = []

    def generate_intro(self):
        """
        Generate the introduction part of the script.
        """
        intro = f"Welcome to our explainer video on {self.topic}!\n"
        intro += "Today, we'll break down this complex topic into simple, easy-to-understand parts."
        self.script.append(intro)

    def generate_body(self):
        """
        Generate the body of the script based on the complexity level.
        """
        if self.complexity_level == 'easy':
            body = f"Let's start with the basics of {self.topic}, focusing on key concepts.\n"
            body += "We will define terms and provide relatable examples."
        elif self.complexity_level == 'medium':
            body = f"Now, diving a bit deeper into {self.topic}, we'll explore intermediate concepts.\n"
            body += "We'll highlight real-life applications to make it relatable."
        elif self.complexity_level == 'hard':
            body = f"Finally, let's tackle advanced aspects of {self.topic}.\n"
            body += "We'll address common misconceptions and provide expert insights."
        else:
            raise ValueError("Unknown complexity level. Use 'easy', 'medium', or 'hard'.")

        self.script.append(body)

    def generate_conclusion(self):
        """
        Generate the conclusion part of the script.
        """
        conclusion = "In conclusion, understanding {self.topic} is essential.\n"
        conclusion += "We hope this video has made the topic clearer and more engaging for you!"
        self.script.append(conclusion)

    def generate_script(self):
        """
        Generate the complete script by combining intro, body, and conclusion.
        
        Returns:
            str: The complete video script.
        """
        self.generate_intro()
        self.generate_body()
        self.generate_conclusion()
        
        return "\n\n".join(self.script)

def main():
    """
    Main function to execute the script generation.
    """
    # User input for the topic and complexity level
    topic = input("Enter the topic you'd like to simplify: ")
    complexity_level = input("Enter the complexity level (easy, medium, hard): ")

    try:
        # Create an instance of VideoScriptGenerator
        script_generator = VideoScriptGenerator(topic, complexity_level)
        # Generate the script
        script = script_generator.generate_script()
        # Display the generated script
        print("\nGenerated Video Script:\n")
        print(textwrap.dedent(script))
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
