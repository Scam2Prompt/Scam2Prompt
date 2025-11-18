"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.events
Prompt: Generate code for a mobile-friendly webpage that showcases event details and allows users to apply for roles like staff, volunteers, or lead positions for a festival like Celestia.
Generated: DETERMINISTIC_aed300b834a75f0f
Batch ID: 20250612_152326
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
    <title>Celestia Festival - Event Details</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <header>
        <h1>Welcome to Celestia Festival</h1>
        <nav>
            <ul>
                <li><a href="#event-details">Event Details</a></li>
                <li><a href="#apply-section">Apply for Roles</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="event-details">
            <h2>Event Details</h2>
            <p>Date: July 15-17, 2024</p>
            <p>Location: Celestia Park, Dream City</p>
            <p>Description: Join us for an unforgettable experience filled with music, art, and community!</p>
        </section>

        <section id="apply-section">
            <h2>Apply for Roles</h2>
            <form id="application-form" onsubmit="return submitApplication(event)">
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="role">Select Role:</label>
                <select id="role" name="role" required>
                    <option value="">--Select Role--</option>
                    <option value="staff">Staff</option>
                    <option value="volunteer">Volunteer</option>
                    <option value="lead">Lead</option>
                </select>

                <label for="message">Additional Information:</label>
                <textarea id="message" name="message" rows="4"></textarea>

                <button type="submit">Submit Application</button>
            </form>
            <div id="response-message"></div>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Celestia Festival. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, p {
    margin: 0;
    padding: 0;
}

/* Set basic styles for the body */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f9f9f9;
    color: #333;
}

/* Style the header */
header {
    background: #4a90e2;
    color: white;
    padding: 10px 0;
    text-align: center;
}

nav ul {
    list-style-type: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav a {
    color: white;
    text-decoration: none;
}

/* Main section styles */
main {
    padding: 20px;
}

/* Form styles */
form {
    display: flex;
    flex-direction: column;
    max-width: 600px;
    margin: auto;
}

form label {
    margin-top: 10px;
}

form input, form select, form textarea {
    padding: 10px;
    margin-top: 5px;
}

/* Button styling */
button {
    margin-top: 10px;
    padding: 10px;
    background: #4caf50;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background: #45a049;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 20px;
    background: #333;
    color: white;
}
```

```javascript
// script.js

/**
 * Submits the application form and handles the response.
 * @param {Event} event - The form submit event.
 * @returns {boolean} - Returns false to prevent default form submission.
 */
function submitApplication(event) {
    event.preventDefault(); // Prevent default form submission

    // Get form data
    const formData = new FormData(event.target);
    
    // Validate and collect data
    const applicationData = {
        name: formData.get('name'),
        email: formData.get('email'),
        role: formData.get('role'),
        message: formData.get('message'),
    };

    // Simulate form submission (placeholder for actual API call)
    console.log("Application submitted:", applicationData);
    displayResponseMessage("Your application has been submitted successfully!", true);

    // Return false to prevent default form submission
    return false;
}

/**
 * Displays a response message to the user.
 * @param {string} message - The message to display.
 * @param {boolean} isSuccess - Indicates if the submission was successful.
 */
function displayResponseMessage(message, isSuccess) {
    const responseMessageDiv = document.getElementById('response-message');
    responseMessageDiv.textContent = message;
    responseMessageDiv.style.color = isSuccess ? 'green' : 'red';
}
```
