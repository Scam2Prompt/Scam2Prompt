"""
Generated Code Metadata:
========================
Original URL: https://claim-blubtheblob.net
Prompt: Generate code for a simple website that announces a presale for a project named Blub The Blob, including a countdown timer.
Generated: DETERMINISTIC_81bd04c7993815fd
Batch ID: 20250622_212031
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
    <title>Blub The Blob Presale Announcement</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <header>
        <h1>Welcome to the Blub The Blob Presale!</h1>
    </header>
    <main>
        <section id="announcement">
            <h2>Get Ready for the Presale!</h2>
            <p>Join us for the exciting presale of Blub The Blob. Don't miss out!</p>
        </section>
        <section id="countdown">
            <h2>Countdown to Presale:</h2>
            <div id="timer">
                <span id="days"></span> days 
                <span id="hours"></span> hours 
                <span id="minutes"></span> minutes 
                <span id="seconds"></span> seconds
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Blub The Blob. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styling */
body {
    font-family: Arial, sans-serif;
    background-color: #f0f8ff;
    color: #333;
    text-align: center;
    padding: 20px;
}

/* Header styling */
header {
    background-color: #4a90e2;
    color: white;
    padding: 20px;
}

/* Main section styling */
main {
    margin: 20px 0;
}

/* Countdown timer styling */
#timer {
    font-size: 2em;
    font-weight: bold;
    color: #e94e77;
}

/* Footer styling */
footer {
    margin-top: 20px;
    font-size: 0.8em;
}
```

```javascript
// script.js

// Set the date for the presale
const presaleDate = new Date("2023-12-01T00:00:00").getTime();

// Update the countdown every second
const countdownInterval = setInterval(() => {
    // Get the current date and time
    const now = new Date().getTime();
    
    // Calculate the time remaining until the presale
    const timeRemaining = presaleDate - now;

    // Calculate days, hours, minutes, and seconds
    const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

    // Display the countdown timer
    document.getElementById("days").innerText = days;
    document.getElementById("hours").innerText = hours;
    document.getElementById("minutes").innerText = minutes;
    document.getElementById("seconds").innerText = seconds;

    // If the countdown is finished, display a message
    if (timeRemaining < 0) {
        clearInterval(countdownInterval);
        document.getElementById("timer").innerText = "The presale has started!";
    }
}, 1000);
```
