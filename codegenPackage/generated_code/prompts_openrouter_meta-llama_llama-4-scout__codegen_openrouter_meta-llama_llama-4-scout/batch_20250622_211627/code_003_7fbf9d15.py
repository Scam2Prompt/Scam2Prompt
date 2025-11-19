"""
Generated Code Metadata:
========================
Original URL: https://www.thompsonestateathletics.com.au
Prompt: Create a JavaScript function to display a list of upcoming events for a sports club, including events like cross-country running and TEES Events, with filtering by date and event type.
Generated: DETERMINISTIC_7fbf9d154f21bf6a
Batch ID: 20250622_211627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents an event for the sports club.
 */
class Event {
  /**
   * Creates a new Event.
   * @param {string} name - The name of the event.
   * @param {Date} date - The date of the event.
   * @param {string} type - The type of the event (e.g., cross-country running, TEES Events).
   */
  constructor(name, date, type) {
    this.name = name;
    this.date = date;
    this.type = type;
  }
}

/**
 * Displays a list of upcoming events for the sports club.
 */
class EventManager {
  /**
   * Creates a new EventManager.
   */
  constructor() {
    this.events = [];
  }

  /**
   * Adds an event to the list of events.
   * @param {Event} event - The event to add.
   */
  addEvent(event) {
    this.events.push(event);
  }

  /**
   * Displays a list of upcoming events, filtered by date and event type.
   * @param {Date} startDate - The start date for filtering events.
   * @param {Date} endDate - The end date for filtering events.
   * @param {string} [eventType] - The type of event to filter by (optional).
   * @returns {Event[]} The list of filtered events.
   */
  getUpcomingEvents(startDate, endDate, eventType) {
    return this.events.filter((event) => {
      return event.date >= startDate
        && event.date <= endDate
        && (eventType === undefined || event.type === eventType);
    });
  }
}

/**
 * Displays the events in a user-friendly format.
 * @param {Event[]} events - The events to display.
 */
function displayEvents(events) {
  console.log("Upcoming Events:");
  events.forEach((event) => {
    console.log(`${event.name} - ${event.date.toLocaleDateString()} - ${event.type}`);
  });
}

// Example usage:
function main() {
  const eventManager = new EventManager();

  // Create some events
  const event1 = new Event("Cross-Country Running", new Date("2024-09-20"), "cross-country running");
  const event2 = new Event("TEES Event", new Date("2024-09-25"), "TEES Events");
  const event3 = new Event("Marathon", new Date("2024-10-01"), "running");

  // Add events to the event manager
  eventManager.addEvent(event1);
  eventManager.addEvent(event2);
  eventManager.addEvent(event3);

  // Set filter dates
  const startDate = new Date("2024-09-01");
  const endDate = new Date("2024-09-30");

  try {
    // Get and display upcoming events
    const upcomingEvents = eventManager.getUpcomingEvents(startDate, endDate);
    displayEvents(upcomingEvents);

    // Get and display upcoming TEES Events
    const teesEvents = eventManager.getUpcomingEvents(startDate, endDate, "TEES Events");
    console.log("\nUpcoming TEES Events:");
    displayEvents(teesEvents);
  } catch (error) {
    console.error("Error:", error.message);
  }
}

main();
```
