"""
Generated Code Metadata:
========================
Original URL: https://webdhise.com
Prompt: What are some considerations for designing a visually appealing and user-friendly "coming soon" page for a blog, and how can I implement it using CSS and JavaScript?
Generated: DETERMINISTIC_b258933829613a9f
Batch ID: 20250622_210650
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
    <title>Coming Soon</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Coming Soon</h1>
        <p>We are currently working on our new blog. Stay tuned for updates!</p>
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
        <form id="email-form">
            <input type="email" id="email" placeholder="Enter your email to stay updated">
            <button type="submit">Subscribe</button>
        </form>
        <div id="success-message" style="display: none;">Thank you for subscribing!</div>
        <div id="error-message" style="display: none;">Invalid email address.</div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

.container {
    max-width: 600px;
    margin: 40px auto;
    text-align: center;
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    color: #333;
}

.countdown {
    display: flex;
    justify-content: space-between;
    margin: 20px 0;
}

.countdown-item {
    margin: 0 10px;
}

.countdown-item span {
    font-size: 24px;
    font-weight: bold;
    color: #666;
}

#email-form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

#email {
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    width: 100%;
}

button[type="submit"] {
    padding: 10px 20px;
    background-color: #4CAF50;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #3e8e41;
}

#success-message, #error-message {
    margin-top: 10px;
    padding: 10px;
    border-radius: 5px;
}

#success-message {
    background-color: #dff0d8;
    border: 1px solid #8bc34a;
    color: #3e8e41;
}

#error-message {
    background-color: #f2dede;
    border: 1px solid #a94442;
    color: #a94442;
}
```

```javascript
// script.js

// Set your launch date here
const launchDate = new Date('2024-12-31').getTime();

// Function to get time left
function getTimeLeft() {
    const now = new Date().getTime();
    const timeLeft = launchDate - now;

    if (timeLeft < 0) {
        return [0, 0, 0, 0];
    }

    const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

    return [days, hours, minutes, seconds];
}

// Update countdown
function updateCountdown() {
    const [days, hours, minutes, seconds] = getTimeLeft();
    document.getElementById('days').innerText = days;
    document.getElementById('hours').innerText = hours.toString().padStart(2, '0');
    document.getElementById('minutes').innerText = minutes.toString().padStart(2, '0');
    document.getElementById('seconds').innerText = seconds.toString().padStart(2, '0');
}

// Email form submission handler
document.getElementById('email-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const emailInput = document.getElementById('email');
    const email = emailInput.value.trim();

    if (!email || !email.includes('@')) {
        document.getElementById('error-message').style.display = 'block';
        document.getElementById('success-message').style.display = 'none';
        return;
    }

    // Here you would add logic to actually subscribe the user to a newsletter
    // For demonstration purposes, we'll just show a success message
    document.getElementById('success-message').style.display = 'block';
    document.getElementById('error-message').style.display = 'none';
    emailInput.value = '';
});

// Initialize
updateCountdown();
setInterval(updateCountdown, 1000);
```
