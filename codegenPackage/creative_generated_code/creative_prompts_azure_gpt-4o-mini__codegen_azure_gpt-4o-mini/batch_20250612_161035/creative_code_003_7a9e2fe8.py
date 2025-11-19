"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prom-app.vercel.app
Prompt: Create a simple HTML layout for an event page that includes a countdown timer and a schedule, inspired by the design of Gabe and Adnan's Prom.
Generated: DETERMINISTIC_7a9e2fe891c50ed3
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Event Countdown - Gabe and Adnan's Prom</title>
    <link rel="stylesheet" href="styles.css">
    <script defer src="script.js"></script>
</head>
<body>
    <header>
        <h1>Welcome to Gabe and Adnan's Prom</h1>
        <p>Join us for an unforgettable night!</p>
    </header>

    <section id="countdown">
        <h2>Countdown to the Event</h2>
        <div id="timer">
            <span id="days">00</span> Days
            <span id="hours">00</span> Hours
            <span id="minutes">00</span> Minutes
            <span id="seconds">00</span> Seconds
        </div>
    </section>

    <section id="schedule">
        <h2>Event Schedule</h2>
        <ul>
            <li><strong>7:00 PM:</strong> Arrival & Check-in</li>
            <li><strong>7:30 PM:</strong> Dinner & Socializing</li>
            <li><strong>8:30 PM:</strong> Dance Begins</li>
            <li><strong>10:30 PM:</strong> Awards Ceremony</li>
            <li><strong>11:00 PM:</strong> After Party</li>
        </ul>
    </section>

    <footer>
        <p>&copy; 2023 Gabe and Adnan's Prom. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General styling for the body */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

/* Header styling */
header {
    background-color: #4CAF50;
    color: white;
    text-align: center;
    padding: 20px 0;
}

/* Countdown timer styling */
#countdown {
    text-align: center;
    margin: 20px 0;
}

/* Timer display styling */
#timer {
    font-size: 2em;
}

/* Schedule section styling */
#schedule {
    background-color: white;
    padding: 20px;
    margin: 20px auto;
    max-width: 600px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
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

// Set the date for the countdown (YYYY, MM - 1, DD, HH, MM, SS)
const eventDate = new Date(2023, 5, 15, 19, 0, 0).getTime();

// Update the countdown every second
const countdownInterval = setInterval(function() {
    const now = new Date().getTime();
    const distance = eventDate - now;

    // Time calculations for days, hours, minutes, and seconds
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Display the result in the HTML
    document.getElementById("days").innerHTML = String(days).padStart(2, '0');
    document.getElementById("hours").innerHTML = String(hours).padStart(2, '0');
    document.getElementById("minutes").innerHTML = String(minutes).padStart(2, '0');
    document.getElementById("seconds").innerHTML = String(seconds).padStart(2, '0');

    // If the countdown is over, display a message
    if (distance < 0) {
        clearInterval(countdownInterval);
        document.getElementById("timer").innerHTML = "The event has started!";
    }
}, 1000);
```
