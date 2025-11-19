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
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ashekane Aulia Fazil Madrasah Online Admission Portal</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#application">Application</a></li>
                <li><a href="#result">Result</a></li>
                <li><a href="#notices">Notices</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Ashekane Aulia Fazil Madrasah Online Admission Portal</h1>
        <p>Welcome to the online admission portal of Ashekane Aulia Fazil Madrasah.</p>
    </section>

    <!-- Application Section -->
    <section id="application" class="application">
        <h2>Apply Online</h2>
        <form id="application-form">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone:</label>
            <input type="tel" id="phone" name="phone" required>

            <label for="program">Program:</label>
            <select id="program" name="program" required>
                <option value="">Select a program</option>
                <option value="fazil">Fazil</option>
                <option value="alim">Alim</option>
                <option value="others">Others</option>
            </select>

            <button type="submit">Submit Application</button>
        </form>
    </section>

    <!-- Result Section -->
    <section id="result" class="result">
        <h2>Check Result</h2>
        <form id="result-form">
            <label for="roll">Roll:</label>
            <input type="text" id="roll" name="roll" required>

            <label for="session">Session:</label>
            <select id="session" name="session" required>
                <option value="">Select a session</option>
                <option value="2022-2023">2022-2023</option>
                <option value="2023-2024">2023-2024</option>
            </select>

            <button type="submit">Check Result</button>
        </form>
    </section>

    <!-- Notices Section -->
    <section id="notices" class="notices">
        <h2>Important Notices</h2>
        <ul>
            <li>Notice 1: Admission date extended.</li>
            <li>Notice 2: Class schedule.</li>
            <li>Notice 3: Fee structure.</li>
        </ul>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Ashekane Aulia Fazil Madrasah. All rights reserved.</p>
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
    background-image: linear-gradient(to bottom, #f7f7f7, #ddd);
    padding: 5em;
    text-align: center;
}

.application, .result, .notices {
    padding: 2em;
}

label {
    display: block;
    margin-bottom: 10px;
}

input, select {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

button[type="submit"] {
    background-color: #333;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #444;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```

```javascript
// script.js

// Get the application form
const applicationForm = document.getElementById('application-form');

// Add event listener to the application form
applicationForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get the form data
    const formData = new FormData(applicationForm);

    // Send the form data to the server
    fetch('/apply', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
});

// Get the result form
const resultForm = document.getElementById('result-form');

// Add event listener to the result form
resultForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get the form data
    const formData = new FormData(resultForm);

    // Send the form data to the server
    fetch('/result', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
});
```
