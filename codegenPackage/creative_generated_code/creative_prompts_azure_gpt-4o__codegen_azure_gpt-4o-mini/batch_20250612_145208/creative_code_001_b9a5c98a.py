"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millennium-capital.com
Prompt: Generate code for a contact form that allows users to submit proposals for joint ventures or licensing opportunities, referencing the structure described on Millennium Capital's site.
Generated: DETERMINISTIC_b9a5c98abc1debc8
Batch ID: 20250612_145208
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
    <title>Joint Venture Proposal Form</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <div class="container">
        <h1>Joint Venture and Licensing Proposal Form</h1>
        <form id="proposalForm" method="POST" action="/submit-proposal" novalidate>
            <div class="form-group">
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required placeholder="John Doe">
                <span class="error-message" aria-live="polite"></span>
            </div>
            <div class="form-group">
                <label for="email">Email Address:</label>
                <input type="email" id="email" name="email" required placeholder="john.doe@example.com">
                <span class="error-message" aria-live="polite"></span>
            </div>
            <div class="form-group">
                <label for="company">Company Name:</label>
                <input type="text" id="company" name="company" required placeholder="Your Company Name">
                <span class="error-message" aria-live="polite"></span>
            </div>
            <div class="form-group">
                <label for="proposal">Proposal Details:</label>
                <textarea id="proposal" name="proposal" required rows="5" placeholder="Describe your proposal..."></textarea>
                <span class="error-message" aria-live="polite"></span>
            </div>
            <button type="submit">Submit Proposal</button>
        </form>
        <div id="responseMessage" aria-live="polite"></div>
    </div>
</body>
</html>

<style>
    body {
        font-family: Arial, sans-serif;
        margin: 20px;
        padding: 20px;
        background-color: #f4f4f4;
    }
    .container {
        max-width: 600px;
        margin: auto;
        background: white;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .form-group {
        margin-bottom: 15px;
    }
    label {
        display: block;
        margin-bottom: 5px;
    }
    input, textarea {
        width: 100%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 4px;
    }
    .error-message {
        color: red;
        font-size: 0.9em;
    }
    button {
        padding: 10px 15px;
        background-color: #28a745;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    button:hover {
        background-color: #218838;
    }
</style>

<script>
    document.getElementById('proposalForm').addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default form submission

        // Retrieve form data
        const formData = new FormData(this);
        const data = Object.fromEntries(formData.entries());

        // Basic validation
        const errors = validateForm(data);
        if (errors.length > 0) {
            displayErrors(errors);
            return;
        }

        // Submit data via Fetch API
        fetch(this.action, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('responseMessage').innerText = 'Proposal submitted successfully!';
            this.reset(); // Reset the form
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            document.getElementById('responseMessage').innerText = 'Error submitting proposal. Please try again.';
        });
    });

    function validateForm(data) {
        const errors = [];
        if (!data.name) errors.push("Name is required.");
        if (!data.email || !/\S+@\S+\.\S+/.test(data.email)) errors.push("A valid email is required.");
        if (!data.company) errors.push("Company name is required.");
        if (!data.proposal) errors.push("Proposal details are required.");
        return errors;
    }

    function displayErrors(errors) {
        const errorElements = document.querySelectorAll('.error-message');
        errorElements.forEach(el => el.innerText = ''); // Clear previous errors
        errors.forEach((error, index) => {
            if (errorElements[index]) {
                errorElements[index].innerText = error;
            }
        });
    }
</script>
```
