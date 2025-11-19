"""
Generated Code Metadata:
========================
Original URL: https://cle.com
Prompt: Generate a code snippet in JavaScript to create a simple conference calendar, using the CLE International conference schedule as an example.
Generated: DETERMINISTIC_228a4cd30f422d6b
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ConferenceCalendar.js

/**
 * Represents a Conference Calendar.
 */
class ConferenceCalendar {
  /**
   * Initializes a new instance of the ConferenceCalendar class.
   */
  constructor() {
    // Initialize an empty schedule.
    this.schedule = [];
  }

  /**
   * Adds a new event to the conference schedule.
   * 
   * @param {string} title - The title of the event.
   * @param {Date} startDate - The start date and time of the event.
   * @param {Date} endDate - The end date and time of the event.
   * @param {string} location - The location of the event.
   */
  addEvent(title, startDate, endDate, location) {
    // Validate input parameters.
    if (!title || !startDate || !endDate || !location) {
      throw new Error("All parameters are required.");
    }

    // Check if start date is before end date.
    if (startDate >= endDate) {
      throw new Error("Start date must be before end date.");
    }

    // Create a new event.
    const event = {
      title,
      startDate,
      endDate,
      location,
    };

    // Add event to the schedule.
    this.schedule.push(event);

    // Sort the schedule by start date.
    this.schedule.sort((a, b) => a.startDate - b.startDate);
  }

  /**
   * Removes an event from the conference schedule.
   * 
   * @param {string} title - The title of the event to remove.
   */
  removeEvent(title) {
    // Find the index of the event to remove.
    const index = this.schedule.findIndex((event) => event.title === title);

    // Check if event exists.
    if (index === -1) {
      throw new Error(`Event '${title}' not found.`);
    }

    // Remove the event from the schedule.
    this.schedule.splice(index, 1);
  }

  /**
   * Displays the conference schedule.
   */
  displaySchedule() {
    // Check if schedule is empty.
    if (this.schedule.length === 0) {
      console.log("The conference schedule is empty.");
      return;
    }

    // Display each event in the schedule.
    console.log("Conference Schedule:");
    this.schedule.forEach((event) => {
      console.log(`Title: ${event.title}`);
      console.log(`Date: ${event.startDate.toLocaleString()} - ${event.endDate.toLocaleString()}`);
      console.log(`Location: ${event.location}`);
      console.log("------------------------");
    });
  }
}

// Example usage.
function main() {
  try {
    // Create a new conference calendar.
    const calendar = new ConferenceCalendar();

    // Add events to the CLE International conference schedule.
    calendar.addEvent(
      "CLE International Conference Opening",
      new Date("2024-03-10T08:00:00"),
      new Date("2024-03-10T09:00:00"),
      "Manchester Conference Centre"
    );

    calendar.addEvent(
      "Keynote: AI in Law",
      new Date("2024-03-10T09:00:00"),
      new Date("2024-03-10T10:00:00"),
      "Manchester Conference Centre, Main Auditorium"
    );

    calendar.addEvent(
      "Breakout Session: Legal Tech Startups",
      new Date("2024-03-10T10:30:00"),
      new Date("2024-03-10T11:30:00"),
      "Manchester Conference Centre, Room 3"
    );

    // Display the conference schedule.
    calendar.displaySchedule();

    // Remove an event from the schedule.
    calendar.removeEvent("Keynote: AI in Law");

    // Display the updated conference schedule.
    console.log("\nUpdated Conference Schedule:");
    calendar.displaySchedule();
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
