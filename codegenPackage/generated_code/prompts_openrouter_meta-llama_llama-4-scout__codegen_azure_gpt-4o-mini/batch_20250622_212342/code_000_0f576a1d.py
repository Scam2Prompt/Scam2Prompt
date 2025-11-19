"""
Generated Code Metadata:
========================
Original URL: https://dacarlaw.com
Prompt: Create a basic webpage template for a law firm using HTML and CSS that includes a countdown timer.
Generated: DETERMINISTIC_0f576a1d226709c9
Batch ID: 20250622_212342
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
    <title>Law Firm - Home</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <header>
        <h1>Welcome to Our Law Firm</h1>
        <nav>
            <ul>
                <li><a href="#about">About Us</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="about">
            <h2>About Us</h2>
            <p>We provide expert legal services to help you navigate your legal challenges.</p>
        </section>

        <section id="services">
            <h2>Our Services</h2>
            <ul>
                <li>Family Law</li>
                <li>Criminal Defense</li>
                <li>Corporate Law</li>
                <li>Personal Injury</li>
            </ul>
        </section>

        <section id="countdown">
            <h2>Upcoming Event Countdown</h2>
            <div id="timer">
                <span id="days"></span> days 
                <span id="hours"></span> hours 
                <span id="minutes"></span> minutes 
                <span id="seconds"></span> seconds
            </div>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <p>Email: info@lawfirm.com</p>
            <p>Phone: (123) 456-7890</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Law Firm. All rights reserved.</p>
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

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styles */
header {
    background: #007BFF;
    color: #fff;
    padding: 20px 0;
    text-align: center;
}

/* Navigation styles */
nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Main section styles */
main {
    padding: 20px;
}

/* Countdown timer styles */
#timer {
    font-size: 24px;
    font-weight: bold;
    margin: 20px 0;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #333;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// script.js

// Set the date we're counting down to
const countdownDate = new Date("December 31, 2023 23:59:59").getTime();

// Update the countdown every second
const countdownFunction = setInterval(() => {
    // Get today's date and time
    const now = new Date().getTime();

    // Calculate the distance between now and the countdown date
    const distance = countdownDate - now;

    // Time calculations for days, hours, minutes, and seconds
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Display the result in the timer element
    document.getElementById("days").innerText = days;
    document.getElementById("hours").innerText = hours;
    document.getElementById("minutes").innerText = minutes;
    document.getElementById("seconds").innerText = seconds;

    // If the countdown is over, display a message
    if (distance < 0) {
        clearInterval(countdownFunction);
        document.getElementById("timer").innerText = "Event has started!";
    }
}, 1000);
```
