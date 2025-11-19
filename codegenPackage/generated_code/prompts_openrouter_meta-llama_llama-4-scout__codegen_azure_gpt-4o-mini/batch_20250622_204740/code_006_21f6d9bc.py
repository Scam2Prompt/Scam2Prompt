"""
Generated Code Metadata:
========================
Original URL: https://kaicat-claims.pages.dev
Prompt: Create a simple web page using HTML, CSS, and JavaScript to display a countdown timer for the KAI presale and claiming process, similar to the one on the provided webpage.
Generated: DETERMINISTIC_21f6d9bcd5a634c5
Batch ID: 20250622_204740
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
    <title>KAI Presale Countdown Timer</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>KAI Presale Countdown</h1>
        <div id="countdown" class="countdown">
            <div class="time" id="days">00</div>
            <div class="label">Days</div>
            <div class="time" id="hours">00</div>
            <div class="label">Hours</div>
            <div class="time" id="minutes">00</div>
            <div class="label">Minutes</div>
            <div class="time" id="seconds">00</div>
            <div class="label">Seconds</div>
        </div>
        <div id="message" class="message"></div>
    </div>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.container {
    text-align: center;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.countdown {
    display: flex;
    justify-content: center;
    margin: 20px 0;
}

.time {
    font-size: 2em;
    margin: 0 10px;
}

.label {
    font-size: 0.5em;
    text-transform: uppercase;
}
```

```javascript
// script.js

// Set the date for the KAI presale (YYYY, MM-1, DD, HH, MM, SS)
const presaleDate = new Date(2023, 10 - 1, 15, 12, 0, 0).getTime(); // Example: November 15, 2023, 12:00:00

// Update the countdown every second
const countdownInterval = setInterval(() => {
    const now = new Date().getTime();
    const distance = presaleDate - now;

    // Calculate time components
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Display the result in the respective elements
    document.getElementById("days").innerText = String(days).padStart(2, '0');
    document.getElementById("hours").innerText = String(hours).padStart(2, '0');
    document.getElementById("minutes").innerText = String(minutes).padStart(2, '0');
    document.getElementById("seconds").innerText = String(seconds).padStart(2, '0');

    // If the countdown is over, display a message
    if (distance < 0) {
        clearInterval(countdownInterval);
        document.getElementById("countdown").style.display = "none";
        document.getElementById("message").innerText = "The KAI presale has started!";
    }
}, 1000);
```
