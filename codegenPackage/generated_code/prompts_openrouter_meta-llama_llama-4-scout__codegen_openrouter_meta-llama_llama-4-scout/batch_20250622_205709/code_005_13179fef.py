"""
Generated Code Metadata:
========================
Original URL: https://papeairdropclaim.pages.dev
Prompt: Design a simple webpage using HTML, CSS, and JavaScript that displays the $PAPE token sale progress, including the countdown timer and percentage of tokens sold.
Generated: DETERMINISTIC_13179fef04bc8a16
Batch ID: 20250622_205709
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
    <title>$PAPE Token Sale</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>$PAPE Token Sale</h1>
        <div class="countdown-timer">
            <p>Countdown: <span id="countdown"></span></p>
        </div>
        <div class="token-sale-progress">
            <p>Tokens Sold: <span id="tokens-sold"></span>%</p>
            <div class="progress-bar">
                <div id="progress-bar-fill"></div>
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
    text-align: center;
}

.container {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.countdown-timer {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
}

.token-sale-progress {
    margin-bottom: 20px;
}

.progress-bar {
    width: 100%;
    height: 20px;
    background-color: #ccc;
    border-radius: 10px;
    overflow: hidden;
}

#progress-bar-fill {
    height: 20px;
    background-color: #4CAF50;
    border-radius: 10px;
    transition: width 0.5s;
}
```

**script.js**
```javascript
// Set token sale end time in Unix timestamp (seconds)
const TOKEN_SALE_END_TIME = 1735689600; // Example end time

// Set total tokens for sale
const TOTAL_TOKENS = 1000000;

// Set tokens sold so far
const TOKENS_SOLD = 250000;

function getCountdown() {
    const now = Math.floor(Date.now() / 1000);
    const timeLeft = TOKEN_SALE_END_TIME - now;

    if (timeLeft <= 0) {
        document.getElementById('countdown').innerText = 'Token sale has ended';
        return;
    }

    const days = Math.floor(timeLeft / (60 * 60 * 24));
    const hours = Math.floor((timeLeft % (60 * 60 * 24)) / (60 * 60));
    const minutes = Math.floor((timeLeft % (60 * 60)) / 60);
    const seconds = timeLeft % 60;

    document.getElementById('countdown').innerText = `${days}d ${hours}h ${minutes}m ${seconds}s`;
}

function updateTokenSaleProgress() {
    const tokensSoldPercentage = (TOKENS_SOLD / TOTAL_TOKENS) * 100;
    document.getElementById('tokens-sold').innerText = `${tokensSoldPercentage.toFixed(2)}%`;
    document.getElementById('progress-bar-fill').style.width = `${tokensSoldPercentage}%`;
}

function init() {
    try {
        // Update countdown every second
        setInterval(getCountdown, 1000);

        // Update token sale progress
        updateTokenSaleProgress();

        // Update token sale progress every 10 seconds (simulating real-time updates)
        setInterval(() => {
            // Replace with actual API call to get updated token sale data
            // TOKENS_SOLD = getTokensSoldFromAPI();
            updateTokenSaleProgress();
        }, 10000);
    } catch (error) {
        console.error('Error initializing token sale progress:', error);
    }
}

init();
```
