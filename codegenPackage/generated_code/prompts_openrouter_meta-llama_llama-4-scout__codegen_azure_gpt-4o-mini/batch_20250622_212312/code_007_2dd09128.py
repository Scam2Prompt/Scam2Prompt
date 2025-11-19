"""
Generated Code Metadata:
========================
Original URL: https://tether.cfd
Prompt: Create a basic webpage using HTML, CSS, and JavaScript to display a countdown timer for a limited-time reward program like Tether's USDT Reward Program.
Generated: DETERMINISTIC_2dd09128878a1ee2
Batch ID: 20250622_212312
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
    <title>Countdown Timer for Reward Program</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Limited-Time Reward Program</h1>
        <div id="countdown" class="countdown-timer"></div>
        <p id="message" class="message"></p>
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

/* Container styling */
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background-color: #f4f4f4;
    font-family: Arial, sans-serif;
}

/* Countdown timer styling */
.countdown-timer {
    font-size: 2rem;
    color: #333;
}

/* Message styling */
.message {
    margin-top: 20px;
    font-size: 1.2rem;
    color: #ff0000;
}
```

```javascript
// script.js

// Set the date we're counting down to (example: 1 hour from now)
const countdownDate = new Date(Date.now() + 60 * 60 * 1000).getTime();

// Update the countdown every second
const countdownFunction = setInterval(() => {
    // Get the current date and time
    const now = new Date().getTime();

    // Calculate the distance between now and the countdown date
    const distance = countdownDate - now;

    // Time calculations for days, hours, minutes, and seconds
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Display the result in the countdown element
    document.getElementById("countdown").innerHTML = `${hours}h ${minutes}m ${seconds}s`;

    // If the countdown is over, display a message
    if (distance < 0) {
        clearInterval(countdownFunction);
        document.getElementById("countdown").innerHTML = "EXPIRED";
        document.getElementById("message").innerHTML = "The reward program has ended.";
    }
}, 1000);
```
