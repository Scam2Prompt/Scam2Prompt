"""
Generated Code Metadata:
========================
Original URL: https://o3-labs.vercel.app
Prompt: Create a countdown timer in JavaScript to display the time left for a campaign, similar to the "7d • 0h • 0m • 0s" timer on the O3 Token website.
Generated: DETERMINISTIC_b95da8260c795fcc
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Countdown Timer for Campaign
 * Displays time remaining in days, hours, minutes, and seconds format
 * Example: "7d • 0h • 0m • 0s"
 */

class CountdownTimer {
  /**
   * Initialize the countdown timer
   * @param {string} endDate - The end date of the campaign in ISO format (YYYY-MM-DDTHH:MM:SS)
   * @param {string} elementId - The ID of the HTML element to display the timer
   */
  constructor(endDate, elementId) {
    this.endDate = new Date(endDate);
    this.elementId = elementId;
    this.timerElement = document.getElementById(elementId);
    
    if (!this.timerElement) {
      throw new Error(`Element with ID '${elementId}' not found`);
    }
    
    this.interval = null;
    this.updateTimer(); // Initial update
  }

  /**
   * Calculate time remaining and update the display
   */
  updateTimer() {
    const now = new Date();
    const timeLeft = this.endDate - now;

    if (timeLeft <= 0) {
      this.timerElement.textContent = "Campaign ended";
      this.stop();
      return;
    }

    const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

    this.timerElement.textContent = `${days}d • ${hours}h • ${minutes}m • ${seconds}s`;
  }

  /**
   * Start the countdown timer
   */
  start() {
    if (this.interval) return; // Prevent multiple intervals
    this.interval = setInterval(() => this.updateTimer(), 1000);
  }

  /**
   * Stop the countdown timer
   */
  stop() {
    if (this.interval) {
      clearInterval(this.interval);
      this.interval = null;
    }
  }
}

// Example usage:
// const campaignTimer = new CountdownTimer("2023-12-31T23:59:59", "countdown-timer");
// campaignTimer.start();
```
