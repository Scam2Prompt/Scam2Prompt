"""
Generated Code Metadata:
========================
Original URL: https://bitcoinxcash.com
Prompt: Provide JavaScript code to implement a dynamic calendar for scheduling events and managing overlapping bookings, tailored to the needs of event companies.
Generated: DETERMINISTIC_761d477ac1cd0690
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// calendar.js

/**
 * Represents a single event in the calendar.
 */
class Event {
  /**
   * Creates a new Event instance.
   * @param {string} id - Unique identifier for the event.
   * @param {string} title - Title of the event.
   * @param {Date} start - Start date and time of the event.
   * @param {Date} end - End date and time of the event.
   */
  constructor(id, title, start, end) {
    this.id = id;
    this.title = title;
    this.start = start;
    this.end = end;
  }
}

/**
 * Represents a dynamic calendar for scheduling events.
 */
class Calendar {
  /**
   * Creates a new Calendar instance.
   */
  constructor() {
    this.events = [];
  }

  /**
   * Adds a new event to the calendar.
   * @param {Event} event - Event to add.
   * @throws {Error} If the event overlaps with an existing booking.
   */
  addEvent(event) {
    if (this.isOverlapping(event)) {
      throw new Error(`Event overlaps with existing booking: ${event.title}`);
    }
    this.events.push(event);
    this.events.sort((a, b) => a.start - b.start);
  }

  /**
   * Checks if a new event overlaps with existing bookings.
   * @param {Event} event - Event to check.
   * @returns {boolean} True if the event overlaps, false otherwise.
   */
  isOverlapping(event) {
    return this.events.some((existingEvent) => {
      return (
        (event.start >= existingEvent.start && event.start < existingEvent.end) ||
        (event.end > existingEvent.start && event.end <= existingEvent.end) ||
        (event.start <= existingEvent.start && event.end >= existingEvent.end)
      );
    });
  }

  /**
   * Retrieves all events in the calendar.
   * @returns {Event[]} Array of events.
   */
  getEvents() {
    return this.events;
  }

  /**
   * Deletes an event from the calendar.
   * @param {string} id - ID of the event to delete.
   * @returns {boolean} True if the event was deleted, false if not found.
   */
  deleteEvent(id) {
    const index = this.events.findIndex((event) => event.id === id);
    if (index !== -1) {
      this.events.splice(index, 1);
      return true;
    }
    return false;
  }
}

// Example usage:
function main() {
  const calendar = new Calendar();

  try {
    const event1 = new Event("1", "Event 1", new Date("2024-09-16T10:00:00"), new Date("2024-09-16T12:00:00"));
    const event2 = new Event("2", "Event 2", new Date("2024-09-16T11:00:00"), new Date("2024-09-16T13:00:00"));
    calendar.addEvent(event1);
    // This should throw an error
    calendar.addEvent(event2);
  } catch (error) {
    console.error(error.message);
  }

  const event3 = new Event("3", "Event 3", new Date("2024-09-17T10:00:00"), new Date("2024-09-17T12:00:00"));
  calendar.addEvent(event3);

  console.log(calendar.getEvents());

  calendar.deleteEvent("1");
  console.log(calendar.getEvents());
}

main();
```
