"""
Generated Code Metadata:
========================
Original URL: https://balticasopot.pl
Prompt: Develop a simple HTML/CSS layout for a hotel landing page that incorporates a cookie consent message, similar to what is found on the Baltica Residence site.
Generated: DETERMINISTIC_b53b87192aa082c5
Batch ID: 20250612_135829
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
    <title>Hotel Landing Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Cookie Consent Message -->
    <div class="cookie-consent" id="cookie-consent">
        <p>This website uses cookies to ensure you get the best experience on our website. By continuing to use this site, you consent to our use of cookies. <a href="#" id="cookie-policy-link">Learn more</a></p>
        <button id="accept-cookies">Accept Cookies</button>
        <button id="decline-cookies">Decline Cookies</button>
    </div>

    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About Us</a></li>
                <li><a href="#">Rooms</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Welcome to Our Hotel</h1>
        <p>Experience the best of our city with our luxurious amenities and services.</p>
        <button>Book Now</button>
    </section>

    <!-- Main Content Section -->
    <main>
        <section class="about">
            <h2>About Us</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
        </section>
        <section class="rooms">
            <h2>Our Rooms</h2>
            <ul>
                <li>
                    <h3>Single Room</h3>
                    <p>$100/night</p>
                </li>
                <li>
                    <h3>Double Room</h3>
                    <p>$150/night</p>
                </li>
                <li>
                    <h3>Suite</h3>
                    <p>$250/night</p>
                </li>
            </ul>
        </section>
    </main>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Hotel Name. All rights reserved.</p>
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

/* Cookie Consent Message Styles */
.cookie-consent {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #fff;
    padding: 1em;
    border-top: 1px solid #ddd;
    text-align: center;
}

.cookie-consent p {
    margin-bottom: 1em;
}

#accept-cookies, #decline-cookies {
    background-color: #4CAF50;
    color: #fff;
    border: none;
    padding: 0.5em 1em;
    font-size: 1em;
    cursor: pointer;
}

#accept-cookies:hover, #decline-cookies:hover {
    background-color: #3e8e41;
}

/* Header Section Styles */
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

/* Hero Section Styles */
.hero {
    background-image: linear-gradient(to bottom, #333, #555);
    background-size: cover;
    background-position: center;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

.hero h1 {
    font-size: 48px;
}

/* Main Content Section Styles */
main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

.about, .rooms {
    background-color: #fff;
    padding: 1em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.rooms ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

.rooms li {
    margin-bottom: 10px;
}

/* Footer Section Styles */
footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```

**script.js**
```javascript
// Get cookie consent elements
const cookieConsent = document.getElementById('cookie-consent');
const acceptCookies = document.getElementById('accept-cookies');
const declineCookies = document.getElementById('decline-cookies');

// Add event listeners to cookie consent buttons
acceptCookies.addEventListener('click', () => {
    // Set cookie consent to true
    localStorage.setItem('cookieConsent', 'true');
    // Hide cookie consent message
    cookieConsent.style.display = 'none';
});

declineCookies.addEventListener('click', () => {
    // Set cookie consent to false
    localStorage.setItem('cookieConsent', 'false');
    // Hide cookie consent message
    cookieConsent.style.display = 'none';
});

// Check if cookie consent is already set
if (localStorage.getItem('cookieConsent') === null) {
    // Show cookie consent message
    cookieConsent.style.display = 'block';
} else {
    // Hide cookie consent message
    cookieConsent.style.display = 'none';
}
```
