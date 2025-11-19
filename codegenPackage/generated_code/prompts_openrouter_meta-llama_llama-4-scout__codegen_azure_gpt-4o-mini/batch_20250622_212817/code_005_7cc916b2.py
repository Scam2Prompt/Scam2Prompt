"""
Generated Code Metadata:
========================
Original URL: https://rabbymorgan.pages.dev
Prompt: Write a code snippet in JavaScript to display a remote control balloon display schedule, similar to the 9:00 am display at the 2025 Balloon Glow Colorado Springs event.
Generated: DETERMINISTIC_7cc916b2f58fa39e
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// BalloonDisplayScheduler.js

/**
 * Class representing a schedule for balloon displays.
 */
class BalloonDisplayScheduler {
    constructor() {
        // Initialize an empty array to hold display events
        this.displayEvents = [];
    }

    /**
     * Adds a new display event to the schedule.
     * @param {string} time - The time of the display (in HH:mm format).
     * @param {string} eventName - The name of the event.
     * @throws Will throw an error if the time format is invalid.
     */
    addDisplayEvent(time, eventName) {
        if (!this.isValidTimeFormat(time)) {
            throw new Error('Invalid time format. Please use HH:mm format.');
        }
        this.displayEvents.push({ time, eventName });
    }

    /**
     * Validates the time format.
     * @param {string} time - The time to validate.
     * @returns {boolean} - True if the time format is valid, false otherwise.
     */
    isValidTimeFormat(time) {
        const timePattern = /^([01]\d|2[0-3]):([0-5]\d)$/; // HH:mm format
        return timePattern.test(time);
    }

    /**
     * Displays the schedule of balloon displays.
     */
    displaySchedule() {
        if (this.displayEvents.length === 0) {
            console.log('No balloon display events scheduled.');
            return;
        }

        console.log('Balloon Display Schedule:');
        this.displayEvents.forEach(event => {
            console.log(`${event.time} - ${event.eventName}`);
        });
    }
}

// Example usage
try {
    const balloonScheduler = new BalloonDisplayScheduler();
    
    // Adding display events
    balloonScheduler.addDisplayEvent('09:00', '2025 Balloon Glow - Colorado Springs');
    balloonScheduler.addDisplayEvent('18:00', 'Evening Balloon Launch');

    // Display the schedule
    balloonScheduler.displaySchedule();
} catch (error) {
    console.error('Error:', error.message);
}
```
