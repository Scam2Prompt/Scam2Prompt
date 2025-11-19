"""
Generated Code Metadata:
========================
Original URL: https://prom-app.vercel.app
Prompt: Create a simple HTML layout for an event page that includes a countdown timer and a schedule, inspired by the design of Gabe and Adnan's Prom.
Generated: DETERMINISTIC_7a9e2fe891c50ed3
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Event Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Event Countdown</h1>
    </header>
    <main>
        <section class="countdown">
            <h2>Countdown to Event</h2>
            <div class="countdown-timer">
                <span id="days">0</span> days, 
                <span id="hours">0</span> hours, 
                <span id="minutes">0</span> minutes, 
                <span id="seconds">0</span> seconds
            </div>
        </section>
        <section class="schedule">
            <h2>Event Schedule</h2>
            <table>
                <thead>
                    <tr>
                        <th>Time</th>
                        <th>Event</th>
                    </tr>
                </thead>
                <tbody id="schedule-body">
                    <!-- Schedule items will be generated here -->
                </tbody>
            </table>
        </section>
    </main>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

.countdown {
    background-color: #f0f0f0;
    padding: 1em;
    margin-bottom: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.countdown-timer {
    font-size: 24px;
    font-weight: bold;
}

.schedule {
    background-color: #f0f0f0;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

table {
    width: 100%;
    border-collapse: collapse;
}

th, td {
    border: 1px solid #ddd;
    padding: 0.5em;
    text-align: left;
}

th {
    background-color: #f0f0f0;
}
```

```javascript
// script.js

// Set event date
const eventDate = new Date('2024-09-17T00:00:00.000Z');

// Get countdown elements
const daysElement = document.getElementById('days');
const hoursElement = document.getElementById('hours');
const minutesElement = document.getElementById('minutes');
const secondsElement = document.getElementById('seconds');

// Get schedule body
const scheduleBody = document.getElementById('schedule-body');

// Function to update countdown
function updateCountdown() {
    const now = new Date();
    const timeLeft = eventDate.getTime() - now.getTime();

    if (timeLeft < 0) {
        // Event has passed
        daysElement.textContent = '0';
        hoursElement.textContent = '0';
        minutesElement.textContent = '0';
        secondsElement.textContent = '0';
        return;
    }

    const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

    daysElement.textContent = days;
    hoursElement.textContent = hours.toString().padStart(2, '0');
    minutesElement.textContent = minutes.toString().padStart(2, '0');
    secondsElement.textContent = seconds.toString().padStart(2, '0');
}

// Function to generate schedule
function generateSchedule() {
    // Example schedule data
    const scheduleData = [
        { time: '09:00 AM', event: 'Registration' },
        { time: '10:00 AM', event: 'Keynote Speech' },
        { time: '11:30 AM', event: 'Break' },
        { time: '12:00 PM', event: 'Panel Discussion' },
    ];

    scheduleData.forEach((item) => {
        const row = document.createElement('tr');
        const timeCell = document.createElement('td');
        const eventCell = document.createElement('td');

        timeCell.textContent = item.time;
        eventCell.textContent = item.event;

        row.appendChild(timeCell);
        row.appendChild(eventCell);

        scheduleBody.appendChild(row);
    });
}

// Initialize countdown and schedule
updateCountdown();
generateSchedule();

// Update countdown every second
setInterval(updateCountdown, 1000);
```
