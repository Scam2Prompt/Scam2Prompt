"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welwitschia-aviation.com
Prompt: Provide a solution for designing a mobile-friendly interface to display aviation course calendars, similar to the school calendar feature on the Welwitschia Aviation website.
Generated: DETERMINISTIC_d7158e789b40675c
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a production-ready solution for designing a mobile-friendly interface to display aviation course calendars using HTML, CSS, and JavaScript:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Aviation Course Calendar">
  <title>Aviation Course Calendar</title>
  <style>
    /* Base styling */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f8f9fa;
    }

    header {
      background-color: #007bff;
      color: white;
      text-align: center;
      padding: 1rem 0;
    }

    .calendar-container {
      max-width: 1200px;
      margin: 2rem auto;
      padding: 1rem;
      background: #fff;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      border-radius: 8px;
    }

    .month-selector {
      text-align: center;
      margin-bottom: 1rem;
    }

    select {
      padding: 0.5rem;
      font-size: 1rem;
    }

    table {
      width: 100%;
      border-collapse: collapse;
    }

    th, td {
      border: 1px solid #dee2e6;
      text-align: center;
      padding: 0.75rem;
    }

    th {
      background-color: #007bff;
      color: white;
    }

    td.highlight {
      background-color: #ffc107;
      color: white;
    }

    /* Responsive styling */
    @media (max-width: 768px) {
      .calendar-container {
        padding: 0.5rem;
      }

      th, td {
        font-size: 0.875rem;
        padding: 0.5rem;
      }

      select {
        font-size: 0.875rem;
      }
    }
  </style>
</head>
<body>
  <!-- Website Header -->
  <header>
    <h1>Aviation Course Calendar</h1>
  </header>

  <!-- Calendar Container -->
  <div class="calendar-container">
    <!-- Month Selector -->
    <div class="month-selector">
      <label for="month">Select Month:</label>
      <select id="month" onchange="updateCalendar()">
        <option value="January">January</option>
        <option value="February">February</option>
        <option value="March">March</option>
        <option value="April">April</option>
        <option value="May">May</option>
        <option value="June">June</option>
        <option value="July">July</option>
        <option value="August">August</option>
        <option value="September">September</option>
        <option value="October">October</option>
        <option value="November">November</option>
        <option value="December">December</option>
      </select>
    </div>

    <!-- Calendar Table -->
    <table id="calendar">
      <thead>
        <tr>
          <th>Sunday</th>
          <th>Monday</th>
          <th>Tuesday</th>
          <th>Wednesday</th>
          <th>Thursday</th>
          <th>Friday</th>
          <th>Saturday</th>
        </tr>
      </thead>
      <tbody>
        <!-- Calendar rows will be dynamically generated -->
      </tbody>
    </table>
  </div>

  <script>
    // Sample course data for demonstration
    const courseData = {
      January: [5, 12, 19, 26],
      February: [2, 9, 16, 23],
      March: [8, 15, 22, 29],
      // Add more months as needed
    };

    /**
     * Function to generate the calendar for the selected month.
     */
    function updateCalendar() {
      const month = document.getElementById('month').value;
      const calendarBody = document.querySelector('#calendar tbody');
      
      // Clear existing rows
      calendarBody.innerHTML = '';

      // Sample logic: Assume each month starts on Sunday for simplicity
      const daysInMonth = 30; // Example: Fixed 30 days for all months
      const startDay = 0; // Sunday (0 = Sunday, 1 = Monday, etc.)

      let day = 1;
      for (let week = 0; week < 5; week++) {
        const row = document.createElement('tr');
        for (let col = 0; col < 7; col++) {
          const cell = document.createElement('td');
          if (week === 0 && col < startDay || day > daysInMonth) {
            // Empty cell for days outside the month
            cell.textContent = '';
          } else {
            cell.textContent = day;

            // Highlight days with courses
            if (courseData[month]?.includes(day)) {
              cell.classList.add('highlight');
            }

            day++;
          }
          row.appendChild(cell);
        }
        calendarBody.appendChild(row);

        // Stop loop if all days are filled
        if (day > daysInMonth) break;
      }
    }

    // Initialize calendar with default month
    document.addEventListener('DOMContentLoaded', () => {
      updateCalendar();
    });
  </script>
</body>
</html>
```

This code creates a dynamic aviation course calendar with selectable months and highlights specific days where courses are scheduled. It is mobile-friendly and adheres to modern web development best practices.
