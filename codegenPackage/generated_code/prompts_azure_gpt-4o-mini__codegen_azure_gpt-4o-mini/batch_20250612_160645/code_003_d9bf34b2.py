"""
Generated Code Metadata:
========================
Original URL: https://rembytservis02.ru
Prompt: Develop a simple web form in HTML/CSS for users to submit their requests for selling laptops and computers, referencing the service details provided on the site.
Generated: DETERMINISTIC_d9bf34b232e56e38
Batch ID: 20250612_160645
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
    <title>Sell Your Laptop/Computer</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Request to Sell Your Laptop/Computer</h1>
        <form id="sellForm" action="/submit-request" method="POST">
            <label for="name">Your Name:</label>
            <input type="text" id="name" name="name" required placeholder="Enter your name">

            <label for="email">Your Email:</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email">

            <label for="deviceType">Device Type:</label>
            <select id="deviceType" name="deviceType" required>
                <option value="" disabled selected>Select your device type</option>
                <option value="laptop">Laptop</option>
                <option value="desktop">Desktop Computer</option>
            </select>

            <label for="deviceModel">Device Model:</label>
            <input type="text" id="deviceModel" name="deviceModel" required placeholder="Enter device model">

            <label for="condition">Condition:</label>
            <textarea id="condition" name="condition" required placeholder="Describe the condition of your device"></textarea>

            <button type="submit">Submit Request</button>
        </form>
    </div>

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

/* Container styling */
.container {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
}

/* Heading styling */
h1 {
    text-align: center;
    margin-bottom: 20px;
}

/* Form element styling */
label {
    display: block;
    margin-bottom: 5px;
}

input, select, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

/* Button styling */
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
```

```javascript
// script.js

// Add an event listener to the form for submission
document.getElementById('sellForm').addEventListener('submit', function(event) {
    // Prevent the default form submission
    event.preventDefault();

    // Gather form data
    const formData = new FormData(this);

    // Send the form data to the server
    fetch(this.action, {
        method: this.method,
        body: formData,
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        // Handle success response
        alert('Request submitted successfully: ' + data.message);
    })
    .catch(error => {
        // Handle error response
        console.error('There was a problem with the fetch operation:', error);
        alert('There was an error submitting your request. Please try again later.');
    });
});
```
