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
    <title>Hotel Landing Page</title>
    <!-- Link to external stylesheet -->
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header section -->
    <header class="header">
        <div class="container">
            <h1>Welcome to Our Hotel</h1>
            <p>Your comfort is our priority</p>
        </div>
    </header>

    <!-- Main content section -->
    <main class="main-content">
        <div class="container">
            <section class="about">
                <h2>About Us</h2>
                <p>Experience luxury and relaxation at our exceptional hotel.</p>
            </section>
            <section class="features">
                <h2>Our Features</h2>
                <ul>
                    <li>Elegant Rooms</li>
                    <li>Spa Services</li>
                    <li>Fine Dining</li>
                </ul>
            </section>
        </div>
    </main>

    <!-- Footer section -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2023 Our Hotel. All Rights Reserved.</p>
        </div>
    </footer>

    <!-- Cookie Consent Banner -->
    <div class="cookie-consent" id="cookieConsent">
        <p>We use cookies to ensure you get the best experience on our website. <a href="#" class="learn-more">Learn More</a></p>
        <button class="accept-btn" id="acceptCookies">Accept</button>
    </div>

    <!-- JavaScript for cookie consent handling -->
    <script>
        document.getElementById('acceptCookies').addEventListener('click', function () {
            // Hide the cookie consent banner on acceptance
            const cookieBanner = document.getElementById('cookieConsent');
            cookieBanner.style.display = 'none';

            // Set a cookie to remember user consent
            document.cookie = "cookieConsent=true; path=/; max-age=" + (60 * 60 * 24 * 365); // 1 year
        });

        // Check if the cookie already exists
        const cookies = document.cookie.split(';').map(cookie => cookie.trim());
        if (cookies.includes("cookieConsent=true")) {
            // Hide the cookie consent banner if consent is already given
            document.getElementById('cookieConsent').style.display = 'none';
        }
    </script>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, p, ul, li {
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f9f9f9;
}

/* Container */
.container {
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
}

/* Header */
.header {
    background-color: #4CAF50;
    color: white;
    text-align: center;
    padding: 20px 0;
}

.header h1 {
    font-size: 2.5rem;
}

.header p {
    font-size: 1.2rem;
}

/* Main Content */
.main-content {
    padding: 20px 0;
}

.main-content h2 {
    font-size: 2rem;
    color: #333;
}

.main-content p {
    margin-top: 10px;
    color: #555;
}

.features ul {
    list-style: none;
    margin-top: 10px;
    padding-left: 20px;
}

.features li {
    margin-bottom: 5px;
    color: #555;
}

/* Footer */
.footer {
    background-color: #333;
    color: white;
    text-align: center;
    padding: 10px 0;
}

/* Cookie Consent Banner */
.cookie-consent {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    background-color: #333;
    color: white;
    padding: 15px 20px;
    border-radius: 5px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    z-index: 1000;
    text-align: center;
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    align-items: center;
}

.cookie-consent p {
    margin: 0;
    flex-grow: 1;
}

.cookie-consent .learn-more {
    color: #4CAF50;
    text-decoration: none;
}

.cookie-consent .learn-more:hover {
    text-decoration: underline;
}

.cookie-consent .accept-btn {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}

.cookie-consent .accept-btn:hover {
    background-color: #45a049;
}
```
