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

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Event Calendar</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .calendar {
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            gap: 10px;
        }
        .day {
            border: 1px solid #ccc;
            padding: 10px;
            text-align: center;
            min-height: 100px;
            position: relative;
        }
        .event {
            background-color: #007bff;
            color: white;
            padding: 5px;
            margin: 5px 0;
            border-radius: 3px;
        }
    </style>
</head>
<body>

<h1>Event Calendar</h1>
<div id="calendar" class="calendar"></div>

<script>
    // Sample events data
    const events = [
        { date: '2023-10-01', title: 'Event 1' },
        { date: '2023-10-05', title: 'Event 2' },
        { date: '2023-10-12', title: 'Event 3' },
        { date: '2023-10-15', title: 'Event 4' },
        { date: '2023-10-20', title: 'Event 5' },
    ];

    /**
     * Function to create a calendar for the current month
     * @param {number} year - The year for the calendar
     * @param {number} month - The month for the calendar (0-11)
     */
    function createCalendar(year, month) {
        const calendarElement = document.getElementById('calendar');
        calendarElement.innerHTML = ''; // Clear previous calendar

        // Get the first day of the month and the number of days in the month
        const firstDay = new Date(year, month, 1);
        const lastDay = new Date(year, month + 1, 0);
        const daysInMonth = lastDay.getDate();

        // Fill in the calendar with days
        for (let i = 1; i <= daysInMonth; i++) {
            const currentDate = new Date(year, month, i);
            const dayElement = document.createElement('div');
            dayElement.className = 'day';
            dayElement.innerText = i;

            // Check for events on the current date
            const eventList = events.filter(event => event.date === currentDate.toISOString().split('T')[0]);
            eventList.forEach(event => {
                const eventElement = document.createElement('div');
                eventElement.className = 'event';
                eventElement.innerText = event.title;
                dayElement.appendChild(eventElement);
            });

            // Append the day element to the calendar
            calendarElement.appendChild(dayElement);
        }
    }

    // Initialize the calendar for the current month
    const today = new Date();
    createCalendar(today.getFullYear(), today.getMonth());
</script>

</body>
</html>
```
