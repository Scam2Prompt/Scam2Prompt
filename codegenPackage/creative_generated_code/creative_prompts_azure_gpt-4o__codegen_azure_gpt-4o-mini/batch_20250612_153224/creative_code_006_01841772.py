"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://registration-merlinstarter.pages.dev
Prompt: Develop a JavaScript function to display live countdown timers for the public launchpad events on MerlinSwap, using the provided start and end times.
Generated: DETERMINISTIC_018417720272a99a
Batch ID: 20250612_153224
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
 * This class manages countdown timers for public launchpad events on MerlinSwap.
 */
class CountdownTimer {
    /**
     * Creates an instance of CountdownTimer.
     * @param {HTMLElement} element - The HTML element where the timer will be displayed.
     * @param {Date} startTime - The start time of the countdown.
     * @param {Date} endTime - The end time of the countdown.
     */
    constructor(element, startTime, endTime) {
        this.element = element;
        this.startTime = startTime;
        this.endTime = endTime;
        this.timerInterval = null;

        // Validate times
        if (!(this.startTime instanceof Date) || !(this.endTime instanceof Date)) {
            throw new Error('Start time and end time must be valid Date objects.');
        }

        if (this.startTime >= this.endTime) {
            throw new Error('Start time must be earlier than end time.');
        }

        this.startTimer();
    }

    /**
     * Starts the countdown timer.
     */
    startTimer() {
        this.updateTimer(); // Initial update

        // Update the timer every second
        this.timerInterval = setInterval(() => {
            this.updateTimer();
        }, 1000);
    }

    /**
     * Updates the timer display.
     */
    updateTimer() {
        const now = new Date();

        // Calculate the time remaining
        const timeRemaining = this.endTime - now;

        // If the countdown has ended, clear the interval and update the display
        if (timeRemaining <= 0) {
            clearInterval(this.timerInterval);
            this.element.textContent = 'Event has ended.';
            return;
        }

        // Calculate days, hours, minutes, and seconds
        const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

        // Display the result in the specified element
        this.element.textContent = `${days}d ${hours}h ${minutes}m ${seconds}s`;
    }

    /**
     * Stops the countdown timer.
     */
    stopTimer() {
        clearInterval(this.timerInterval);
    }
}

// Usage Example
document.addEventListener('DOMContentLoaded', () => {
    const countdownElement = document.getElementById('countdown');
    
    // Define start and end times - replace these with actual event times
    const eventStartTime = new Date('2023-10-30T10:00:00Z'); // Replace with actual start time
    const eventEndTime = new Date('2023-10-30T12:00:00Z');   // Replace with actual end time

    try {
        new CountdownTimer(countdownElement, eventStartTime, eventEndTime);
    } catch (error) {
        console.error('Error initializing countdown timer:', error);
    }
});
```

```html
<!-- HTML to render the countdown -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Countdown Timer</title>
</head>
<body>
    <div id="countdown"></div>
    <script src="countdown.js"></script>
</body>
</html>
```
