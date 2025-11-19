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
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Event Countdown - Gabe and Adnan's Prom</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <header>
        <h1>Gabe and Adnan's Prom</h1>
        <p>Join us for a night to remember!</p>
    </header>

    <main>
        <section id="countdown">
            <h2>Countdown to the Event</h2>
            <div id="timer">
                <span id="days">00</span> days 
                <span id="hours">00</span> hours 
                <span id="minutes">00</span> minutes 
                <span id="seconds">00</span> seconds
            </div>
        </section>

        <section id="schedule">
            <h2>Event Schedule</h2>
            <ul>
                <li><strong>6:00 PM:</strong> Arrival and Check-in</li>
                <li><strong>7:00 PM:</strong> Dinner Served</li>
                <li><strong>8:00 PM:</strong> Dance Begins</li>
                <li><strong>10:00 PM:</strong> Special Performance</li>
                <li><strong>11:30 PM:</strong> Event Ends</li>
            </ul>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Gabe and Adnan's Prom. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styling */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styling */
header {
    background-color: #4CAF50;
    color: white;
    text-align: center;
    padding: 20px 0;
}

/* Main content styling */
main {
    padding: 20px;
}

/* Countdown section styling */
#countdown {
    background-color: #fff;
    border: 1px solid #ddd;
    padding: 20px;
    margin-bottom: 20px;
    text-align: center;
}

/* Timer styling */
#timer {
    font-size: 2em;
    font-weight: bold;
}

/* Schedule section styling */
#schedule {
    background-color: #fff;
    border: 1px solid #ddd;
    padding: 20px;
}

/* Footer styling */
footer {
    text-align: center;
    padding: 10px 0;
    background-color: #4CAF50;
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// script.js

// Set the date of the event
const eventDate = new Date("2023-12-31T18:00:00").getTime();

// Update the countdown every second
const countdownInterval = setInterval(() => {
    const now = new Date().getTime();
    const distance = eventDate - now;

    // Calculate time components
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Display the result in the timer element
    document.getElementById("days").innerText = String(days).padStart(2, '0');
    document.getElementById("hours").innerText = String(hours).padStart(2, '0');
    document.getElementById("minutes").innerText = String(minutes).padStart(2, '0');
    document.getElementById("seconds").innerText = String(seconds).padStart(2, '0');

    // If the countdown is over, display a message
    if (distance < 0) {
        clearInterval(countdownInterval);
        document.getElementById("timer").innerText = "Event has started!";
    }
}, 1000);
```
