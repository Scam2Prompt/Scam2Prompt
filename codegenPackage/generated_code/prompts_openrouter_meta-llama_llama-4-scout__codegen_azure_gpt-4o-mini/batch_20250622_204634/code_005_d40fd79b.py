"""
Generated Code Metadata:
========================
Original URL: https://aamctg.edu.bd
Prompt: "Design a basic webpage structure for Ashekane Aulia Fazil Madrasah's online admission portal, including sections for application, result checking, and important notices."
Generated: DETERMINISTIC_d40fd79b8f45c1b0
Batch ID: 20250622_204634
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
    <title>Ashekane Aulia Fazil Madrasah - Online Admission Portal</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Ashekane Aulia Fazil Madrasah</h1>
        <nav>
            <ul>
                <li><a href="#application">Application</a></li>
                <li><a href="#result-check">Result Checking</a></li>
                <li><a href="#notices">Important Notices</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="application">
            <h2>Online Application</h2>
            <form action="submit_application.php" method="POST" id="application-form">
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required>

                <label for="program">Select Program:</label>
                <select id="program" name="program" required>
                    <option value="fazel">Fazel</option>
                    <option value="alim">Alim</option>
                    <option value="hifz">Hifz</option>
                </select>

                <button type="submit">Submit Application</button>
            </form>
        </section>

        <section id="result-check">
            <h2>Check Your Result</h2>
            <form action="check_result.php" method="GET" id="result-check-form">
                <label for="application-id">Application ID:</label>
                <input type="text" id="application-id" name="application_id" required>

                <button type="submit">Check Result</button>
            </form>
        </section>

        <section id="notices">
            <h2>Important Notices</h2>
            <ul>
                <li>Admissions are open from January 1 to March 31.</li>
                <li>Results will be announced on April 15.</li>
                <li>Please ensure all documents are submitted before the deadline.</li>
            </ul>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Ashekane Aulia Fazil Madrasah. All rights reserved.</p>
    </footer>

    <script src="script.js"></script> <!-- Link to external JavaScript for interactivity -->
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
    background-color: #f4f4f4;
}

/* Header styling */
header {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
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
    color: #ffffff;
    text-decoration: none;
}

/* Main content styling */
main {
    padding: 20px;
}

/* Section styling */
section {
    background: #ffffff;
    margin: 20px 0;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Form styling */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin: 10px 0 5px;
}

form input, form select, form button {
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

/* Button styling */
form button {
    background: #35424a;
    color: #ffffff;
    border: none;
    cursor: pointer;
}

form button:hover {
    background: #2c3e50;
}

/* Footer styling */
footer {
    text-align: center;
    padding: 10px 0;
    background: #35424a;
    color: #ffffff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// script.js

// This script can be used for form validation or interactivity in the future.
// Currently, it is a placeholder for future enhancements.

// Example of a simple form validation
document.getElementById('application-form').addEventListener('submit', function(event) {
    // Perform any necessary validation here
    // If validation fails, prevent form submission
    // event.preventDefault();
});
```
