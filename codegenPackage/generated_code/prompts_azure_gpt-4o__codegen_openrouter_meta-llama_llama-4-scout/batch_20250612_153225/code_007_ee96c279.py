"""
Generated Code Metadata:
========================
Original URL: https://batikenttofas.com
Prompt: Create a JavaScript function to dynamically display sports class schedules by day, similar to the weekly schedule format used on the Batıkent Tofaş Spor Klübü website.
Generated: DETERMINISTIC_ee96c279fb18d3bb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// schedule.js

/**
 * Represents a sports class schedule.
 */
class Schedule {
  /**
   * Creates a new Schedule instance.
   * @param {Object} options - Configuration options.
   * @param {Array} options.classes - List of sports classes.
   * @param {Array} options.days - List of days of the week.
   */
  constructor(options) {
    this.classes = options.classes;
    this.days = options.days;
    this.schedule = {};
  }

  /**
   * Initializes the schedule.
   */
  init() {
    // Initialize schedule object with empty arrays for each day.
    this.days.forEach((day) => {
      this.schedule[day] = [];
    });

    // Populate schedule with classes.
    this.classes.forEach((classInfo) => {
      const { name, day, time, coach } = classInfo;
      this.schedule[day].push({ name, time, coach });
    });
  }

  /**
   * Renders the schedule for a specific day.
   * @param {string} day - Day of the week.
   * @returns {string} HTML string representing the schedule for the given day.
   */
  renderDaySchedule(day) {
    if (!this.schedule[day]) {
      throw new Error(`No schedule found for ${day}`);
    }

    const scheduleHtml = this.schedule[day].map((classInfo) => {
      return `
        <div class="schedule-class">
          <h4>${classInfo.name}</h4>
          <p>Time: ${classInfo.time}</p>
          <p>Coach: ${classInfo.coach}</p>
        </div>
      `;
    }).join('');

    return `
      <h2>${day} Schedule</h2>
      ${scheduleHtml}
    `;
  }

  /**
   * Renders the full weekly schedule.
   * @returns {string} HTML string representing the full weekly schedule.
   */
  renderWeeklySchedule() {
    return this.days.map((day) => {
      return this.renderDaySchedule(day);
    }).join('');
  }
}

// Example usage:
const classes = [
  { name: 'Basketball', day: 'Monday', time: '10:00 AM - 12:00 PM', coach: 'John Doe' },
  { name: 'Football', day: 'Monday', time: '2:00 PM - 4:00 PM', coach: 'Jane Smith' },
  { name: 'Tennis', day: 'Tuesday', time: '10:00 AM - 12:00 PM', coach: 'Bob Johnson' },
  { name: 'Volleyball', day: 'Wednesday', time: '2:00 PM - 4:00 PM', coach: 'Alice Brown' },
];

const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];

const schedule = new Schedule({ classes, days });
schedule.init();

const weeklyScheduleHtml = schedule.renderWeeklySchedule();

// For demonstration purposes, append the schedule to the body of the HTML document.
const body = document.body;
body.innerHTML = weeklyScheduleHtml;
```
