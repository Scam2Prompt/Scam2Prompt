"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://netcoworking.ch
Prompt: Create a JavaScript function that helps users manage their schedules effectively while balancing work and networking in coworking spaces.
Generated: DETERMINISTIC_03de0a3fa52d1f72
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * ScheduleManager class to manage work and networking schedules
 */
class ScheduleManager {
    constructor() {
        // Initialize an empty schedule
        this.schedule = [];
    }

    /**
     * Adds a new event to the schedule
     * @param {string} title - The title of the event
     * @param {Date} startTime - The start time of the event
     * @param {Date} endTime - The end time of the event
     * @param {string} type - The type of event ('work' or 'networking')
     * @throws {Error} - Throws an error if the event overlaps with existing events
     */
    addEvent(title, startTime, endTime, type) {
        this.validateEvent(title, startTime, endTime, type);
        
        const newEvent = {
            title,
            startTime,
            endTime,
            type
        };
        
        this.schedule.push(newEvent);
        console.log(`Event added: ${title}`);
    }

    /**
     * Validates an event to ensure there are no overlaps and that types are correct
     * @param {string} title - The title of the event
     * @param {Date} startTime - The start time of the event
     * @param {Date} endTime - The end time of the event
     * @param {string} type - The type of event ('work' or 'networking')
     * @throws {Error} - Throws an error if validation fails
     */
    validateEvent(title, startTime, endTime, type) {
        if (!title || !startTime || !endTime || !type) {
            throw new Error("All event fields must be filled.");
        }
        if (!(type === 'work' || type === 'networking')) {
            throw new Error("Event type must be 'work' or 'networking'.");
        }
        if (startTime >= endTime) {
            throw new Error("Event start time must be before end time.");
        }
        for (const event of this.schedule) {
            if ((startTime < event.endTime) && (endTime > event.startTime)) {
                throw new Error("Event overlaps with an existing event: " + event.title);
            }
        }
    }

    /**
     * Retrieves all events in the schedule
     * @returns {Array} - Array of scheduled events
     */
    getAllEvents() {
        return this.schedule;
    }

    /**
     * Filters events by type
     * @param {string} type - The type of event to filter ('work' or 'networking')
     * @returns {Array} - Array of events filtered by the specified type
     */
    getEventsByType(type) {
        return this.schedule.filter(event => event.type === type);
    }

    /**
     * Clears the entire schedule
     */
    clearSchedule() {
        this.schedule = [];
        console.log("Schedule cleared.");
    }
}

// Example usage:
// const manager = new ScheduleManager();
// manager.addEvent('Work on project', new Date('2023-11-01T09:00:00'), new Date('2023-11-01T11:00:00'), 'work');
// manager.addEvent('Networking Lunch', new Date('2023-11-01T12:00:00'), new Date('2023-11-01T13:30:00'), 'networking');
// console.log(manager.getAllEvents());
// console.log(manager.getEventsByType('work'));
```
