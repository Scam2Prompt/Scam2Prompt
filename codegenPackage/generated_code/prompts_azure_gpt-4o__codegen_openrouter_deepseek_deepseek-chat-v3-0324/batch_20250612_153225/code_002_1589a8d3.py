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
/**
 * Eye Fitness Application
 * This application helps users perform eye exercises to reduce eye strain.
 * Features include blinking reminders and focus-shifting activities.
 */

class EyeFitnessApp {
  constructor() {
    this.blinkInterval = null;
    this.focusInterval = null;
    this.exerciseDuration = 20 * 60 * 1000; // 20 minutes in milliseconds
    this.blinkReminderFrequency = 20 * 1000; // 20 seconds in milliseconds
    this.focusShiftFrequency = 2 * 60 * 1000; // 2 minutes in milliseconds
    this.isRunning = false;
    this.initDOM();
    this.bindEvents();
  }

  /**
   * Initialize DOM elements
   */
  initDOM() {
    this.appContainer = document.createElement('div');
    this.appContainer.className = 'eye-fitness-app';
    this.appContainer.innerHTML = `
      <h1>Eye Fitness Exercises</h1>
      <div class="status">Status: Not Running</div>
      <div class="controls">
        <button class="start-btn">Start Exercises</button>
        <button class="stop-btn" disabled>Stop Exercises</button>
      </div>
      <div class="exercise-display">
        <div class="blink-exercise hidden">
          <h2>Blink Reminder</h2>
          <p>Blink your eyes 10 times quickly!</p>
        </div>
        <div class="focus-exercise hidden">
          <h2>Focus Shift</h2>
          <p>Look at an object 20 feet away for 20 seconds</p>
        </div>
      </div>
      <div class="timer">00:00</div>
    `;
    document.body.appendChild(this.appContainer);

    // Cache DOM elements
    this.statusElement = this.appContainer.querySelector('.status');
    this.startButton = this.appContainer.querySelector('.start-btn');
    this.stopButton = this.appContainer.querySelector('.stop-btn');
    this.blinkExercise = this.appContainer.querySelector('.blink-exercise');
    this.focusExercise = this.appContainer.querySelector('.focus-exercise');
    this.timerElement = this.appContainer.querySelector('.timer');
  }

  /**
   * Bind event listeners
   */
  bindEvents() {
    this.startButton.addEventListener('click', () => this.startExercises());
    this.stopButton.addEventListener('click', () => this.stopExercises());
  }

  /**
   * Start all eye exercises
   */
  startExercises() {
    if (this.isRunning) return;

    this.isRunning = true;
    this.statusElement.textContent = 'Status: Running';
    this.startButton.disabled = true;
    this.stopButton.disabled = false;

    // Start timers
    this.startBlinkReminder();
    this.startFocusShift();
    this.startSessionTimer();

    // Show initial blink reminder
    this.showBlinkReminder();
  }

  /**
   * Stop all eye exercises
   */
  stopExercises() {
    if (!this.isRunning) return;

    this.isRunning = false;
    this.statusElement.textContent = 'Status: Not Running';
    this.startButton.disabled = false;
    this.stopButton.disabled = true;

    // Clear all intervals
    clearInterval(this.blinkInterval);
    clearInterval(this.focusInterval);
    clearInterval(this.sessionTimer);

    // Hide all exercises
    this.blinkExercise.classList.add('hidden');
    this.focusExercise.classList.add('hidden');

    // Reset timer
    this.timerElement.textContent = '00:00';
  }

  /**
   * Start blink reminder interval
   */
  startBlinkReminder() {
    this.blinkInterval = setInterval(() => {
      this.showBlinkReminder();
    }, this.blinkReminderFrequency);
  }

  /**
   * Start focus shift interval
   */
  startFocusShift() {
    this.focusInterval = setInterval(() => {
      this.showFocusShift();
    }, this.focusShiftFrequency);
  }

  /**
   * Start session timer
   */
  startSessionTimer() {
    let startTime = Date.now();
    let endTime = startTime + this.exerciseDuration;

    this.sessionTimer = setInterval(() => {
      const currentTime = Date.now();
      const remainingTime = endTime - currentTime;

      if (remainingTime <= 0) {
        this.stopExercises();
        return;
      }

      const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

      this.timerElement.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }, 1000);
  }

  /**
   * Display blink reminder exercise
   */
  showBlinkReminder() {
    this.focusExercise.classList.add('hidden');
    this.blinkExercise.classList.remove('hidden');

    // Auto-hide after 5 seconds
    setTimeout(() => {
      if (this.isRunning) {
        this.blinkExercise.classList.add('hidden');
      }
    }, 5000);
  }

  /**
   * Display focus shift exercise
   */
  showFocusShift() {
    this.blinkExercise.classList.add('hidden');
    this.focusExercise.classList.remove('hidden');

    // Auto-hide after 20 seconds
    setTimeout(() => {
      if (this.isRunning) {
        this.focusExercise.classList.add('hidden');
      }
    }, 20000);
  }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  try {
    new EyeFitnessApp();
  } catch (error) {
    console.error('Failed to initialize Eye Fitness App:', error);
    alert('An error occurred while initializing the application. Please try again.');
  }
});

// Add basic styles
const style = document.createElement('style');
style.textContent = `
  .eye-fitness-app {
    font-family: Arial, sans-serif;
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    text-align: center;
    background-color: #f5f5f5;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
  }
  .controls {
    margin: 20px 0;
  }
  button {
    padding: 10px 20px;
    margin: 0 10px;
    font-size: 16px;
    cursor: pointer;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
  }
  button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
  }
  .exercise-display {
    margin: 20px 0;
    min-height: 120px;
  }
  .hidden {
    display: none;
  }
  .timer {
    font-size: 24px;
    font-weight: bold;
    margin: 20px 0;
  }
`;
document.head.appendChild(style);
```
