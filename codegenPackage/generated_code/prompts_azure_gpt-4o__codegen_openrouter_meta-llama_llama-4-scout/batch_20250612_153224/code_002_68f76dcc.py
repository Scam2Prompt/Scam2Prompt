"""
Generated Code Metadata:
========================
Original URL: https://churchproweb.com
Prompt: Generate a responsive HTML/CSS template for a church website homepage that includes sections for prayer requests, sermon highlights, and online donations, following the layout style mentioned on ChurchProWeb.
Generated: DETERMINISTIC_68f76dcc57fab5be
Batch ID: 20250612_153224
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
    <title>Church Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Ministries</a></li>
                <li><a href="#">Events</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Welcome to Our Church</h1>
        <p>We're a community of believers seeking to serve and love our neighbors.</p>
        <button>Learn More</button>
    </section>

    <!-- Prayer Requests Section -->
    <section class="prayer-requests">
        <h2>Prayer Requests</h2>
        <p>Submit your prayer requests and we'll be praying for you.</p>
        <form id="prayer-request-form">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name"><br><br>
            <label for="request">Request:</label>
            <textarea id="request" name="request"></textarea><br><br>
            <button id="submit-request">Submit</button>
        </form>
        <div id="prayer-requests-list"></div>
    </section>

    <!-- Sermon Highlights Section -->
    <section class="sermon-highlights">
        <h2>Sermon Highlights</h2>
        <div class="sermon-cards">
            <div class="sermon-card">
                <h3>Sermon Title 1</h3>
                <p>Summary of sermon 1.</p>
                <button>Watch Now</button>
            </div>
            <div class="sermon-card">
                <h3>Sermon Title 2</h3>
                <p>Summary of sermon 2.</p>
                <button>Watch Now</button>
            </div>
            <div class="sermon-card">
                <h3>Sermon Title 3</h3>
                <p>Summary of sermon 3.</p>
                <button>Watch Now</button>
            </div>
        </div>
    </section>

    <!-- Online Donations Section -->
    <section class="online-donations">
        <h2>Support Our Ministry</h2>
        <p>Give online to support our church's mission.</p>
        <form id="donation-form">
            <label for="amount">Amount:</label>
            <input type="number" id="amount" name="amount"><br><br>
            <label for="donation-type">Donation Type:</label>
            <select id="donation-type" name="donation-type">
                <option value="one-time">One-Time</option>
                <option value="recurring">Recurring</option>
            </select><br><br>
            <button id="make-donation">Donate</button>
        </form>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Our Church. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
/* Global Styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
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
    display: flex;
    justify-content: space-between;
}

header nav ul li {
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

.prayer-requests {
    padding: 2em;
}

.prayer-requests h2 {
    margin-top: 0;
}

#prayer-request-form {
    margin-bottom: 20px;
}

#prayer-requests-list {
    margin-top: 20px;
}

.sermon-highlights {
    padding: 2em;
}

.sermon-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.sermon-card {
    background-color: #fff;
    padding: 1em;
    margin: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: calc(33.33% - 2em);
}

.online-donations {
    padding: 2em;
}

#donation-form {
    margin-bottom: 20px;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}

/* Responsive Design */
@media only screen and (max-width: 768px) {
    .sermon-card {
        width: calc(50% - 2em);
    }
}

@media only screen and (max-width: 480px) {
    .sermon-card {
        width: 100%;
    }
}
```

**script.js**
```javascript
// Prayer Request Form Submission
document.getElementById('prayer-request-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const request = document.getElementById('request').value;
    // Send data to server or API for processing
    console.log(`Prayer request from ${name}: ${request}`);
    document.getElementById('prayer-request-form').reset();
});

// Online Donation Form Submission
document.getElementById('donation-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const amount = document.getElementById('amount').value;
    const donationType = document.getElementById('donation-type').value;
    // Send data to server or API for processing
    console.log(`Donation of ${amount} ${donationType}`);
    document.getElementById('donation-form').reset();
});
```
