"""
Generated Code Metadata:
========================
Original URL: https://rdmerakyat.com
Prompt: Write code to implement a privacy policy and terms and conditions page for an architectural solutions website, ensuring compliance with modern web standards.
Generated: DETERMINISTIC_14e1976c21ba0c42
Batch ID: 20250612_153400
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
    <title>Privacy Policy & Terms and Conditions</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Architectural Solutions</h1>
        <nav>
            <ul>
                <li><a href="#privacy-policy">Privacy Policy</a></li>
                <li><a href="#terms-conditions">Terms and Conditions</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="privacy-policy">
            <h2>Privacy Policy</h2>
            <p>Last updated: <span id="last-updated"></span></p>
            <p>Your privacy is important to us. This privacy policy explains how we collect, use, and protect your information.</p>
            <h3>Information We Collect</h3>
            <ul>
                <li>Personal Information: Name, email address, etc.</li>
                <li>Usage Data: Information on how you use our website.</li>
            </ul>
            <h3>How We Use Your Information</h3>
            <p>We use your information to:</p>
            <ul>
                <li>Provide and maintain our services.</li>
                <li>Notify you about changes to our services.</li>
                <li>Provide customer support.</li>
            </ul>
            <h3>Data Security</h3>
            <p>We take reasonable measures to protect your information from unauthorized access.</p>
        </section>

        <section id="terms-conditions">
            <h2>Terms and Conditions</h2>
            <p>Last updated: <span id="last-updated-terms"></span></p>
            <p>By accessing our website, you agree to comply with these terms and conditions.</p>
            <h3>Use of the Site</h3>
            <p>You may use our site only for lawful purposes and in accordance with these terms.</p>
            <h3>Intellectual Property</h3>
            <p>All content on this site is the property of Architectural Solutions and is protected by copyright laws.</p>
            <h3>Limitation of Liability</h3>
            <p>In no event shall we be liable for any damages arising from the use of our site.</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Architectural Solutions. All rights reserved.</p>
    </footer>

    <script>
        // Function to set the last updated date dynamically
        function setLastUpdatedDate() {
            const currentDate = new Date();
            const options = { year: 'numeric', month: 'long', day: 'numeric' };
            const formattedDate = currentDate.toLocaleDateString(undefined, options);
            document.getElementById('last-updated').textContent = formattedDate;
            document.getElementById('last-updated-terms').textContent = formattedDate;
        }

        // Call the function to set the last updated date on page load
        window.onload = setLastUpdatedDate;
    </script>
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
    line-height: 1.6;
    padding: 20px;
    background-color: #f4f4f4;
}

/* Header styling */
header {
    background: #333;
    color: #fff;
    padding: 10px 0;
    text-align: center;
}

/* Navigation styling */
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

/* Main content styling */
main {
    margin: 20px 0;
    background: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Footer styling */
footer {
    text-align: center;
    margin-top: 20px;
    font-size: 0.9em;
}
```
