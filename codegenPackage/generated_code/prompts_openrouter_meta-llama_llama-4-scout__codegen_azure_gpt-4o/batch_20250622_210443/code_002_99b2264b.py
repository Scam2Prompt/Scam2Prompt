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
/**
 * Event Calendar
 * This script creates a simple event calendar using JavaScript.
 * It dynamically generates a calendar for the current month and allows adding events.
 */

// Constants for calendar generation
const DAYS_IN_WEEK = 7;
const MONTH_NAMES = [
  "January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
];
const DAY_NAMES = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

// Initialize the calendar
document.addEventListener("DOMContentLoaded", () => {
  const calendarContainer = document.getElementById("calendar");
  const events = {}; // Object to store events (key: date, value: event description)

  // Generate the calendar for the current month
  const today = new Date();
  const currentMonth = today.getMonth();
  const currentYear = today.getFullYear();
  generateCalendar(currentMonth, currentYear, calendarContainer, events);
});

/**
 * Generates the calendar for a given month and year.
 * @param {number} month - The month (0-based index).
 * @param {number} year - The year.
 * @param {HTMLElement} container - The container element for the calendar.
 * @param {Object} events - The events object.
 */
function generateCalendar(month, year, container, events) {
  container.innerHTML = ""; // Clear previous calendar

  // Create header with month and year
  const header = document.createElement("div");
  header.className = "calendar-header";
  header.innerHTML = `<h2>${MONTH_NAMES[month]} ${year}</h2>`;
  container.appendChild(header);

  // Create day names row
  const dayNamesRow = document.createElement("div");
  dayNamesRow.className = "calendar-row";
  DAY_NAMES.forEach(day => {
    const dayCell = document.createElement("div");
    dayCell.className = "calendar-cell calendar-day-name";
    dayCell.textContent = day;
    dayNamesRow.appendChild(dayCell);
  });
  container.appendChild(dayNamesRow);

  // Get the first day of the month and total days in the month
  const firstDay = new Date(year, month, 1).getDay();
  const daysInMonth = new Date(year, month + 1, 0).getDate();

  // Create rows for the days
  let day = 1;
  for (let i = 0; i < Math.ceil((firstDay + daysInMonth) / DAYS_IN_WEEK); i++) {
    const row = document.createElement("div");
    row.className = "calendar-row";

    for (let j = 0; j < DAYS_IN_WEEK; j++) {
      const cell = document.createElement("div");
      cell.className = "calendar-cell";

      if (i === 0 && j < firstDay || day > daysInMonth) {
        // Empty cell for days outside the current month
        cell.className += " calendar-empty";
      } else {
        // Cell for a valid day
        cell.textContent = day;
        cell.className += " calendar-day";
        cell.dataset.date = `${year}-${month + 1}-${day}`;

        // Add event listener for adding events
        cell.addEventListener("click", () => addEvent(cell, events));
        day++;
      }

      row.appendChild(cell);
    }

    container.appendChild(row);
  }
}

/**
 * Adds an event to a specific date.
 * @param {HTMLElement} cell - The calendar cell element.
 * @param {Object} events - The events object.
 */
function addEvent(cell, events) {
  const date = cell.dataset.date;
  const eventDescription = prompt(`Add an event for ${date}:`);

  if (eventDescription) {
    events[date] = eventDescription;
    cell.className += " calendar-event";
    cell.title = eventDescription; // Tooltip for the event
  }
}

// CSS styles for the calendar (can be moved to a separate CSS file)
const style = document.createElement("style");
style.textContent = `
  #calendar {
    display: flex;
    flex-direction: column;
    max-width: 600px;
    margin: auto;
    font-family: Arial, sans-serif;
  }
  .calendar-header {
    text-align: center;
    margin-bottom: 10px;
  }
  .calendar-row {
    display: flex;
  }
  .calendar-cell {
    flex: 1;
    padding: 10px;
    text-align: center;
    border: 1px solid #ddd;
    cursor: pointer;
  }
  .calendar-day-name {
    font-weight: bold;
    background-color: #f0f0f0;
  }
  .calendar-empty {
    background-color: #f9f9f9;
    cursor: default;
  }
  .calendar-event {
    background-color: #ffeb3b;
  }
`;
document.head.appendChild(style);

// HTML structure for the calendar (can be added to the HTML file)
const calendarHTML = document.createElement("div");
calendarHTML.id = "calendar";
document.body.appendChild(calendarHTML);
```
