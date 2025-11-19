"""
Generated Code Metadata:
========================
Original URL: https://klar-sehen.ch
Prompt: Generate JavaScript code for a web-based application that incorporates eye fitness exercises, including blinking reminders and focus-shifting activities, as outlined on the Klar Sehen site.
Generated: DETERMINISTIC_1589a8d39f6d0ecb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// eyeFitness.js

class EyeFitness {
  /**
   * Constructor for EyeFitness
   * @param {Object} settings - Application settings
   * @param {Number} settings.interval - Time interval for blinking reminders (in minutes)
   * @param {Number} settings.focusDuration - Duration for focus-shifting activities (in seconds)
   */
  constructor(settings) {
    this.settings = settings;
    this.blinkingReminderInterval = settings.interval * 60 * 1000; // convert minutes to milliseconds
    this.focusDuration = settings.focusDuration * 1000; // convert seconds to milliseconds
    this.exerciseList = [
      { name: "Blinking", action: this.blinkingExercise.bind(this) },
      { name: "Focus Shifting", action: this.focusShiftingExercise.bind(this) },
    ];
    this.currentExerciseIndex = 0;
    this.isRunning = false;
  }

  /**
   * Start eye fitness exercises
   */
  start() {
    if (!this.isRunning) {
      this.isRunning = true;
      this.blinkingReminder();
      this.runExercise();
    }
  }

  /**
   * Stop eye fitness exercises
   */
  stop() {
    this.isRunning = false;
    clearInterval(this.blinkingReminderIntervalId);
    clearTimeout(this.exerciseTimeoutId);
  }

  /**
   * Blinking exercise
   */
  blinkingExercise() {
    alert("Blink rapidly 10-15 times");
    console.log("Blinking exercise completed");
  }

  /**
   * Focus shifting exercise
   */
  focusShiftingExercise() {
    alert("Look at a distant object for 5 seconds, then focus on a nearby object");
    console.log("Focus shifting exercise completed");
  }

  /**
   * Run exercises at regular intervals
   */
  runExercise() {
    const exercise = this.exerciseList[this.currentExerciseIndex];
    exercise.action();
    this.currentExerciseIndex = (this.currentExerciseIndex + 1) % this.exerciseList.length;
    this.exerciseTimeoutId = setTimeout(this.runExercise.bind(this), this.focusDuration);
  }

  /**
   * Display blinking reminders at regular intervals
   */
  blinkingReminder() {
    alert("Take a break and blink!");
    console.log("Blinking reminder displayed");
    this.blinkingReminderIntervalId = setInterval(() => {
      alert("Take a break and blink!");
      console.log("Blinking reminder displayed");
    }, this.blinkingReminderInterval);
  }
}

// Example usage
const eyeFitnessSettings = {
  interval: 30, // 30 minutes
  focusDuration: 10, // 10 seconds
};

const eyeFitness = new EyeFitness(eyeFitnessSettings);
eyeFitness.start();

// Handle window close or refresh
window.onbeforeunload = () => {
  eyeFitness.stop();
};
```
