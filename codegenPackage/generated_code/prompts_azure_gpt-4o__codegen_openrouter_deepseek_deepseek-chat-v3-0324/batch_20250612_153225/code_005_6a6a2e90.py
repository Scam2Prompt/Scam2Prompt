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
import sys

class EyeExerciseGame:
    def __init__(self):
        """Initialize the eye exercise game with default parameters."""
        self.window_name = "Eye Exercise Game"
        self.screen_width = 800
        self.screen_height = 600
        self.background_color = (255, 255, 255)  # White
        self.target_color = (0, 0, 255)  # Red
        self.target_radius = 20
        self.target_pos = [0, 0]
        self.game_duration = 60  # seconds
        self.current_level = 1
        self.score = 0
        self.start_time = 0
        self.is_running = False
        self.target_speed = 5
        self.max_level = 5

        # Initialize OpenCV window
        cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(self.window_name, self.screen_width, self.screen_height)

    def reset_game(self):
        """Reset game state to initial values."""
        self.current_level = 1
        self.score = 0
        self.target_speed = 5
        self.target_pos = [
            random.randint(self.target_radius, self.screen_width - self.target_radius),
            random.randint(self.target_radius, self.screen_height - self.target_radius)
        ]
        self.start_time = time.time()
        self.is_running = True

    def draw_target(self, frame):
        """Draw the target circle on the frame."""
        cv2.circle(frame, tuple(self.target_pos), self.target_radius, self.target_color, -1)
        cv2.circle(frame, tuple(self.target_pos), self.target_radius // 2, (255, 255, 255), -1)

    def move_target(self):
        """Move the target randomly within screen bounds."""
        direction = random.choice(["left", "right", "up", "down"])
        
        if direction == "left":
            self.target_pos[0] = max(self.target_radius, self.target_pos[0] - self.target_speed)
        elif direction == "right":
            self.target_pos[0] = min(self.screen_width - self.target_radius, self.target_pos[0] + self.target_speed)
        elif direction == "up":
            self.target_pos[1] = max(self.target_radius, self.target_pos[1] - self.target_speed)
        elif direction == "down":
            self.target_pos[1] = min(self.screen_height - self.target_radius, self.target_pos[1] + self.target_speed)

    def check_click(self, x, y):
        """Check if click is within target area."""
        distance = np.sqrt((x - self.target_pos[0])**2 + (y - self.target_pos[1])**2)
        if distance <= self.target_radius:
            self.score += 1
            if self.score % 5 == 0 and self.current_level < self.max_level:
                self.current_level += 1
                self.target_speed += 2
            return True
        return False

    def draw_ui(self, frame):
        """Draw game UI elements."""
        elapsed_time = int(time.time() - self.start_time)
        remaining_time = max(0, self.game_duration - elapsed_time)
        
        # Display score and time
        cv2.putText(frame, f"Level: {self.current_level}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
        cv2.putText(frame, f"Score: {self.score}", (10, 60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
        cv2.putText(frame, f"Time: {remaining_time}s", (10, 90), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

        # Display instructions
        if not self.is_running:
            cv2.putText(frame, "Click the red target to start", 
                        (self.screen_width // 2 - 150, self.screen_height // 2), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

    def run(self):
        """Main game loop."""
        self.reset_game()
        
        def mouse_callback(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                if not self.is_running:
                    self.reset_game()
                else:
                    if self.check_click(x, y):
                        self.target_pos = [
                            random.randint(self.target_radius, self.screen_width - self.target_radius),
                            random.randint(self.target_radius, self.screen_height - self.target_radius)
                        ]

        cv2.setMouseCallback(self.window_name, mouse_callback)

        while True:
            frame = np.full((self.screen_height, self.screen_width, 3), self.background_color, dtype=np.uint8)
            
            if self.is_running:
                self.move_target()
                self.draw_target(frame)
                
                # Check if game time is over
                if time.time() - self.start_time >= self.game_duration:
                    self.is_running = False
                    cv2.putText(frame, f"Game Over! Final Score: {self.score}", 
                                (self.screen_width // 2 - 200, self.screen_height // 2), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
                    cv2.putText(frame, "Click to play again", 
                                (self.screen_width // 2 - 100, self.screen_height // 2 + 40), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
            
            self.draw_ui(frame)
            
            cv2.imshow(self.window_name, frame)
            
            key = cv2.waitKey(30)
            if key == 27:  # ESC key
                break
        
        cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        game = EyeExerciseGame()
        game.run()
    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)
```
