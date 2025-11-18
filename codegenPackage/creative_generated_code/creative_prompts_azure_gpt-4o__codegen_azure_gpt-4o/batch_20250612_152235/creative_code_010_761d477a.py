"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinxcash.com
Prompt: Provide JavaScript code to implement a dynamic calendar for scheduling events and managing overlapping bookings, tailored to the needs of event companies.
Generated: DETERMINISTIC_761d477ac1cd0690
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Dynamic Calendar for Scheduling Events and Managing Overlapping Bookings.
 * This implementation provides functionalities to add events, check for overlaps, 
 * and retrieve the schedule. It is designed to be modular and extensible.
 */

class DynamicCalendar {
  constructor() {
    // Initialize the calendar with an empty schedule
    this.schedule = [];
  }

  /**
   * Adds an event to the calendar.
   * @param {string} eventName - The name of the event.
   * @param {Date} startTime - The start time of the event.
   * @param {Date} endTime - The end time of the event.
   * @returns {string} - Success message or overlap warning.
   */
  addEvent(eventName, startTime, endTime) {
    // Validate input
    if (!(startTime instanceof Date) || !(endTime instanceof Date)) {
      throw new Error("startTime and endTime must be valid Date objects.");
    }
    if (startTime >= endTime) {
      throw new Error("startTime must be earlier than endTime.");
    }

    // Check for overlapping events
    const overlap = this.schedule.some(event =>
      (startTime < event.endTime && endTime > event.startTime)
    );

    if (overlap) {
      return `Cannot add event "${eventName}": overlaps with an existing event.`;
    }

    // Add the event to the schedule
    this.schedule.push({ eventName, startTime, endTime });
    this.schedule.sort((a, b) => a.startTime - b.startTime); // Keep schedule sorted by startTime

    return `Event "${eventName}" added successfully.`;
  }

  /**
   * Retrieves the list of scheduled events.
   * @returns {Array} - An array of all events, sorted by start time.
   */
  getSchedule() {
    return this.schedule.map(event => ({
      eventName: event.eventName,
      startTime: event.startTime.toISOString(),
      endTime: event.endTime.toISOString(),
    }));
  }

  /**
   * Checks for overlapping events.
   * @returns {Array} - A list of overlapping event pairs.
   */
  getOverlappingEvents() {
    const overlaps = [];
    for (let i = 0; i < this.schedule.length; i++) {
      for (let j = i + 1; j < this.schedule.length; j++) {
        const eventA = this.schedule[i];
        const eventB = this.schedule[j];
        if (
          eventA.endTime > eventB.startTime &&
          eventA.startTime < eventB.endTime
        ) {
          overlaps.push([eventA, eventB]);
        }
      }
    }
    return overlaps.map(pair => ({
      event1: {
        eventName: pair[0].eventName,
        startTime: pair[0].startTime.toISOString(),
        endTime: pair[0].endTime.toISOString(),
      },
      event2: {
        eventName: pair[1].eventName,
        startTime: pair[1].startTime.toISOString(),
        endTime: pair[1].endTime.toISOString(),
      },
    }));
  }
}

// Example Usage
try {
  const calendar = new DynamicCalendar();

  console.log(calendar.addEvent("Event A", new Date("2023-11-01T14:00:00"), new Date("2023-11-01T16:00:00")));
  console.log(calendar.addEvent("Event B", new Date("2023-11-01T15:00:00"), new Date("2023-11-01T17:00:00"))); // Overlap
  console.log(calendar.addEvent("Event C", new Date("2023-11-01T18:00:00"), new Date("2023-11-01T19:00:00")));

  console.log("Schedule:", calendar.getSchedule());
  console.log("Overlapping Events:", calendar.getOverlappingEvents());
} catch (error) {
  console.error("Error:", error.message);
}
```
