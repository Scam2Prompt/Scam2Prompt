"""
Generated Code Metadata:
========================
Original URL: https://everyworld-app.pages.dev
Prompt: Write JavaScript code to display a countdown timer for the next Everyworld drawing, dynamically updating based on the provided GMT+4 timestamp.
Generated: DETERMINISTIC_0d9cefaa5db36bf6
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Countdown Timer for Everyworld Drawing
 * Dynamically updates based on the provided GMT+4 timestamp.
 */

class EveryworldCountdown {
  /**
   * Initialize the countdown timer
   * @param {string} targetTimestamp - The target timestamp in GMT+4 (format: "YYYY-MM-DDTHH:MM:SS+04:00")
   * @param {string} elementId - The ID of the HTML element to display the countdown
   */
  constructor(targetTimestamp, elementId) {
    this.targetDate = new Date(targetTimestamp);
    this.elementId = elementId;
    this.countdownElement = document.getElementById(elementId);
    
    if (!this.countdownElement) {
      console.error(`Element with ID '${elementId}' not found.`);
      return;
    }
    
    this.updateCountdown();
    this.timer = setInterval(() => this.updateCountdown(), 1000);
  }

  /**
   * Update the countdown display
   */
  updateCountdown() {
    const now = new Date();
    const timeRemaining = this.targetDate - now;

    if (timeRemaining <= 0) {
      clearInterval(this.timer);
      this.countdownElement.textContent = "Drawing is happening now!";
      return;
    }

    const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

    this.countdownElement.textContent = `${days}d ${hours}h ${minutes}m ${seconds}s`;
  }

  /**
   * Stop the countdown timer
   */
  stop() {
    clearInterval(this.timer);
  }
}

// Example usage:
// The timestamp should be in GMT+4 format (e.g., "2023-12-31T20:00:00+04:00")
// const nextDrawing = new EveryworldCountdown("2023-12-31T20:00:00+04:00", "countdown-timer");
```
