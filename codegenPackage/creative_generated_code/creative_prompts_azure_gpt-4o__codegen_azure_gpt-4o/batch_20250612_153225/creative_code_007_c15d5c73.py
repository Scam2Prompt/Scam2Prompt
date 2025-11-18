"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agnelosfx.in
Prompt: Provide a Python example for creating a custom fireworks effect for a luxury wedding venue, inspired by Agnelo SFX's work at locations like the Grand Hyatt or Taj Palace.
Generated: DETERMINISTIC_c15d5c7368b527f6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import turtle
import random
import time

def create_firework(turtle_obj, x, y, color, size):
    """
    Creates a single firework effect at the given location.
    
    Args:
        turtle_obj (turtle.Turtle): Turtle object used for drawing.
        x (float): X-coordinate of the firework.
        y (float): Y-coordinate of the firework.
        color (str): Color of the firework.
        size (int): Size scale of the firework.
    """
    # Move to the given coordinates
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.color(color)
    
    # Draw multiple lines originating from the center
    for _ in range(36):  # 36 lines create a circular burst effect
        turtle_obj.forward(size)
        turtle_obj.backward(size)
        turtle_obj.right(10)  # Rotate 10 degrees for the next line

def generate_random_firework(turtle_obj, screen_width, screen_height):
    """
    Generates a random firework effect within the screen boundaries.
    
    Args:
        turtle_obj (turtle.Turtle): Turtle object used for drawing.
        screen_width (int): Width of the screen.
        screen_height (int): Height of the screen.
    """
    # Randomize position, color, and size
    x = random.randint(-screen_width // 2, screen_width // 2)
    y = random.randint(-screen_height // 2, screen_height // 2)
    color = random.choice(['red', 'blue', 'yellow', 'green', 'purple', 'orange'])
    size = random.randint(20, 100)
    
    # Create the firework
    create_firework(turtle_obj, x, y, color, size)

def main():
    """
    Main function to create the fireworks display.
    """
    # Setup the turtle screen
    screen = turtle.Screen()
    screen.bgcolor("black")  # Set background color to black
    screen.title("Luxury Wedding Fireworks Display")
    
    screen_width, screen_height = screen.window_width(), screen.window_height()
    
    # Create a turtle object for drawing
    firework_turtle = turtle.Turtle()
    firework_turtle.speed(0)  # Set turtle to maximum speed
    firework_turtle.hideturtle()  # Hide the turtle cursor
    
    # Generate fireworks in a loop
    try:
        for _ in range(20):  # Number of fireworks
            generate_random_firework(firework_turtle, screen_width, screen_height)
            time.sleep(0.5)  # Pause to simulate timing between fireworks
    except Exception as e:
        print(f"An error occurred while generating fireworks: {e}")
    finally:
        # Close the turtle screen on click
        screen.mainloop()

# Run the main function
if __name__ == "__main__":
    main()
```
