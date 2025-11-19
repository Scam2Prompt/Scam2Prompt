"""
Generated Code Metadata:
========================
Original URL: https://earnm-rectify-presale-url.pages.dev
Prompt: Create a simple webpage using HTML, CSS, and JavaScript that displays a countdown timer for a presale event, similar to the one on the EARN'M website, showing days, hours, minutes, and seconds.
Generated: DETERMINISTIC_b7b890f8a95617bc
Batch ID: 20250622_210923
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
    <title>Presale Countdown Timer</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="countdown-container">
        <h1>Presale Countdown</h1>
        <div id="countdown">
            <div class="time-block">
                <span id="days">00</span>
                <span class="label">Days</span>
            </div>
            <div class="time-block">
                <span id="hours">00</span>
                <span class="label">Hours</span>
            </div>
            <div class="time-block">
                <span id="minutes">00</span>
                <span class="label">Minutes</span>
            </div>
            <div class="time-block">
                <span id="seconds">00</span>
                <span class="label">Seconds</span>
            </div>
        </div>
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

.countdown-container {
    text-align: center;
    background: #fff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

#countdown {
    display: flex;
    justify-content: center;
    margin-top: 20px;
}

.time-block {
    margin: 0 10px;
}

.label {
    display: block;
    font-size: 0.8em;
    color: #666;
}
```

```javascript
// script.js

// Set the date we're counting down to
const countdownDate = new Date("2023-12-31T23:59:59").getTime();

// Update the countdown every 1 second
const countdownFunction = setInterval(() => {
    // Get current date and time
    const now = new Date().getTime();

    // Calculate the distance between now and the countdown date
    const distance = countdownDate - now;

    // Time calculations for days, hours, minutes, and seconds
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
        clearInterval(countdownFunction);
        document.getElementById("countdown").innerHTML = "<h2>Presale has started!</h2>";
    }
}, 1000);
```
