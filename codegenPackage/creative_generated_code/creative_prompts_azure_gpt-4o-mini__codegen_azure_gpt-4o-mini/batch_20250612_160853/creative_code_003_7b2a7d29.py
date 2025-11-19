"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patenteimpresa.it
Prompt: Develop a simple HTML form for users to book a spot in the "Patente d'impresa" course, including dropdowns for event selection and user type.
Generated: DETERMINISTIC_7b2a7d29abb8e3df
Batch ID: 20250612_160853
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
    <title>Book Your Course Spot</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
    <script src="script.js" defer></script> <!-- Link to external JS for form handling -->
</head>

<body>
    <main>
        <h1>Book Your Spot for the "Patente d'impresa" Course</h1>
        <form id="bookingForm" action="/submit-booking" method="POST"> <!-- Form submission endpoint -->
            <label for="event">Select Event:</label>
            <select id="event" name="event" required>
                <option value="" disabled selected>Select an event</option>
                <option value="course1">Course 1: Introduction to Business</option>
                <option value="course2">Course 2: Advanced Business Strategies</option>
                <option value="course3">Course 3: Entrepreneurship Essentials</option>
            </select>

            <label for="userType">Select User Type:</label>
            <select id="userType" name="userType" required>
                <option value="" disabled selected>Select user type</option>
                <option value="student">Student</option>
                <option value="professional">Professional</option>
                <option value="entrepreneur">Entrepreneur</option>
            </select>

            <label for="name">Your Name:</label>
            <input type="text" id="name" name="name" required placeholder="Enter your full name">

            <label for="email">Your Email:</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email">

            <button type="submit">Book Now</button>
        </form>
        <div id="message"></div> <!-- Element for displaying messages -->
    </main>
</body>

</html>
```

```css
/* styles.css */

/* Basic reset for styling */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;
}

h1 {
    color: #333;
}

form {
    background: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin: 10px 0 5px;
}

input[type="text"],
input[type="email"],
select {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #28a745;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

#message {
    margin-top: 20px;
    color: red;
}
```

```javascript
// script.js

// Function to handle form submission
document.getElementById('bookingForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent default form submission
    
    // Gather form data
    const eventSelection = document.getElementById('event').value;
    const userType = document.getElementById('userType').value;
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;

    // Simple validation
    if (!eventSelection || !userType || !name || !email) {
        displayMessage('Please fill out all fields.');
        return;
    }

    // Simulate form submission (in production, you would send this data to the server)
    const bookingData = {
        event: eventSelection,
        userType: userType,
        name: name,
        email: email
    };

    console.log('Booking data:', bookingData);
    displayMessage('Booking successful! Thank you for signing up.'); // Success message
});

// Function to display messages to the user
function displayMessage(msg) {
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = msg; // Set the message content
}
```
