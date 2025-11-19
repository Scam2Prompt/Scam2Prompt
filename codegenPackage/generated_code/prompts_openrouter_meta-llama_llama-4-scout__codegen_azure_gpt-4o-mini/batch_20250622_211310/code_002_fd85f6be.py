"""
Generated Code Metadata:
========================
Original URL: https://immediatecode-360.com
Prompt: Generate a code snippet that illustrates how to create a simple investment education website, like Immediate Code 360, using HTML, CSS, and JavaScript.
Generated: DETERMINISTIC_fd85f6bec6e7e270
Batch ID: 20250622_211310
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/real-estate": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/stocks": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/bonds": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Investment Education</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Investment Education Hub</h1>
        <nav>
            <ul>
                <li><a href="#about">About</a></li>
                <li><a href="#resources">Resources</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="about">
            <h2>About Us</h2>
            <p>We provide resources and education to help you make informed investment decisions.</p>
        </section>

        <section id="resources">
            <h2>Resources</h2>
            <ul id="resource-list">
                <!-- Resources will be dynamically populated here -->
            </ul>
            <button id="load-resources">Load Resources</button>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contact-form">
                <label for="name">Name:</label>
                <input type="text" id="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" required>
                
                <label for="message">Message:</label>
                <textarea id="message" required></textarea>
                
                <button type="submit">Send</button>
            </form>
            <div id="form-response"></div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Investment Education Hub. All rights reserved.</p>
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
}

/* Header styles */
header {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
    text-align: center;
}

nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav a {
    color: #ffffff;
    text-decoration: none;
}

/* Main section styles */
main {
    padding: 20px;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #35424a;
    color: #ffffff;
    position: relative;
    bottom: 0;
    width: 100%;
}

/* Form styles */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin: 10px 0 5px;
}

form input, form textarea {
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}
```

```javascript
// script.js

// Function to load resources dynamically
function loadResources() {
    const resources = [
        { title: "Understanding Stocks", link: "https://example.com/stocks" },
        { title: "Bonds Basics", link: "https://example.com/bonds" },
        { title: "Real Estate Investing", link: "https://example.com/real-estate" }
    ];

    const resourceList = document.getElementById('resource-list');
    resourceList.innerHTML = ''; // Clear existing resources

    resources.forEach(resource => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `<a href="${resource.link}" target="_blank">${resource.title}</a>`;
        resourceList.appendChild(listItem);
    });
}

// Function to handle form submission
function handleFormSubmit(event) {
    event.preventDefault(); // Prevent default form submission

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Simple validation
    if (!name || !email || !message) {
        alert("All fields are required!");
        return;
    }

    // Simulate form submission
    document.getElementById('form-response').innerText = `Thank you, ${name}! Your message has been sent.`;
    document.getElementById('contact-form').reset(); // Reset form fields
}

// Event listeners
document.getElementById('load-resources').addEventListener('click', loadResources);
document.getElementById('contact-form').addEventListener('submit', handleFormSubmit);
```
