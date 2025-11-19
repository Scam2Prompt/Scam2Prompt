"""
Generated Code Metadata:
========================
Original URL: https://jsa.academy
Prompt: "Generate a sample code for a simple web page that promotes a soccer academy program, including a call-to-action for volunteers to join, using HTML, CSS, and JavaScript."
Generated: DETERMINISTIC_3f3fb3d8d7f57e2f
Batch ID: 20250622_210655
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
    <title>Soccer Academy Program</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to Our Soccer Academy!</h1>
        <p>Join us in nurturing the next generation of soccer stars.</p>
    </header>

    <main>
        <section id="program-details">
            <h2>About Our Program</h2>
            <p>Our soccer academy offers professional coaching, skill development, and competitive play for all ages.</p>
            <ul>
                <li>Experienced Coaches</li>
                <li>State-of-the-art Facilities</li>
                <li>Inclusive Environment</li>
            </ul>
        </section>

        <section id="volunteer-call-to-action">
            <h2>Become a Volunteer!</h2>
            <p>We are looking for passionate individuals to help us make a difference. Join our team and support young athletes!</p>
            <button id="volunteer-button">Sign Up to Volunteer</button>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Soccer Academy. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
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
    background: #007bff;
    color: white;
    padding: 20px;
    text-align: center;
}

/* Main section styles */
main {
    padding: 20px;
}

/* Section styles */
section {
    margin-bottom: 20px;
    padding: 15px;
    background: white;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Button styles */
button {
    background: #28a745;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background: #218838;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px;
    background: #007bff;
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// script.js

// Function to handle volunteer sign-up
function handleVolunteerSignUp() {
    // Display a simple alert for demonstration purposes
    alert("Thank you for your interest in volunteering! We will contact you soon.");
}

// Add event listener to the volunteer button
document.getElementById("volunteer-button").addEventListener("click", handleVolunteerSignUp);
```
