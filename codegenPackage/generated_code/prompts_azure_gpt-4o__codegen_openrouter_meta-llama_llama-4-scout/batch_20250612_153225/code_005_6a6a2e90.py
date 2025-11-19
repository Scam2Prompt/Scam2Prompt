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

# Window and frame settings
WINDOW_NAME = "Eye Exercise Game"
WIDTH, HEIGHT = 800, 600

# Circle properties
CIRCLE_RADIUS = 20

class EyeExerciseGame:
    def __init__(self):
        self.window = cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
        self.window_size = (WIDTH, HEIGHT)
        cv2.resizeWindow(WINDOW_NAME, *self.window_size)
        self.circle_x = random.randint(CIRCLE_RADIUS, WIDTH - CIRCLE_RADIUS)
        self.circle_y = random.randint(CIRCLE_RADIUS, HEIGHT - CIRCLE_RADIUS)

    def draw_circle(self, frame):
        cv2.circle(frame, (self.circle_x, self.circle_y), CIRCLE_RADIUS, (0, 255, 0), -1)

    def move_circle(self):
        self.circle_x = random.randint(CIRCLE_RADIUS, WIDTH - CIRCLE_RADIUS)
        self.circle_y = random.randint(CIRCLE_RADIUS, HEIGHT - CIRCLE_RADIUS)

    def game_loop(self):
        while True:
            frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
            self.draw_circle(frame)
            cv2.putText(frame, "Follow the green circle with your eyes!", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cv2.imshow(WINDOW_NAME, frame)
            key = cv2.waitKey(1000) & 0xFF
            if key == ord('q'):
                break
            self.move_circle()

        cv2.destroyAllWindows()

    def track_object(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Cannot open camera")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Cannot receive frame")
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
            _, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)

            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                area = cv2.contourArea(contour)
                x, y, w, h = cv2.boundingRect(contour)
                aspect_ratio = float(w)/h
                if area > 1000 and aspect_ratio > 2:
                    cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
                    M = cv2.moments(contour)
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                    cv2.circle(frame, (cx, cy), 10, (0, 0, 255), -1)

            cv2.imshow(WINDOW_NAME, frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

def main():
    game = EyeExerciseGame()
    print("Press 'q' to quit the game.")
    print("1. Start eye exercise game")
    print("2. Start object tracking game")
    choice = input("Choose a game: ")
    if choice == "1":
        game.game_loop()
    elif choice == "2":
        game.track_object()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
```
