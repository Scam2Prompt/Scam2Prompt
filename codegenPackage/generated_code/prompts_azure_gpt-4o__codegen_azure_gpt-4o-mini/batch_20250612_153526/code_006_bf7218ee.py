"""
Generated Code Metadata:
========================
Original URL: https://pacm.pages.dev
Prompt: Create a JavaScript function to display real-time countdowns for multiple events, similar to the Pacmoon airdrop timers.
Generated: DETERMINISTIC_bf7218ee6af08692
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Countdown Timer Class
 * This class manages multiple countdown timers for different events.
 */
class CountdownTimer {
    constructor(eventName, endTime) {
        this.eventName = eventName; // Name of the event
        this.endTime = new Date(endTime).getTime(); // End time in milliseconds
        this.timerId = null; // Timer ID for clearing the interval
    }

    /**
     * Start the countdown timer
     */
    start() {
        // Check if the end time is in the past
        if (this.endTime < Date.now()) {
            console.error(`Error: The end time for ${this.eventName} is in the past.`);
            return;
        }

        this.update(); // Initial call to display the countdown
        this.timerId = setInterval(() => this.update(), 1000); // Update every second
    }

    /**
     * Update the countdown display
     */
    update() {
        const now = Date.now();
        const distance = this.endTime - now; // Calculate remaining time

        // Calculate time components
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result
        const countdownDisplay = `${this.eventName}: ${days}d ${hours}h ${minutes}m ${seconds}s`;
        console.log(countdownDisplay);

        // If the countdown is finished, clear the interval and notify
        if (distance < 0) {
            clearInterval(this.timerId);
            console.log(`${this.eventName} has ended!`);
        }
    }

    /**
     * Stop the countdown timer
     */
    stop() {
        clearInterval(this.timerId);
    }
}

/**
 * Function to initialize and start countdown timers for multiple events
 * @param {Array} events - Array of event objects with name and end time
 */
function initializeCountdowns(events) {
    if (!Array.isArray(events) || events.length === 0) {
        console.error("Error: Invalid events array.");
        return;
    }

    events.forEach(event => {
        if (!event.name || !event.endTime) {
            console.error("Error: Each event must have a name and endTime.");
            return;
        }
        const timer = new CountdownTimer(event.name, event.endTime);
        timer.start();
    });
}

// Example usage
const events = [
    { name: "Event 1", endTime: "2023-12-31T23:59:59Z" },
    { name: "Event 2", endTime: "2023-11-30T12:00:00Z" },
    { name: "Event 3", endTime: "2023-10-15T15:30:00Z" }
];

// Initialize countdowns for the specified events
initializeCountdowns(events);
```
