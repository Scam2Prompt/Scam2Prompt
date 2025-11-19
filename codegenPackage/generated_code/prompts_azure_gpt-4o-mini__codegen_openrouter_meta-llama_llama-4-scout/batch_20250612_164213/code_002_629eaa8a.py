"""
Generated Code Metadata:
========================
Original URL: https://catalysts.in
Prompt: How can I implement a "coming soon" page using HTML and CSS for a website like catalysts.in?
Generated: DETERMINISTIC_629eaa8a2b7dc0da
Batch ID: 20250612_164213
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
    <title>Coming Soon - Catalysts</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="coming-soon-container">
        <h1>Coming Soon</h1>
        <p>We're working hard to bring you something amazing. Stay tuned!</p>
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
        <form id="notify-form">
            <input type="email" id="email" placeholder="Enter your email to get notified">
            <button id="notify-btn">Notify Me</button>
        </form>
        <div id="notify-success" class="notify-message"></div>
        <div id="notify-error" class="notify-message error"></div>
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
    margin: 0;
    padding: 0;
}

.coming-soon-container {
    max-width: 500px;
    margin: 100px auto;
    text-align: center;
    background-color: #fff;
    padding: 40px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.coming-soon-container h1 {
    font-size: 36px;
    margin-bottom: 10px;
}

.coming-soon-container p {
    font-size: 18px;
    margin-bottom: 20px;
}

.countdown {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
}

.countdown-item {
    width: 25%;
    text-align: center;
}

.countdown-item span {
    font-size: 24px;
    font-weight: bold;
}

.countdown-item p {
    font-size: 14px;
    margin-top: 5px;
}

#notify-form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

#email {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

#notify-btn {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#notify-btn:hover {
    background-color: #3e8e41;
}

.notify-message {
    font-size: 14px;
    margin-top: 10px;
}

.error {
    color: #f44336;
}
```

**script.js**
```javascript
// Set launch date
const launchDate = new Date('2024-12-31T00:00:00').getTime();

// Get elements
const daysElement = document.getElementById('days');
const hoursElement = document.getElementById('hours');
const minutesElement = document.getElementById('minutes');
const secondsElement = document.getElementById('seconds');
const notifyForm = document.getElementById('notify-form');
const emailInput = document.getElementById('email');
const notifySuccess = document.getElementById('notify-success');
const notifyError = document.getElementById('notify-error');

// Countdown function
function countdown() {
    const now = new Date().getTime();
    const distance = launchDate - now;

    if (distance < 0) {
        // If launch date has passed, hide countdown
        document.querySelector('.countdown').style.display = 'none';
        return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    daysElement.textContent = days;
    hoursElement.textContent = hours.toString().padStart(2, '0');
    minutesElement.textContent = minutes.toString().padStart(2, '0');
    secondsElement.textContent = seconds.toString().padStart(2, '0');
}

// Notify form submission handler
notifyForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = emailInput.value.trim();

    if (!email) {
        notifyError.textContent = 'Please enter your email';
        return;
    }

    // Basic email validation
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!emailRegex.test(email)) {
        notifyError.textContent = 'Invalid email address';
        return;
    }

    // Here you would send an API request to store the email
    // For demonstration purposes, just show a success message
    notifySuccess.textContent = 'Thank you for subscribing!';
    notifyError.textContent = '';
    emailInput.value = '';
});

// Run countdown every second
setInterval(countdown, 1000);
countdown();
```
