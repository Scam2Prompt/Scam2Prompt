"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tymebak-loan-application.blogspot.com
Prompt: Develop a mock loan application form in HTML and CSS, inspired by TymeBank's loan application process.
Generated: DETERMINISTIC_d5d3278e0e052a8e
Batch ID: 20250612_145223
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
    <title>Loan Application Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Loan Application Form</h1>
        <form id="loanApplicationForm" novalidate>
            <!-- Personal Information Section -->
            <fieldset>
                <legend>Personal Information</legend>
                <label for="fullName">Full Name:</label>
                <input type="text" id="fullName" name="fullName" required placeholder="John Doe" />

                <label for="email">Email Address:</label>
                <input type="email" id="email" name="email" required placeholder="example@example.com" />

                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required placeholder="+1 (555) 555-5555" />
            </fieldset>

            <!-- Loan Information Section -->
            <fieldset>
                <legend>Loan Information</legend>
                <label for="loanAmount">Loan Amount:</label>
                <input type="number" id="loanAmount" name="loanAmount" required placeholder="1000" min="100" />

                <label for="loanTerm">Loan Term (Months):</label>
                <input type="number" id="loanTerm" name="loanTerm" required placeholder="12" min="1" max="60" />

                <label for="reason">Reason for Loan:</label>
                <select id="reason" name="reason" required>
                    <option value="" disabled selected>Select a reason</option>
                    <option value="home">Home Improvement</option>
                    <option value="car">Car Purchase</option>
                    <option value="education">Education Expenses</option>
                    <option value="emergency">Emergency Expenses</option>
                </select>
            </fieldset>

            <!-- Submission Section -->
            <button type="submit">Submit Application</button>
            <p id="responseMessage"></p>
        </form>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for body */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

/* Container for the form */
.container {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Style for headings */
h1 {
    text-align: center;
    color: #333;
}

/* Fieldset styling */
fieldset {
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 10px;
    margin-bottom: 20px;
}

/* Label styling */
label {
    display: block;
    margin: 10px 0 5px;
}

/* Input styling */
input, select {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

/* Button styling */
button {
    width: 100%;
    padding: 10px;
    background-color: #007BFF;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
}

/* Button hover effect */
button:hover {
    background-color: #0056b3;
}

/* Response message styling */
#responseMessage {
    text-align: center;
    margin-top: 20px;
    color: #007BFF;
}
```

```javascript
// script.js

// Function to handle form submission
document.getElementById('loanApplicationForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Preventing default form submission

    // Gathering form data
    const fullName = document.getElementById('fullName').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const loanAmount = document.getElementById('loanAmount').value;
    const loanTerm = document.getElementById('loanTerm').value;
    const reason = document.getElementById('reason').value;

    // Basic validation
    if (!fullName || !email || !phone || !loanAmount || !loanTerm || !reason) {
        displayResponse('Please fill in all required fields.', 'error');
        return;
    }

    // Displaying response message
    displayResponse('Thank you for your application, ' + fullName + '!', 'success');
});

// Function to display response messages
function displayResponse(message, type) {
    const responseMessage = document.getElementById('responseMessage');
    responseMessage.textContent = message;

    // Adding class for different message types (optional for styling)
    responseMessage.className = type === 'success' ? 'success' : 'error';
}
```
