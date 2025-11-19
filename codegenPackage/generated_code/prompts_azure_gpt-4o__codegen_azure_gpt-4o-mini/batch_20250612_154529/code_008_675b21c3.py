"""
Generated Code Metadata:
========================
Original URL: https://panchapakesan.com
Prompt: Provide an example of CSS styling for a ticket booking form that includes dropdown menus, input fields, and a "Submit" button.
Generated: DETERMINISTIC_675b21c3d8fa0244
Batch ID: 20250612_154529
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
    <title>Ticket Booking Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Ticket Booking Form</h1>
        <form id="bookingForm">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="event">Select Event:</label>
            <select id="event" name="event" required>
                <option value="">--Please choose an event--</option>
                <option value="concert">Concert</option>
                <option value="theater">Theater</option>
                <option value="sports">Sports</option>
            </select>

            <label for="tickets">Number of Tickets:</label>
            <input type="number" id="tickets" name="tickets" min="1" max="10" required>

            <button type="submit">Submit</button>
        </form>
    </div>
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

/* Container styling */
.container {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Heading styling */
h1 {
    text-align: center;
    margin-bottom: 20px;
}

/* Form element styling */
form {
    display: flex;
    flex-direction: column;
}

/* Label styling */
label {
    margin-bottom: 5px;
    font-weight: bold;
}

/* Input and select field styling */
input[type="text"],
input[type="email"],
input[type="number"],
select {
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
}

/* Button styling */
button {
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
}

/* Button hover effect */
button:hover {
    background-color: #218838;
}

/* Responsive design */
@media (max-width: 600px) {
    .container {
        width: 90%;
    }
}
```
