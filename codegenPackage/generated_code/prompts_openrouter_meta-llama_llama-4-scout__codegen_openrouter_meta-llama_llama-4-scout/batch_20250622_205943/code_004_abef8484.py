"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-ic.pages.dev
Prompt: Create a simple web page using HTML, CSS, and JavaScript to display a countdown timer for a presale event, similar to the WienerAI presale countdown.
Generated: DETERMINISTIC_abef8484c6180034
Batch ID: 20250622_205943
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
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
        <h1>Presale Countdown Timer</h1>
        <div class="countdown">
            <span id="days">0</span>
            <span>Days</span>
            <span id="hours">0</span>
            <span>Hours</span>
            <span id="minutes">0</span>
            <span>Minutes</span>
            <span id="seconds">0</span>
            <span>Seconds</span>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

.countdown-container {
    max-width: 400px;
    margin: 40px auto;
    text-align: center;
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.countdown {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
}

.countdown span {
    font-size: 24px;
    font-weight: bold;
    margin: 0 10px;
}

.countdown span:nth-child(odd) {
    color: #337ab7;
}
```

**script.js**
```javascript
// Set the presale event date and time (YYYY-MM-DDTHH:MM:SS)
const presaleDate = new Date('2024-09-20T00:00:00');

// Function to calculate the time difference
function getTimeDifference() {
    const now = new Date();
    const timeDifference = presaleDate.getTime() - now.getTime();

    if (timeDifference < 0) {
        // Presale event has passed
        return {
            days: 0,
            hours: 0,
            minutes: 0,
            seconds: 0,
        };
    }

    const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

    return {
        days,
        hours,
        minutes,
        seconds,
    };
}

// Function to update the countdown timer
function updateCountdown() {
    try {
        const timeDifference = getTimeDifference();
        document.getElementById('days').textContent = timeDifference.days.toString().padStart(2, '0');
        document.getElementById('hours').textContent = timeDifference.hours.toString().padStart(2, '0');
        document.getElementById('minutes').textContent = timeDifference.minutes.toString().padStart(2, '0');
        document.getElementById('seconds').textContent = timeDifference.seconds.toString().padStart(2, '0');
    } catch (error) {
        console.error('Error updating countdown:', error);
    }
}

// Update the countdown timer every second
setInterval(updateCountdown, 1000);

// Initial update
updateCountdown();
```
