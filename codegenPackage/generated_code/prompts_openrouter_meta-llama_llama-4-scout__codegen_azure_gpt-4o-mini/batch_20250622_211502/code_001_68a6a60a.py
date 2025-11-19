"""
Generated Code Metadata:
========================
Original URL: https://2323-50q.pages.dev
Prompt: Design a basic website structure and write the HTML code for a sample page with a greeting message.
Generated: DETERMINISTIC_68a6a60ad0b7e5da
Batch ID: 20250622_211502
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
    <meta name="description" content="A simple greeting page">
    <title>Greeting Page</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS file -->
    <script src="script.js" defer></script> <!-- Link to external JavaScript file -->
</head>
<body>
    <header>
        <h1>Welcome to My Website</h1> <!-- Main heading -->
    </header>
    
    <main>
        <section>
            <h2>Greeting Message</h2> <!-- Subheading for the greeting section -->
            <p id="greeting-message">Hello, visitor! We're glad to have you here.</p> <!-- Greeting message -->
        </section>
    </main>
    
    <footer>
        <p>&copy; 2023 My Website. All rights reserved.</p> <!-- Footer content -->
    </footer>
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
    font-family: Arial, sans-serif; /* Set a clean font */
    line-height: 1.6; /* Improve readability */
    background-color: #f4f4f4; /* Light background color */
    color: #333; /* Dark text color */
}

/* Header styles */
header {
    background: #007BFF; /* Blue background for header */
    color: #fff; /* White text color */
    padding: 20px; /* Padding for header */
    text-align: center; /* Center align text */
}

/* Main section styles */
main {
    padding: 20px; /* Padding for main content */
}

/* Footer styles */
footer {
    text-align: center; /* Center align footer text */
    padding: 10px; /* Padding for footer */
    background: #333; /* Dark background for footer */
    color: #fff; /* White text color */
}
```

```javascript
// script.js

// Function to display a greeting message
function displayGreeting() {
    const greetingElement = document.getElementById('greeting-message');
    if (greetingElement) {
        greetingElement.textContent = "Hello, visitor! Welcome to our website."; // Update greeting message
    } else {
        console.error("Greeting message element not found."); // Log error if element is not found
    }
}

// Execute the function when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', displayGreeting);
```
