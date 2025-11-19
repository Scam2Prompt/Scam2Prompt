"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tubalife.me
Prompt: Design a simple web form using HTML and JavaScript to allow users to inquire about services at TUBA SPA, including their contact details and preferred service.
Generated: DETERMINISTIC_8ee3eda7aa5d7caf
Batch ID: 20250612_161520
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
    <title>TUBA SPA Inquiry Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f7f7f7;
            margin: 0;
            padding: 20px;
        }
        h1 {
            color: #4CAF50;
        }
        form {
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        input, select, textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        .error {
            color: red;
            font-size: 0.9em;
        }
    </style>
</head>
<body>

<h1>Inquire About Our Services</h1>
<form id="inquiryForm">
    <label for="name">Full Name:</label>
    <input type="text" id="name" name="name" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>

    <label for="phone">Phone Number:</label>
    <input type="tel" id="phone" name="phone" required>

    <label for="service">Preferred Service:</label>
    <select id="service" name="service" required>
        <option value="">Select a service</option>
        <option value="massage">Massage</option>
        <option value="facial">Facial</option>
        <option value="manicure">Manicure</option>
        <option value="pedicure">Pedicure</option>
        <option value="body_treatment">Body Treatment</option>
    </select>

    <label for="message">Additional Message:</label>
    <textarea id="message" name="message" rows="4"></textarea>

    <button type="submit">Submit Inquiry</button>
    <div id="error-message" class="error"></div>
</form>

<script>
    // Function to handle form submission
    document.getElementById('inquiryForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Collect form data
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const phone = document.getElementById('phone').value.trim();
        const service = document.getElementById('service').value;
        const message = document.getElementById('message').value.trim();

        // Basic validation
        if (!name || !email || !phone || !service) {
            document.getElementById('error-message').textContent = "Please fill in all required fields.";
            return;
        }

        // Clear any previous error messages
        document.getElementById('error-message').textContent = "";

        // Prepare the inquiry data
        const inquiryData = {
            name: name,
            email: email,
            phone: phone,
            service: service,
            message: message
        };

        // Simulate sending the inquiry data (replace this with actual API call)
        console.log('Inquiry submitted:', inquiryData);
        alert('Your inquiry has been submitted successfully!');

        // Optionally, reset the form after submission
        document.getElementById('inquiryForm').reset();
    });
</script>

</body>
</html>
```
