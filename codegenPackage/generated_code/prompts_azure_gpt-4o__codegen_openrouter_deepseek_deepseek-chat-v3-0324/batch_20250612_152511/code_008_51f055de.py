"""
Generated Code Metadata:
========================
Original URL: https://irgift.info
Prompt: Generate code for a countdown timer feature to display limited-time offers on an e-commerce site, similar to the "0 روز 00 ساعت 00 دقیقه 00 ثانیه" timer shown on "ای ار گیفت."
Generated: DETERMINISTIC_51f055de65e0b2be
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
 * Countdown Timer for E-commerce Limited-Time Offers
 * Displays time remaining in days, hours, minutes, and seconds
 * Similar to "ای ار گیفت" style timer
 */

class CountdownTimer {
  /**
   * Initialize the countdown timer
   * @param {string} endTime - ISO string of the end time (e.g., "2023-12-31T23:59:59")
   * @param {string} containerId - ID of the HTML element to display the timer
   * @param {function} callback - Optional callback when timer reaches zero
   */
  constructor(endTime, containerId, callback = null) {
    this.endTime = new Date(endTime);
    this.container = document.getElementById(containerId);
    this.callback = callback;
    this.intervalId = null;
    
    if (!this.container) {
      throw new Error(`Container element with ID '${containerId}' not found`);
    }
    
    if (isNaN(this.endTime.getTime())) {
      throw new Error('Invalid end time provided');
    }
    
    this.start();
  }

  /**
   * Start the countdown timer
   */
  start() {
    this.updateTimer();
    this.intervalId = setInterval(() => this.updateTimer(), 1000);
  }

  /**
   * Update the timer display
   */
  updateTimer() {
    const now = new Date();
    const timeRemaining = this.endTime - now;

    if (timeRemaining <= 0) {
      this.stop();
      this.container.innerHTML = "0 روز 00 ساعت 00 دقیقه 00 ثانیه";
      if (this.callback) this.callback();
      return;
    }

    const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

    this.container.innerHTML = `${days} روز ${this.padZero(hours)} ساعت ${this.padZero(minutes)} دقیقه ${this.padZero(seconds)} ثانیه`;
  }

  /**
   * Stop the countdown timer
   */
  stop() {
    if (this.intervalId) {
      clearInterval(this.intervalId);
      this.intervalId = null;
    }
  }

  /**
   * Pad single-digit numbers with leading zero
   * @param {number} num - Number to pad
   * @returns {string} Padded number as string
   */
  padZero(num) {
    return num < 10 ? `0${num}` : num;
  }
}

// Example usage:
// const offerTimer = new CountdownTimer(
//   "2023-12-31T23:59:59",
//   "countdown-container",
//   () => console.log("Offer expired!")
// );
```
