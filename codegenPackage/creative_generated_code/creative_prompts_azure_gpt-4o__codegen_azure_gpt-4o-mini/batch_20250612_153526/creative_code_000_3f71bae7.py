"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pacm.pages.dev
Prompt: Write JavaScript code to create a countdown timer for an event, similar to the "Airdrop Season 3 Ends" timer on the Pacmoon website.
Generated: DETERMINISTIC_3f71bae70f6ce8c8
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Countdown Timer for an Event
// This code creates a countdown timer that updates every second and displays the time remaining until a specified event.

class CountdownTimer {
    constructor(endTime) {
        // Validate the end time input
        if (!(endTime instanceof Date) || isNaN(endTime)) {
            throw new Error("Invalid end time provided. Please provide a valid Date object.");
        }
        this.endTime = endTime;
        this.timerId = null;
    }

    // Start the countdown timer
    start(displayElement) {
        // Validate the display element
        if (!(displayElement instanceof HTMLElement)) {
            throw new Error("Invalid display element. Please provide a valid HTML element.");
        }
        
        // Initial call to display the timer
        this.updateTimer(displayElement);

        // Update the timer every second
        this.timerId = setInterval(() => this.updateTimer(displayElement), 1000);
    }

    // Update the timer display
    updateTimer(displayElement) {
        const now = new Date();
        const timeRemaining = this.endTime - now;

        // Calculate time components
        const seconds = Math.floor((timeRemaining / 1000) % 60);
        const minutes = Math.floor((timeRemaining / 1000 / 60) % 60);
        const hours = Math.floor((timeRemaining / (1000 * 60 * 60)) % 24);
        const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));

        // Format the output
        displayElement.innerHTML = `
            ${this.padZero(days)} Days 
            ${this.padZero(hours)} Hours 
            ${this.padZero(minutes)} Minutes 
            ${this.padZero(seconds)} Seconds
        `;

        // Stop the timer if the countdown has finished
        if (timeRemaining <= 0) {
            clearInterval(this.timerId);
            displayElement.innerHTML = "Event has ended!";
        }
    }

    // Pad single digit numbers with a leading zero
    padZero(num) {
        return num < 10 ? `0${num}` : num;
    }

    // Stop the countdown timer
    stop() {
        if (this.timerId) {
            clearInterval(this.timerId);
        }
    }
}

// Example usage
const endDate = new Date('2023-12-31T23:59:59'); // Set the event end date and time
const countdownDisplay = document.getElementById('countdown'); // Ensure there is an element with this id in your HTML

try {
    const timer = new CountdownTimer(endDate);
    timer.start(countdownDisplay);
} catch (error) {
    console.error(error.message);
}
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Countdown Timer</title>
</head>
<body>
    <div id="countdown"></div>
    <script src="path/to/your/countdown-timer.js"></script> <!-- Link to your JavaScript file -->
</body>
</html>
```
