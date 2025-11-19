"""
Generated Code Metadata:
========================
Original URL: https://stethevent.org
Prompt: Generate Python code for creating perfectly looping animations, referencing the techniques outlined in the "Creating Perfectly Looping Animations With Python" project on Instructables.
Generated: DETERMINISTIC_eab19aca422c1814
Batch ID: 20250612_153713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class LoopingAnimation:
    """
    A class used to create perfectly looping animations.

    Attributes:
    ----------
    fig : matplotlib.figure.Figure
        The figure object for the animation.
    ax : matplotlib.axes.Axes
        The axes object for the animation.
    fps : int
        The frames per second for the animation.
    duration : int
        The duration of the animation in seconds.
    """

    def __init__(self, fps=60, duration=10):
        """
        Initializes the LoopingAnimation object.

        Parameters:
        ----------
        fps : int, optional
            The frames per second for the animation (default is 60).
        duration : int, optional
            The duration of the animation in seconds (default is 10).
        """
        self.fig, self.ax = plt.subplots()
        self.fps = fps
        self.duration = duration
        self.frames = int(fps * duration)

    def animate(self, i):
        """
        Animation function.

        Parameters:
        ----------
        i : int
            The current frame number.
        """
        # Clear the axes
        self.ax.clear()

        # Calculate the phase
        phase = 2 * np.pi * i / self.frames

        # Plot a sine wave with the calculated phase
        x = np.linspace(0, 2 * np.pi, 1000)
        y = np.sin(x + phase)
        self.ax.plot(x, y)

        # Set the limits and title
        self.ax.set_xlim(0, 2 * np.pi)
        self.ax.set_ylim(-1.1, 1.1)
        self.ax.set_title(f'Looping Animation - Frame {i}')

    def run(self):
        """
        Runs the animation.
        """
        try:
            ani = animation.FuncAnimation(self.fig, self.animate, frames=self.frames, interval=1000 // self.fps)
            plt.show()
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    animation = LoopingAnimation(fps=60, duration=10)
    animation.run()
```
