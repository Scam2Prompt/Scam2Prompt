"""
Generated Code Metadata:
========================
Original URL: https://klar-sehen.ch
Prompt: Develop a Python script that uses OpenCV to create a simple eye exercise game, incorporating visualizations and movement-based activities similar to the "Sehspiele" described on Klar Sehen.
Generated: DETERMINISTIC_6a6a2e9087b0d73d
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import cv2
import numpy as np
import random
import time

# Constants for the game
WINDOW_NAME = "Eye Exercise Game"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CIRCLE_RADIUS = 30
CIRCLE_COLOR = (0, 255, 0)  # Green color in BGR
BACKGROUND_COLOR = (0, 0, 0)  # Black background
FPS = 30  # Frames per second

# Function to create a random position for the circle
def get_random_position():
    x = random.randint(CIRCLE_RADIUS, SCREEN_WIDTH - CIRCLE_RADIUS)
    y = random.randint(CIRCLE_RADIUS, SCREEN_HEIGHT - CIRCLE_RADIUS)
    return (x, y)

# Function to draw the circle on the screen
def draw_circle(image, position):
    cv2.circle(image, position, CIRCLE_RADIUS, CIRCLE_COLOR, -1)

# Main function to run the eye exercise game
def run_eye_exercise_game():
    # Create a window
    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(WINDOW_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    # Initialize game variables
    score = 0
    start_time = time.time()
    duration = 30  # Game duration in seconds

    # Game loop
    while True:
        # Create a black image
        image = np.zeros((SCREEN_HEIGHT, SCREEN_WIDTH, 3), dtype=np.uint8)

        # Get a random position for the circle
        position = get_random_position()

        # Draw the circle on the image
        draw_circle(image, position)

        # Display the score and time left
        cv2.putText(image, f'Score: {score}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        time_left = duration - int(time.time() - start_time)
        cv2.putText(image, f'Time Left: {time_left}s', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Show the image
        cv2.imshow(WINDOW_NAME, image)

        # Check for user input
        key = cv2.waitKey(1000 // FPS)

        # Check if the user clicked on the circle
        if key == ord('q'):  # Quit the game
            break
        elif cv2.getWindowProperty(WINDOW_NAME, cv2.WND_PROP_VISIBLE) < 1:  # Window closed
            break

        # Check mouse click
        def click_event(event, x, y, flags, param):
            nonlocal score
            if event == cv2.EVENT_LBUTTONDOWN:
                # Check if the click is within the circle
                if (x - position[0]) ** 2 + (y - position[1]) ** 2 <= CIRCLE_RADIUS ** 2:
                    score += 1

        # Set mouse callback
        cv2.setMouseCallback(WINDOW_NAME, click_event)

        # Check if time is up
        if time_left <= 0:
            break

    # Clean up
    cv2.destroyAllWindows()
    print(f'Game Over! Your final score is: {score}')

if __name__ == "__main__":
    try:
        run_eye_exercise_game()
    except Exception as e:
        print(f"An error occurred: {e}")
```
