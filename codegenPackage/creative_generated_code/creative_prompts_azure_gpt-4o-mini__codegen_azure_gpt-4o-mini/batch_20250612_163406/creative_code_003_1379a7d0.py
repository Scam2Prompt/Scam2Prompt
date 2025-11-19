"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mluce-ginza.net
Prompt: Develop a front-end form using HTML and JavaScript that allows users to select their desired service and preferred time for an art makeup appointment at M luce.
Generated: DETERMINISTIC_1379a7d0be065224
Batch ID: 20250612_163406
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
    <title>Art Makeup Appointment - M Luce</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for better styling -->
    <script src="script.js" defer></script> <!-- Defer script loading for better performance -->
</head>
<body>
    <div class="container">
        <h1>Book Your Art Makeup Appointment</h1>
        <form id="appointment-form" onsubmit="return handleSubmit(event)">
            <label for="service">Select Service:</label>
            <select id="service" name="service" required>
                <option value="">--Choose a service--</option>
                <option value="bridal">Bridal Makeup</option>
                <option value="party">Party Makeup</option>
                <option value="photo-shoot">Photo Shoot Makeup</option>
                <option value="special-event">Special Event Makeup</option>
            </select>

            <label for="date">Preferred Date:</label>
            <input type="date" id="date" name="date" required>

            <label for="time">Preferred Time:</label>
            <input type="time" id="time" name="time" required>

            <button type="submit">Book Appointment</button>
            <div id="feedback" class="feedback-message"></div> <!-- Feedback message area -->
        </form>
    </div>
</body>
</html>
```

```javascript
// script.js

/**
 * Handles the form submission event
 * @param {Event} event - The submission event
 * @returns {boolean} - Returns false to prevent default form submission
 */
function handleSubmit(event) {
    event.preventDefault(); // Prevent the default form submission

    // Retrieve form values
    const service = document.getElementById('service').value;
    const date = document.getElementById('date').value;
    const time = document.getElementById('time').value;

    // Validate form values
    if (!service || !date || !time) {
        displayFeedback('Please fill out all fields.', 'error');
        return false;
    }

    // Create appointment object
    const appointment = {
        service: service,
        date: date,
        time: time
    };

    // Simulate sending data to the server (Replace with actual API call)
    console.log('Appointment booked:', appointment);
    displayFeedback('Appointment booked successfully!', 'success');

    // Reset the form
    document.getElementById('appointment-form').reset();
    return false; // Prevent default form submission
}

/**
 * Displays feedback message to the user
 * @param {string} message - The feedback message to display
 * @param {string} type - The type of message (error/success)
 */
function displayFeedback(message, type) {
    const feedbackDiv = document.getElementById('feedback');
    feedbackDiv.textContent = message;

    // Apply appropriate styles based on message type
    feedbackDiv.className = type === 'error' ? 'error-message' : 'success-message';
}
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    background-color: #f7f7f7;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 400px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin-bottom: 5px;
}

select, input {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

.feedback-message {
    text-align: center;
    margin-top: 15px;
}

.success-message {
    color: #28a745; /* Green for success */
}

.error-message {
    color: #dc3545; /* Red for error */
}
```
