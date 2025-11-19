"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dacarlaw.com
Prompt: Provide an example of a JavaScript function that updates a countdown timer in real-time on a website.
Generated: DETERMINISTIC_1958e490c00b5773
Batch ID: 20250612_162101
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Countdown Timer Class
 * This class manages the countdown timer and updates the display in real-time.
 */
class CountdownTimer {
    constructor(duration, displayElementId) {
        this.duration = duration; // Duration in seconds
        this.displayElement = document.getElementById(displayElementId);
        this.intervalId = null; // To hold the interval ID for clearing later
    }

    /**
     * Start the countdown timer
     * Initiates the countdown and updates the display every second.
     */
    start() {
        this.clearExistingTimer(); // Clear any existing timer

        let remainingTime = this.duration;

        // Update the display immediately
        this.updateDisplay(remainingTime);

        // Start the countdown
        this.intervalId = setInterval(() => {
            remainingTime--;

            if (remainingTime <= 0) {
                this.stop(); // Stop timer when countdown reaches zero
            } else {
                this.updateDisplay(remainingTime); // Update display
            }
        }, 1000); // 1000ms = 1 second
    }

    /**
     * Stop the countdown timer
     * Clears the interval and updates the display to show "00:00".
     */
    stop() {
        this.clearExistingTimer();
        this.updateDisplay(0); // Display time as zero
    }

    /**
     * Clear existing timer
     * Clears the current interval if it exists to prevent multiple intervals from running.
     */
    clearExistingTimer() {
        if (this.intervalId) {
            clearInterval(this.intervalId);
            this.intervalId = null;
        }
    }

    /**
     * Update the display of the countdown timer
     * Formats the remaining time into MM:SS format and updates the display element.
     * @param {number} seconds - The number of seconds remaining.
     */
    updateDisplay(seconds) {
        const minutes = Math.floor(seconds / 60);
        const secs = seconds % 60;
        const formattedTime = `${this.padZero(minutes)}:${this.padZero(secs)}`;
        this.displayElement.textContent = formattedTime; // Update the display
    }

    /**
     * Pad single digit numbers with a leading zero
     * @param {number} number - The number to pad.
     * @returns {string} - The padded number as a string.
     */
    padZero(number) {
        return number < 10 ? `0${number}` : number.toString();
    }
}

// Example usage:
// Initialize the countdown timer for 5 minutes (300 seconds) and attach to element with id 'timer'.
const countdown = new CountdownTimer(300, 'timer');
countdown.start(); // Start the timer

// HTML structure necessary for the timer to work:
// <div id="timer"></div>
```
