"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genesisicu.com
Prompt: Construct a web form for users to report lost or stolen debit cards, incorporating the contact information and procedures outlined by Genesis Investment Credit Union.
Generated: DETERMINISTIC_139f9730f82ae2cd
Batch ID: 20250612_164021
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
    <title>Report Lost or Stolen Debit Card</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <div class="container">
        <h1>Report Lost or Stolen Debit Card</h1>
        <p>If your debit card is lost or stolen, please fill out the form below and follow the procedures outlined by Genesis Investment Credit Union.</p>

        <form id="reportForm" action="/submitReport" method="POST">
            <fieldset>
                <legend>Contact Information</legend>
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required>
            </fieldset>

            <fieldset>
                <legend>Card Information</legend>
                <label for="cardNumber">Debit Card Number:</label>
                <input type="text" id="cardNumber" name="cardNumber" required pattern="\d{16}">
                
                <label for="dateLost">Date Lost or Stolen:</label>
                <input type="date" id="dateLost" name="dateLost" required>
                
                <label for="details">Additional Details:</label>
                <textarea id="details" name="details" rows="4" placeholder="Provide any additional information..."></textarea>
            </fieldset>

            <button type="submit">Submit Report</button>
        </form>

        <div id="responseMessage" class="hidden"></div>
    </div>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;
}

.container {
    max-width: 600px;
    margin: auto;
    padding: 20px;
    background: white;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
    color: #333;
}

fieldset {
    border: 1px solid #ccc;
    padding: 15px;
    margin-bottom: 20px;
}

legend {
    font-weight: bold;
}

label {
    display: block;
    margin-bottom: 5px;
}

input, textarea {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #5cb85c;
    color: white;
    padding: 10px 15px;
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

#responseMessage {
    margin-top: 20px;
    padding: 10px;
    border: 1px solid #5cb85c;
    color: #5cb85c;
    background-color: #e6ffe6;
}
```

```javascript
// script.js

document.getElementById('reportForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Collect form data
    const formData = new FormData(this);

    // Send a POST request to the server with form data
    fetch('/submitReport', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('responseMessage').innerText = 'Report submitted successfully!';
        document.getElementById('responseMessage').classList.remove('hidden');
        this.reset(); // Clear the form fields
    })
    .catch(error => {
        document.getElementById('responseMessage').innerText = 'There was a problem submitting your report. Please try again later.';
        document.getElementById('responseMessage').classList.remove('hidden');
        console.error('Error:', error); // Log error for debugging
    });
});
```

### Note:
- Ensure that the server-side endpoint `/submitReport` is set up to handle the form submission.
- Styles and scripts should be placed in separate files (`styles.css` and `script.js`) for better maintainability.
