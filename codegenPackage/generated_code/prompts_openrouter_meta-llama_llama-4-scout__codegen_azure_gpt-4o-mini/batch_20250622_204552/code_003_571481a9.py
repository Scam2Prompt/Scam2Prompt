"""
Generated Code Metadata:
========================
Original URL: https://test.emergence-dev.pages.dev
Prompt: Create a JavaScript code snippet for a countdown timer similar to the one used on the Emergence website for the event.
Generated: DETERMINISTIC_571481a937543a0d
Batch ID: 20250622_204552
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
    constructor(endTime) {
        this.endTime = new Date(endTime).getTime();
        this.timerId = null;
        this.initialize();
    }

    // Initialize the countdown
    initialize() {
        this.updateTimer();
        this.startTimer();
    }

    // Start the countdown timer
    startTimer() {
        this.timerId = setInterval(() => {
            this.updateTimer();
        }, 1000);
    }

    // Update the timer display
    updateTimer() {
        const now = new Date().getTime();
        const distance = this.endTime - now;

        // Calculate time components
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result in the element with id="countdown"
        const countdownElement = document.getElementById("countdown");
        if (countdownElement) {
            countdownElement.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;
        } else {
            console.error("Countdown element not found");
        }

        // If the countdown is finished, display a message
        if (distance < 0) {
            clearInterval(this.timerId);
            if (countdownElement) {
                countdownElement.innerHTML = "Event has started!";
            }
        }
    }

    // Stop the countdown timer
    stopTimer() {
        clearInterval(this.timerId);
    }
}

// Usage example
document.addEventListener("DOMContentLoaded", () => {
    // Set the countdown end time (YYYY-MM-DD HH:MM:SS)
    const eventDate = "2023-12-31T23:59:59";
    const countdown = new CountdownTimer(eventDate);
});
```

```html
<!-- HTML structure for the countdown timer -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Countdown Timer</title>
</head>
<body>
    <div id="countdown" style="font-size: 2em; font-weight: bold;"></div>
    <script src="countdown.js"></script> <!-- Link to the JavaScript file -->
</body>
</html>
```
