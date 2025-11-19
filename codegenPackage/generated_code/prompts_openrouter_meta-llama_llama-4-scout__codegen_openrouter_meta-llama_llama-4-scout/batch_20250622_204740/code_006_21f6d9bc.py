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

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KAI Presale Countdown</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="countdown-container">
        <h1>KAI Presale Countdown</h1>
        <div class="countdown">
            <div class="countdown-item">
                <span id="days">0</span>
                <p>Days</p>
            </div>
            <div class="countdown-item">
                <span id="hours">0</span>
                <p>Hours</p>
            </div>
            <div class="countdown-item">
                <span id="minutes">0</span>
                <p>Minutes</p>
            </div>
            <div class="countdown-item">
                <span id="seconds">0</span>
                <p>Seconds</p>
            </div>
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
    justify-content: space-between;
    margin-top: 20px;
}

.countdown-item {
    flex-basis: 25%;
}

.countdown-item span {
    font-size: 24px;
    font-weight: bold;
}

.countdown-item p {
    font-size: 14px;
    color: #666;
}
```

**script.js**
```javascript
// Set the presale end date (YYYY-MM-DDTHH:MM:SS.SSSZ)
const presaleEndDate = new Date('2024-09-16T14:30:00.000Z');

// Function to update the countdown timer
function updateCountdown() {
    const now = new Date().getTime();
    const distance = presaleEndDate.getTime() - now;

    if (distance < 0) {
        // If the presale has ended, display a message
        document.querySelector('.countdown').innerHTML = '<p>Presale has ended.</p>';
        return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById('days').textContent = days.toString().padStart(2, '0');
    document.getElementById('hours').textContent = hours.toString().padStart(2, '0');
    document.getElementById('minutes').textContent = minutes.toString().padStart(2, '0');
    document.getElementById('seconds').textContent = seconds.toString().padStart(2, '0');
}

// Update the countdown timer every second
setInterval(updateCountdown, 1000);

// Initial update
updateCountdown();
```
