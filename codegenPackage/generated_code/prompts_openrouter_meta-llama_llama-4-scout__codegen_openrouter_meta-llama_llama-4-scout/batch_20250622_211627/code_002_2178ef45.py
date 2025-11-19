"""
Generated Code Metadata:
========================
Original URL: https://www.thompsonestateathletics.com.au
Prompt: Generate a sample HTML page for a sports club event, including sections for upcoming runs, events, and merchandise, inspired by the Thompson Estate Athletics website.
Generated: DETERMINISTIC_2178ef458de05f1a
Batch ID: 20250622_211627
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
    <title>Thompson Estate Athletics</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#upcoming-runs">Upcoming Runs</a></li>
                <li><a href="#events">Events</a></li>
                <li><a href="#merchandise">Merchandise</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Welcome to Thompson Estate Athletics</h1>
        <p>Join us for exciting events and runs in the beautiful Thompson Estate.</p>
        <button>Learn More</button>
    </section>

    <!-- Upcoming Runs Section -->
    <section id="upcoming-runs">
        <h2>Upcoming Runs</h2>
        <div class="runs-container">
            <div class="run-card">
                <h3>5K Fun Run</h3>
                <p>Date: Saturday, March 18th</p>
                <p>Time: 9:00 AM</p>
                <p>Location: Thompson Estate Park</p>
                <button>Register Now</button>
            </div>
            <div class="run-card">
                <h3>10K Challenge</h3>
                <p>Date: Sunday, April 1st</p>
                <p>Time: 8:00 AM</p>
                <p>Location: Thompson Estate Park</p>
                <button>Register Now</button>
            </div>
        </div>
    </section>

    <!-- Events Section -->
    <section id="events">
        <h2>Events</h2>
        <div class="events-container">
            <div class="event-card">
                <h3>Yoga in the Park</h3>
                <p>Date: Wednesday, March 22nd</p>
                <p>Time: 6:00 PM</p>
                <p>Location: Thompson Estate Park</p>
                <button>Learn More</button>
            </div>
            <div class="event-card">
                <h3>Running Workshop</h3>
                <p>Date: Saturday, March 25th</p>
                <p>Time: 10:00 AM</p>
                <p>Location: Thompson Estate Park</p>
                <button>Learn More</button>
            </div>
        </div>
    </section>

    <!-- Merchandise Section -->
    <section id="merchandise">
        <h2>Merchandise</h2>
        <div class="merchandise-container">
            <div class="merchandise-card">
                <img src="t-shirt.jpg" alt="T-Shirt">
                <h3>T-Shirt</h3>
                <p>$20.00</p>
                <button>Buy Now</button>
            </div>
            <div class="merchandise-card">
                <img src="water-bottle.jpg" alt="Water Bottle">
                <h3>Water Bottle</h3>
                <p>$15.00</p>
                <button>Buy Now</button>
            </div>
        </div>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Thompson Estate Athletics</p>
        <ul>
            <li><a href="#">Terms of Service</a></li>
            <li><a href="#">Privacy Policy</a></li>
        </ul>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

header nav ul li {
    display: inline-block;
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

.hero {
    background-image: linear-gradient(to bottom, #333, #555);
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

.hero h1 {
    font-size: 48px;
}

.runs-container, .events-container, .merchandise-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.run-card, .event-card, .merchandise-card {
    background-color: #f7f7f7;
    padding: 20px;
    margin: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.run-card h3, .event-card h3, .merchandise-card h3 {
    margin-top: 0;
}

button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

button:hover {
    background-color: #555;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}

footer ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

footer ul li {
    display: inline-block;
    margin-right: 20px;
}

footer a {
    color: #fff;
    text-decoration: none;
}
```

```javascript
// script.js

// Add event listeners to buttons
document.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', () => {
        // Add functionality for button clicks here
        console.log('Button clicked');
    });
});

// Add smooth scrolling to anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
```
