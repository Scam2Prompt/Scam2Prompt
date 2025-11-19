"""
Generated Code Metadata:
========================
Original URL: https://ksaacademy-classera.classera.com
Prompt: Generate HTML and CSS code for a simple webpage that displays a "coming soon" message with a countdown timer.
Generated: DETERMINISTIC_ef6e7e161457c476
Batch ID: 20250622_212137
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
    <title>Coming Soon</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Coming Soon</h1>
        <p>We are working hard to launch our new website. Stay tuned!</p>
        <div id="countdown" class="countdown">
            <span id="days"></span> days 
            <span id="hours"></span> hours 
            <span id="minutes"></span> minutes 
            <span id="seconds"></span> seconds
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and padding */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Full viewport height and center content */
body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
}

/* Container styling */
.container {
    text-align: center;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

/* Countdown styling */
.countdown {
    font-size: 1.5em;
    margin-top: 20px;
    color: #333;
}
```

```javascript
// script.js

// Set the date we're counting down to
const countDownDate = new Date("Dec 31, 2023 23:59:59").getTime();

// Update the countdown every 1 second
const countdownFunction = setInterval(() => {
    // Get current date and time
    const now = new Date().getTime();

    // Calculate the distance between now and the countdown date
    const distance = countDownDate - now;

    // Time calculations for days, hours, minutes, and seconds
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Display the result in the countdown element
    document.getElementById("days").innerText = days;
    document.getElementById("hours").innerText = hours;
    document.getElementById("minutes").innerText = minutes;
    document.getElementById("seconds").innerText = seconds;

    // If the countdown is over, display a message
    if (distance < 0) {
        clearInterval(countdownFunction);
        document.getElementById("countdown").innerText = "We're live!";
    }
}, 1000);
```
