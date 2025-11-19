"""
Generated Code Metadata:
========================
Original URL: https://ethiy.com
Prompt: How might one use HTML, CSS, and JavaScript to create a visually appealing "under construction" or "coming soon" page that also captures visitor interest?
Generated: DETERMINISTIC_94e4b184e030a111
Batch ID: 20250622_212342
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
    <title>Coming Soon</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
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
        <form id="newsletter-form">
            <input type="email" id="email" placeholder="Enter your email address">
            <button id="submit-btn">Notify Me</button>
        </form>
        <div id="success-msg"></div>
        <div id="error-msg"></div>
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

#newsletter-form {
    margin: 20px 0;
}

#email {
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 5px;
    width: 300px;
}

#submit-btn {
    padding: 10px 20px;
    font-size: 16px;
    background-color: #4CAF50;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#submit-btn:hover {
    background-color: #3e8e41;
}

#success-msg {
    color: #008000;
    font-size: 16px;
    margin: 10px 0;
}

#error-msg {
    color: #ff0000;
    font-size: 16px;
    margin: 10px 0;
}
```

**script.js**
```javascript
// Set the launch date
const launchDate = new Date('2024-12-31T00:00:00').getTime();

// Function to update the countdown
function updateCountdown() {
    const now = new Date().getTime();
    const distance = launchDate - now;

    if (distance < 0) {
        // If the launch date has passed, display 0s
        document.getElementById('days').innerText = 0;
        document.getElementById('hours').innerText = 0;
        document.getElementById('minutes').innerText = 0;
        document.getElementById('seconds').innerText = 0;
        return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById('days').innerText = days;
    document.getElementById('hours').innerText = hours;
    document.getElementById('minutes').innerText = minutes;
    document.getElementById('seconds').innerText = seconds;
}

// Update the countdown every second
setInterval(updateCountdown, 1000);

// Newsletter form submission handler
document.getElementById('newsletter-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value.trim();

    if (!email) {
        document.getElementById('error-msg').innerText = 'Please enter your email address';
        return;
    }

    // Basic email validation
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!emailRegex.test(email)) {
        document.getElementById('error-msg').innerText = 'Invalid email address';
        return;
    }

    // Simulate a successful submission (replace with actual backend logic)
    document.getElementById('success-msg').innerText = 'Thank you for subscribing!';
    document.getElementById('error-msg').innerText = '';
    document.getElementById('email').value = '';
});

// Initialize the countdown
updateCountdown();
```
