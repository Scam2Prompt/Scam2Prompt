"""
Generated Code Metadata:
========================
Original URL: https://beta.metis-lab.com
Prompt: Generate a code snippet to create a simple event calendar using JavaScript, inspired by the "Événements" section on the Mêtis website.
Generated: DETERMINISTIC_99b2264b121c57f2
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// EventCalendar.js

/**
 * A simple event calendar class.
 */
class EventCalendar {
  /**
   * Constructor for EventCalendar.
   * @param {HTMLElement} container - The container element for the calendar.
   */
  constructor(container) {
    this.container = container;
    this.events = [];
  }

  /**
   * Adds an event to the calendar.
   * @param {string} title - The title of the event.
   * @param {Date} startDate - The start date of the event.
   * @param {Date} endDate - The end date of the event.
   */
  addEvent(title, startDate, endDate) {
    this.events.push({ title, startDate, endDate });
    this.renderCalendar();
  }

  /**
   * Removes an event from the calendar.
   * @param {string} title - The title of the event to remove.
   */
  removeEvent(title) {
    this.events = this.events.filter(event => event.title !== title);
    this.renderCalendar();
  }

  /**
   * Renders the event calendar.
   */
  renderCalendar() {
    // Clear the container
    this.container.innerHTML = '';

    // Create a header for the calendar
    const header = document.createElement('h2');
    header.textContent = 'Event Calendar';
    this.container.appendChild(header);

    // Create a table for the events
    const table = document.createElement('table');
    table.innerHTML = `
      <thead>
        <tr>
          <th>Title</th>
          <th>Start Date</th>
          <th>End Date</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody id="events-table-body">
      </tbody>
    `;
    this.container.appendChild(table);

    // Populate the table body with events
    const tableBody = table.querySelector('#events-table-body');
    this.events.forEach(event => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${event.title}</td>
        <td>${event.startDate.toLocaleString()}</td>
        <td>${event.endDate.toLocaleString()}</td>
        <td><button class="remove-event-btn">Remove</button></td>
      `;
      tableBody.appendChild(row);

      // Add event listener to the remove button
      row.querySelector('.remove-event-btn').addEventListener('click', () => {
        this.removeEvent(event.title);
      });
    });
  }
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
  const calendarContainer = document.getElementById('event-calendar');
  if (!calendarContainer) {
    throw new Error('No element with id "event-calendar" found');
  }

  const calendar = new EventCalendar(calendarContainer);

  // Add some events
  calendar.addEvent('Event 1', new Date('2024-09-20T10:00:00'), new Date('2024-09-20T12:00:00'));
  calendar.addEvent('Event 2', new Date('2024-09-21T14:00:00'), new Date('2024-09-21T16:00:00'));

  // Error handling example
  try {
    calendar.addEvent('', new Date(), new Date());
  } catch (error) {
    console.error('Error adding event:', error);
  }
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Event Calendar</title>
  <style>
    table {
      border-collapse: collapse;
    }
    th, td {
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
    }
  </style>
</head>
<body>
  <div id="event-calendar"></div>
  <script src="EventCalendar.js"></script>
</body>
</html>
```
