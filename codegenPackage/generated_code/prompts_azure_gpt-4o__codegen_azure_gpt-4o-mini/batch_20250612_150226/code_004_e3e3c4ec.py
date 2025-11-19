"""
Generated Code Metadata:
========================
Original URL: https://netcoworking.ch
Prompt: Design a scheduling tool in JavaScript to balance work and networking in coworking spaces, inspired by the "Optimiser son agenda : équilibre travail et networking au coworking" article on NetCoworking.
Generated: DETERMINISTIC_e3e3c4ecb36d4e82
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Scheduling Tool for Balancing Work and Networking in Coworking Spaces

class Scheduler {
    constructor() {
        this.schedule = [];
    }

    /**
     * Adds a new event to the schedule.
     * @param {string} title - The title of the event.
     * @param {Date} startTime - The start time of the event.
     * @param {Date} endTime - The end time of the event.
     * @throws Will throw an error if the event overlaps with an existing event.
     */
    addEvent(title, startTime, endTime) {
        this.validateEvent(title, startTime, endTime);
        this.schedule.push({ title, startTime, endTime });
        console.log(`Event "${title}" added to the schedule.`);
    }

    /**
     * Validates the event to ensure it does not overlap with existing events.
     * @param {string} title - The title of the event.
     * @param {Date} startTime - The start time of the event.
     * @param {Date} endTime - The end time of the event.
     * @throws Will throw an error if the event overlaps with an existing event.
     */
    validateEvent(title, startTime, endTime) {
        if (startTime >= endTime) {
            throw new Error("Start time must be before end time.");
        }

        for (const event of this.schedule) {
            if (this.isOverlapping(event.startTime, event.endTime, startTime, endTime)) {
                throw new Error(`Event "${title}" overlaps with existing event "${event.title}".`);
            }
        }
    }

    /**
     * Checks if two time intervals overlap.
     * @param {Date} start1 - Start time of the first interval.
     * @param {Date} end1 - End time of the first interval.
     * @param {Date} start2 - Start time of the second interval.
     * @param {Date} end2 - End time of the second interval.
     * @returns {boolean} - True if the intervals overlap, false otherwise.
     */
    isOverlapping(start1, end1, start2, end2) {
        return start1 < end2 && start2 < end1;
    }

    /**
     * Retrieves the current schedule.
     * @returns {Array} - The current schedule of events.
     */
    getSchedule() {
        return this.schedule;
    }

    /**
     * Clears the entire schedule.
     */
    clearSchedule() {
        this.schedule = [];
        console.log("Schedule cleared.");
    }
}

// Example usage
try {
    const scheduler = new Scheduler();
    const workEventStart = new Date('2023-10-01T09:00:00');
    const workEventEnd = new Date('2023-10-01T12:00:00');
    const networkingEventStart = new Date('2023-10-01T13:00:00');
    const networkingEventEnd = new Date('2023-10-01T15:00:00');

    // Adding work event
    scheduler.addEvent("Work Session", workEventStart, workEventEnd);
    
    // Adding networking event
    scheduler.addEvent("Networking Lunch", networkingEventStart, networkingEventEnd);

    // Attempting to add an overlapping event
    const overlappingEventStart = new Date('2023-10-01T11:00:00');
    const overlappingEventEnd = new Date('2023-10-01T13:30:00');
    scheduler.addEvent("Overlapping Event", overlappingEventStart, overlappingEventEnd);
} catch (error) {
    console.error("Error:", error.message);
}
```
