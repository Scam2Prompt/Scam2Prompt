"""
Generated Code Metadata:
========================
Original URL: https://klar-sehen.ch
Prompt: "Generate a code snippet in JavaScript that simulates an eye relaxation exercise, using techniques like progressive muscle relaxation and visualization, as described on the Klar Sehen website."
Generated: DETERMINISTIC_1d0cbcafe0913cc5
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Eye Relaxation Exercise Simulator
 * Implements progressive muscle relaxation and visualization techniques
 * for eye relaxation as described on Klar Sehen website.
 */

class EyeRelaxationExercise {
  constructor() {
    this.exercises = [
      {
        name: "Palming",
        description: "Rub your hands together to warm them, then cup them over your closed eyes without applying pressure.",
        duration: 30000, // 30 seconds
        steps: [
          "Rub your hands together to generate warmth",
          "Close your eyes and place your palms over them",
          "Relax and breathe deeply",
          "Feel the warmth and darkness soothing your eyes"
        ]
      },
      {
        name: "Eye Rolling",
        description: "Slowly roll your eyes in circular motions to relax eye muscles.",
        duration: 20000, // 20 seconds
        steps: [
          "Look up and slowly rotate your eyes clockwise",
          "Complete 5 full rotations",
          "Repeat counter-clockwise",
          "Blink frequently during the exercise"
        ]
      },
      {
        name: "Focus Shifting",
        description: "Alternate focus between near and far objects to reduce eye strain.",
        duration: 25000, // 25 seconds
        steps: [
          "Hold your thumb about 10 inches from your face",
          "Focus on your thumb for 5 seconds",
          "Shift focus to an object 10-20 feet away",
          "Alternate focus for the duration"
        ]
      }
    ];
    this.currentExerciseIndex = 0;
    this.isRunning = false;
    this.timer = null;
  }

  /**
   * Starts the eye relaxation exercise
   * @param {number} exerciseIndex - Index of exercise to start (optional)
   * @returns {Promise} Resolves when exercise is completed
   */
  startExercise(exerciseIndex = 0) {
    if (this.isRunning) {
      return Promise.reject(new Error("Exercise already in progress"));
    }

    if (exerciseIndex < 0 || exerciseIndex >= this.exercises.length) {
      return Promise.reject(new Error("Invalid exercise index"));
    }

    this.currentExerciseIndex = exerciseIndex;
    this.isRunning = true;

    return new Promise((resolve) => {
      const exercise = this.exercises[this.currentExerciseIndex];
      console.log(`Starting ${exercise.name}: ${exercise.description}`);

      this.displaySteps(exercise.steps);

      this.timer = setTimeout(() => {
        this.completeExercise();
        resolve();
      }, exercise.duration);
    });
  }

  /**
   * Displays exercise steps with delays between them
   * @param {Array} steps - Array of step instructions
   */
  displaySteps(steps) {
    const stepDuration = this.exercises[this.currentExerciseIndex].duration / steps.length;
    
    steps.forEach((step, index) => {
      setTimeout(() => {
        console.log(`Step ${index + 1}: ${step}`);
      }, index * stepDuration);
    });
  }

  /**
   * Completes the current exercise
   */
  completeExercise() {
    clearTimeout(this.timer);
    this.isRunning = false;
    console.log(`Completed ${this.exercises[this.currentExerciseIndex].name} exercise.`);
    console.log("Remember to blink frequently and take regular breaks from screens.");
  }

  /**
   * Stops the current exercise prematurely
   */
  stopExercise() {
    if (!this.isRunning) {
      console.log("No exercise in progress");
      return;
    }

    clearTimeout(this.timer);
    this.isRunning = false;
    console.log(`Stopped ${this.exercises[this.currentExerciseIndex].name} exercise early.`);
  }

  /**
   * Gets list of available exercises
   * @returns {Array} List of exercise objects
   */
  getAvailableExercises() {
    return this.exercises.map((ex, index) => ({
      index,
      name: ex.name,
      description: ex.description,
      duration: ex.duration / 1000 + " seconds"
    }));
  }
}

// Example usage:
// const eyeExercise = new EyeRelaxationExercise();
// eyeExercise.startExercise(0).then(() => console.log("Exercise completed successfully"));
```
