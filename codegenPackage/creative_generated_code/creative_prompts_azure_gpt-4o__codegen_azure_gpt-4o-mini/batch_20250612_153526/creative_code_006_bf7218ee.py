"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pacm.pages.dev
Prompt: Create a JavaScript function to display real-time countdowns for multiple events, similar to the Pacmoon airdrop timers.
Generated: DETERMINISTIC_bf7218ee6af08692
Batch ID: 20250612_153526
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
 * Provides functionality to create and manage multiple countdown timers for events.
 */
class CountdownTimer {
    constructor(eventName, endTime) {
        this.eventName = eventName; // Name of the event
        this.endTime = new Date(endTime).getTime(); // End time in milliseconds
        this.interval = null; // Store interval ID for cleanup
        this.displayElement = null; // Element to display countdown
    }

    /**
     * Initialize the countdown timer by setting up the DOM element and starting the timer.
     * @param {HTMLElement} displayElement - The DOM element where the countdown will be displayed.
     */
    init(displayElement) {
        this.displayElement = displayElement;
        this.startCountdown();
    }

    /**
     * Start the countdown timer.
     */
    startCountdown() {
        // Update the countdown every second
        this.interval = setInterval(() => {
            const now = Date.now(); // Get current time
            const distance = this.endTime - now; // Calculate remaining time

            // Calculate time units
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            // Display the result in the specified element
            this.displayElement.innerHTML = `
                ${this.eventName}: ${days}d ${hours}h ${minutes}m ${seconds}s
            `;

            // If the countdown is finished, stop the timer and display a message
            if (distance < 0) {
                clearInterval(this.interval);
                this.displayElement.innerHTML = `${this.eventName} has ended!`;
            }
        }, 1000);
    }

    /**
     * Clear the countdown interval if it exists.
     */
    clearTimer() {
        if (this.interval) {
            clearInterval(this.interval);
            this.interval = null;
        }
    }
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
    // Sample events with names and end times
    const events = [
        { name: 'Event 1', endTime: '2023-12-31T23:59:59Z' },
        { name: 'Event 2', endTime: '2024-01-15T12:00:00Z' },
        { name: 'Event 3', endTime: '2024-02-01T08:30:00Z' }
    ];

    // Create and initialize countdown timers for each event
    events.forEach(event => {
        const timer = new CountdownTimer(event.name, event.endTime);
        const displayElement = document.createElement('div');
        document.body.appendChild(displayElement);
        timer.init(displayElement);
    });
});
```
