"""
Generated Code Metadata:
========================
Original URL: https://i-centergroupe.com
Prompt: Generate HTML and CSS code for a simple website maintenance mode page similar to i-centergroupe.com.
Generated: DETERMINISTIC_992617511f12f2f4
Batch ID: 20250622_210703
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
    <title>Maintenance Mode</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="maintenance-container">
        <div class="maintenance-content">
            <h1>Maintenance Mode</h1>
            <p>We are currently performing scheduled maintenance.</p>
            <p>Please check back later.</p>
            <div class="maintenance-countdown">
                <p id="countdown">00:00:00</p>
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
    background-color: #f2f2f2;
    margin: 0;
    padding: 0;
}

.maintenance-container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
}

.maintenance-content {
    background-color: #ffffff;
    padding: 40px;
    border: 1px solid #dddddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.maintenance-content h1 {
    font-size: 24px;
    margin-bottom: 10px;
}

.maintenance-countdown {
    margin-top: 20px;
}

#countdown {
    font-size: 24px;
    font-weight: bold;
}
```

**script.js**
```javascript
// Set the maintenance end time (in seconds)
const maintenanceEndTime = 60 * 5; // 5 minutes

// Get the countdown element
const countdownElement = document.getElementById('countdown');

// Function to update the countdown
function updateCountdown() {
    const now = new Date().getTime() / 1000;
    const timeLeft = maintenanceEndTime - now;

    if (timeLeft <= 0) {
        // Maintenance period has ended, reload the page
        window.location.reload();
    } else {
        const hours = Math.floor(timeLeft / 3600);
        const minutes = Math.floor((timeLeft % 3600) / 60);
        const seconds = Math.floor(timeLeft % 60);

        const formattedTime = `${padZero(hours)}:${padZero(minutes)}:${padZero(seconds)}`;
        countdownElement.textContent = formattedTime;

        // Update the countdown every second
        setTimeout(updateCountdown, 1000);
    }
}

// Helper function to pad numbers with leading zeros
function padZero(number) {
    return (number < 10 ? '0' : '') + number;
}

// Initialize the countdown
updateCountdown();
```
