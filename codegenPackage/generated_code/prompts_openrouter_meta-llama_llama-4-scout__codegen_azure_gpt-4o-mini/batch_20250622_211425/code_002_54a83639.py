"""
Generated Code Metadata:
========================
Original URL: https://is2btc.com
Prompt: Generate JavaScript code to create a simple countdown timer, similar to the 60-second reload timer on https://is2btc.com, for a cryptocurrency faucet project.
Generated: DETERMINISTIC_54a83639a5f482df
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Countdown Timer Class
class CountdownTimer {
    constructor(duration, displayElement) {
        this.duration = duration; // Duration in seconds
        this.displayElement = displayElement; // HTML element to display the timer
        this.timer = null; // Timer reference
        this.remainingTime = duration; // Remaining time in seconds
    }

    // Start the countdown
    start() {
        this.remainingTime = this.duration; // Reset remaining time
        this.updateDisplay(); // Update display immediately
        this.timer = setInterval(() => {
            this.tick(); // Call tick method every second
        }, 1000);
    }

    // Tick method to update the timer
    tick() {
        if (this.remainingTime > 0) {
            this.remainingTime--; // Decrease remaining time
            this.updateDisplay(); // Update display
        } else {
            this.stop(); // Stop the timer when it reaches zero
        }
    }

    // Update the display element with the remaining time
    updateDisplay() {
        const minutes = Math.floor(this.remainingTime / 60);
        const seconds = this.remainingTime % 60;
        this.displayElement.textContent = `${this.pad(minutes)}:${this.pad(seconds)}`; // Format time
    }

    // Pad single digit numbers with leading zero
    pad(number) {
        return number < 10 ? `0${number}` : number;
    }

    // Stop the countdown
    stop() {
        clearInterval(this.timer); // Clear the timer
        this.timer = null; // Reset timer reference
        this.displayElement.textContent = "Time's up!"; // Display message
    }
}

// Initialize the countdown timer
document.addEventListener("DOMContentLoaded", () => {
    const displayElement = document.getElementById("countdown"); // Get the display element
    const countdownDuration = 60; // Set countdown duration (60 seconds)
    
    // Check if the display element exists
    if (!displayElement) {
        console.error("Display element not found!"); // Log error if element is missing
        return;
    }

    const countdownTimer = new CountdownTimer(countdownDuration, displayElement); // Create a new timer instance
    countdownTimer.start(); // Start the countdown
});
```

```html
<!-- HTML Structure -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Countdown Timer</title>
    <style>
        #countdown {
            font-size: 2em; /* Style for the countdown display */
            text-align: center; /* Center the text */
            margin-top: 20%; /* Margin from the top */
        }
    </style>
</head>
<body>
    <div id="countdown">01:00</div> <!-- Countdown display -->
    <script src="countdown.js"></script> <!-- Link to the JavaScript file -->
</body>
</html>
```
