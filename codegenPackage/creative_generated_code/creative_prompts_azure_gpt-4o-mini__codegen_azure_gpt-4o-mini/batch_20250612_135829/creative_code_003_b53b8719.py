"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balticasopot.pl
Prompt: Develop a simple HTML/CSS layout for a hotel landing page that incorporates a cookie consent message, similar to what is found on the Baltica Residence site.
Generated: DETERMINISTIC_b53b87192aa082c5
Batch ID: 20250612_135829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Welcome to Baltica Residence - Your perfect hotel getaway.">
    <title>Baltica Residence - Hotel Landing Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <div class="logo">Baltica Residence</div>
            <ul class="nav-links">
                <li><a href="#about">About</a></li>
                <li><a href="#rooms">Rooms</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section class="hero">
            <h1>Welcome to Baltica Residence</h1>
            <p>Your perfect getaway awaits.</p>
            <a href="#rooms" class="cta-button">View Rooms</a>
        </section>

        <section id="about">
            <h2>About Us</h2>
            <p>We offer luxurious accommodations and exceptional service for a memorable stay.</p>
        </section>

        <section id="rooms">
            <h2>Our Rooms</h2>
            <p>Explore our variety of rooms designed for comfort and style.</p>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <p>Get in touch for bookings and inquiries.</p>
        </section>
    </main>

    <!-- Cookie Consent Message -->
    <div id="cookie-consent" class="cookie-consent">
        <p>This website uses cookies to ensure you get the best experience on our website. 
            <a href="/privacy-policy" target="_blank">Learn More</a>
        </p>
        <button id="accept-cookies">Accept</button>
    </div>

    <footer>
        <p>&copy; 2023 Baltica Residence. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, p {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
}

/* Header styles */
header {
    background-color: #2c3e50;
    color: white;
    padding: 1rem;
}

nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.nav-links {
    list-style: none;
    display: flex;
}

.nav-links li {
    margin: 0 15px;
}

.nav-links a {
    color: white;
    text-decoration: none;
}

/* Hero section styles */
.hero {
    background: url('hotel-hero.jpg') no-repeat center center/cover;
    color: white;
    text-align: center;
    padding: 100px 20px;
}

/* Button styles */
.cta-button {
    background-color: #e74c3c;
    color: white;
    padding: 10px 20px;
    text-decoration: none;
    border-radius: 5px;
}

/* Cookie consent styles */
.cookie-consent {
    background-color: #333;
    color: white;
    padding: 15px;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    text-align: center;
}

/* Footer styles */
footer {
    background-color: #2c3e50;
    color: white;
    text-align: center;
    padding: 15px;
    position: relative;
}
```

```javascript
// script.js

// Function to handle cookie consent
document.getElementById('accept-cookies').addEventListener('click', function() {
    // Hide cookie consent message
    const cookieConsent = document.getElementById('cookie-consent');
    cookieConsent.style.display = 'none';

    // Set a cookie to remember consent (for demonstration purposes)
    document.cookie = "cookieConsent=true; max-age=" + 60 * 60 * 24 * 30; // 30 days
});

// Check if the cookie consent has already been given
function checkCookieConsent() {
    const cookies = document.cookie.split('; ');
    const cookieConsent = cookies.find(row => row.startsWith('cookieConsent='));

    if (cookieConsent) {
        // If consent cookie exists, hide the consent message
        document.getElementById('cookie-consent').style.display = 'none';
    }
}

// Execute the cookie consent check on page load
window.onload = checkCookieConsent;
```
