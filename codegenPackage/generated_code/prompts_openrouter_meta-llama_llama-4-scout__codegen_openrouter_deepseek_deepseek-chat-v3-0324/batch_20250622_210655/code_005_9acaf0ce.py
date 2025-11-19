"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: Write a script for an educational video that teaches children about the importance of understanding and respecting others' perspectives, using examples from the "Vivir es Convivir" program.
Generated: DETERMINISTIC_9acaf0ceb86aa1e1
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Educational Video Script Generator for "Understanding Perspectives"
This script generates a video script to teach children about respecting others' perspectives,
inspired by the "Vivir es Convivir" program.
"""

import random
from typing import List, Dict

class Character:
    """Represents a character in the educational video."""
    def __init__(self, name: str, age: int, background: str):
        self.name = name
        self.age = age
        self.background = background
        self.perspective = ""

    def set_perspective(self, perspective: str):
        """Set the character's perspective on a situation."""
        self.perspective = perspective

    def introduce(self) -> str:
        """Generate character introduction."""
        return f"Hi! I'm {self.name}, I'm {self.age} years old. {self.background}"

class Scenario:
    """Represents a scenario where different perspectives are shown."""
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.characters = []
        self.resolution = ""

    def add_character(self, character: Character):
        """Add a character to the scenario."""
        self.characters.append(character)

    def set_resolution(self, resolution: str):
        """Set how the conflict was resolved."""
        self.resolution = resolution

    def generate_script(self) -> str:
        """Generate the script for this scenario."""
        script = f"SCENARIO: {self.title}\n\n"
        script += f"Situation: {self.description}\n\n"
        
        script += "Characters:\n"
        for character in self.characters:
            script += f"- {character.introduce()}\n"
        
        script += "\nDifferent Perspectives:\n"
        for character in self.characters:
            script += f"{character.name}: {character.perspective}\n"
        
        script += f"\nResolution: {self.resolution}\n"
        script += "\nLesson: Even though we see things differently, we can find ways to understand each other!\n"
        script += "="*50 + "\n"
        return script

class VideoScriptGenerator:
    """Main class to generate the educational video script."""
    def __init__(self):
        self.scenarios = []
        self.intro = ""
        self.outro = ""
        self._setup_content()

    def _setup_content(self):
        """Initialize the video content."""
        self._create_intro_outro()
        self._create_scenarios()

    def _create_intro_outro(self):
        """Create introduction and conclusion for the video."""
        self.intro = """Welcome to "Understanding Each Other"!
        
In this video, we'll learn how different people can see the same situation in different ways,
and how we can respect and understand each other's perspectives.

Let's explore some examples together!\n\n"""
        
        self.outro = """\n\nGreat job learning about different perspectives!
Remember, when we understand how others see things:
- We can be better friends
- We solve problems together
- We make our community happier

Keep practicing seeing things from others' points of view!
See you next time!"""

    def _create_scenarios(self):
        """Create educational scenarios with different perspectives."""
        # Scenario 1: Sharing toys
        scenario1 = Scenario(
            "The Shared Toy",
            "Two children want to play with the same toy at the same time."
        )
        
        maria = Character("Maria", 7, "I love playing with dolls.")
        maria.set_perspective("This is my favorite doll. I had it first and want to keep playing with it.")
        
        juan = Character("Juan", 6, "I like playing with all kinds of toys.")
        juan.set_perspective("That doll looks fun to play with. I want a turn too!")
        
        scenario1.add_character(maria)
        scenario1.add_character(juan)
        scenario1.set_resolution("They agreed to take turns with the doll and found another toy to play with together while waiting.")
        
        self.scenarios.append(scenario1)

        # Scenario 2: Group project
        scenario2 = Scenario(
            "The Group Project",
            "A team of students can't agree on how to present their school project."
        )
        
        sofia = Character("Sofía", 8, "I enjoy drawing and being creative.")
        sofia.set_perspective("We should make a colorful poster with lots of pictures.")
        
        carlos = Character("Carlos", 9, "I like facts and clear information.")
        carlos.set_perspective("We should write a detailed report with all the information.")
        
        luis = Character("Luis", 8, "I love technology.")
        luis.set_perspective("We should make a digital presentation with videos.")
        
        scenario2.add_character(sofia)
        scenario2.add_character(carlos)
        scenario2.add_character(luis)
        scenario2.set_resolution("They combined all their ideas: made a poster with key facts, included a QR code linking to their digital presentation.")
        
        self.scenarios.append(scenario2)

        # Scenario 3: Lunchtime
        scenario3 = Scenario(
            "Lunchtime Choices",
            "Some classmates are making fun of what another student brought for lunch."
        )
        
        ana = Character("Ana", 7, "I come from a different country.")
        ana.set_perspective("This is the food my family eats at home. I don't understand why they're laughing.")
        
        pedro = Character("Pedro", 7, "I've only eaten food common in our country.")
        pedro.set_perspective("That food looks strange. I've never seen anything like it before.")
        
        scenario3.add_character(ana)
        scenario3.add_character(pedro)
        scenario3.set_resolution("Pedro apologized and asked Ana to explain about her food. They ended up sharing and trying each other's lunches.")
        
        self.scenarios.append(scenario3)

    def generate_full_script(self) -> str:
        """Generate the complete video script."""
        script = self.intro
        
        for i, scenario in enumerate(self.scenarios, 1):
            script += f"\nExample {i}:\n"
            script += scenario.generate_script()
        
        script += self.outro
        return script

    def save_script(self, filename: str = "understanding_perspectives_script.txt"):
        """Save the generated script to a file."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(self.generate_full_script())
            print(f"Script successfully saved to {filename}")
        except IOError as e:
            print(f"Error saving script: {e}")

if __name__ == "__main__":
    generator = VideoScriptGenerator()
    print(generator.generate_full_script())
    generator.save_script()
```
