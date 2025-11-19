"""
Generated Code Metadata:
========================
Original URL: https://ballatorino.it
Prompt: Create a JavaScript code snippet to implement a countdown timer for an event like BallaTorino, displaying the days, hours, minutes, and seconds until the event starts.
Generated: DETERMINISTIC_a47583f20f7af94e
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CountdownTimer.js

/**
 * CountdownTimer class to display the days, hours, minutes, and seconds until an event starts.
 */
class CountdownTimer {
  /**
   * Constructor to initialize the event date and the element to display the countdown.
   * @param {Date} eventDate - The date and time of the event.
   * @param {HTMLElement} displayElement - The HTML element to display the countdown.
   */
  constructor(eventDate, displayElement) {
    this.eventDate = eventDate;
    this.displayElement = displayElement;
  }

  /**
   * Method to calculate the time difference between the current date and the event date.
   * @returns {Object} - An object containing the days, hours, minutes, and seconds until the event starts.
   */
  calculateTimeDifference() {
    const currentDate = new Date();
    const timeDifference = this.eventDate.getTime() - currentDate.getTime();

    if (timeDifference < 0) {
      throw new Error("Event date has passed.");
    }

    const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

    return { days, hours, minutes, seconds };
  }

  /**
   * Method to update the display element with the countdown.
   */
  updateDisplay() {
    try {
      const timeDifference = this.calculateTimeDifference();
      const countdownString = `${this.padZero(timeDifference.days)} days, ${this.padZero(timeDifference.hours)} hours, ${this.padZero(timeDifference.minutes)} minutes, ${this.padZero(timeDifference.seconds)} seconds`;
      this.displayElement.textContent = countdownString;
    } catch (error) {
      this.displayElement.textContent = error.message;
    }
  }

  /**
   * Method to pad a number with a leading zero if it's less than 10.
   * @param {number} number - The number to pad.
   * @returns {string} - The padded number as a string.
   */
  padZero(number) {
    return (number < 10 ? "0" : "") + number;
  }

  /**
   * Method to start the countdown interval.
   */
  startCountdown() {
    this.updateDisplay();
    setInterval(() => {
      this.updateDisplay();
    }, 1000);
  }
}

// Example usage:
const eventDate = new Date("2024-09-17T14:30:00");
const displayElement = document.getElementById("countdown-display");

const countdownTimer = new CountdownTimer(eventDate, displayElement);
countdownTimer.startCountdown();
```
