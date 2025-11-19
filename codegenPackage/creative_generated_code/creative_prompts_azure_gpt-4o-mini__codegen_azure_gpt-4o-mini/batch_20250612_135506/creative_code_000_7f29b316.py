"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://regency-towel.com
Prompt: Generate a code snippet for an online inquiry form that captures customer details for towel orders, similar to the inquiry process at Regency Towel.
Generated: DETERMINISTIC_7f29b31635f391ba
Batch ID: 20250612_135506
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
    <title>Towel Order Inquiry Form</title>
    <link rel="stylesheet" href="styles.css">
    <script defer src="script.js"></script>
</head>
<body>
    <h1>Towel Order Inquiry Form</h1>
    <form id="inquiryForm">
        <label for="fullName">Full Name:</label>
        <input type="text" id="fullName" name="fullName" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" required>

        <label for="quantity">Quantity:</label>
        <input type="number" id="quantity" name="quantity" min="1" required>

        <label for="towelType">Towel Type:</label>
        <select id="towelType" name="towelType" required>
            <option value="" disabled selected>Select a towel type</option>
            <option value="bath">Bath Towel</option>
            <option value="hand">Hand Towel</option>
            <option value="beach">Beach Towel</option>
        </select>

        <label for="message">Additional Message:</label>
        <textarea id="message" name="message"></textarea>

        <button type="submit">Submit Inquiry</button>
    </form>
    <div id="responseMessage" class="hidden"></div>
</body>
</html>
```

```css
/* styles.css */

/* Basic styling for the inquiry form */
body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    padding: 20px;
}

h1 {
    color: #333;
}

form {
    background-color: #fff;
    padding: 15px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-top: 10px;
}

input, select, textarea {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    margin-top: 15px;
    padding: 10px;
    background-color: #5cb85c;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #4cae4c;
}

.hidden {
    display: none;
}

.response-success {
    color: green;
}

.response-error {
    color: red;
}
```

```javascript
// script.js

// Function to handle form submission
document.getElementById('inquiryForm').addEventListener('submit', async function (event) {
    // Prevent default form submission
    event.preventDefault();

    // Gather form data
    const formData = new FormData(this);

    try {
        // Send form data to the server
        const response = await fetch('/submit-inquiry', {
            method: 'POST',
            body: formData
        });

        // Check for a successful response
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        // Handle success response
        const responseData = await response.json();
        displayResponseMessage(`Success: ${responseData.message}`, 'response-success');
    } catch (error) {
        // Handle errors
        displayResponseMessage(`Error: ${error.message}`, 'response-error');
    }
});

// Function to display response messages
function displayResponseMessage(message, responseClass) {
    const responseMessageDiv = document.getElementById('responseMessage');
    responseMessageDiv.textContent = message;
    responseMessageDiv.className = responseClass;
    responseMessageDiv.classList.remove('hidden');
}
```

**Note:** Ensure you have a backend route (`/submit-inquiry`) to handle the form submission and respond with appropriate JSON data for this code to be fully functional in a production environment.
