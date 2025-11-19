"""
Generated Code Metadata:
========================
Original URL: https://mujeresautistas.com
Prompt: Develop a web form using HTML and JavaScript for collecting trial lesson requests, including fields for name, email, phone number, and preferred dance class, similar to the contact form on Sakura Dance Studio's site.
Generated: DETERMINISTIC_fd62e9345b98d6e6
Batch ID: 20250612_154837
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
    <title>Trial Lesson Request Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .form-container {
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: auto;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input, select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
        }
        button:hover {
            background-color: #218838;
        }
        .error {
            color: red;
            font-size: 0.9em;
        }
    </style>
</head>
<body>

<div class="form-container">
    <h2>Request a Trial Lesson</h2>
    <form id="trialLessonForm">
        <div class="form-group">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <div class="error" id="nameError"></div>
        </div>
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <div class="error" id="emailError"></div>
        </div>
        <div class="form-group">
            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required>
            <div class="error" id="phoneError"></div>
        </div>
        <div class="form-group">
            <label for="danceClass">Preferred Dance Class:</label>
            <select id="danceClass" name="danceClass" required>
                <option value="">Select a class</option>
                <option value="Ballet">Ballet</option>
                <option value="Hip Hop">Hip Hop</option>
                <option value="Jazz">Jazz</option>
                <option value="Contemporary">Contemporary</option>
            </select>
            <div class="error" id="classError"></div>
        </div>
        <button type="submit">Submit Request</button>
    </form>
</div>

<script>
    // Function to validate the form inputs
    function validateForm(event) {
        event.preventDefault(); // Prevent form submission

        // Clear previous error messages
        document.getElementById('nameError').innerText = '';
        document.getElementById('emailError').innerText = '';
        document.getElementById('phoneError').innerText = '';
        document.getElementById('classError').innerText = '';

        // Get form values
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const phone = document.getElementById('phone').value.trim();
        const danceClass = document.getElementById('danceClass').value;

        let isValid = true;

        // Validate name
        if (name === '') {
            document.getElementById('nameError').innerText = 'Name is required.';
            isValid = false;
        }

        // Validate email
        if (email === '') {
            document.getElementById('emailError').innerText = 'Email is required.';
            isValid = false;
        } else if (!/\S+@\S+\.\S+/.test(email)) {
            document.getElementById('emailError').innerText = 'Email is invalid.';
            isValid = false;
        }

        // Validate phone
        if (phone === '') {
            document.getElementById('phoneError').innerText = 'Phone number is required.';
            isValid = false;
        }

        // Validate dance class selection
        if (danceClass === '') {
            document.getElementById('classError').innerText = 'Please select a dance class.';
            isValid = false;
        }

        // If the form is valid, proceed with submission
        if (isValid) {
            // Here you can handle the form submission, e.g., send data to a server
            alert('Form submitted successfully!');
            // Reset the form
            document.getElementById('trialLessonForm').reset();
        }
    }

    // Attach the validateForm function to the form's submit event
    document.getElementById('trialLessonForm').addEventListener('submit', validateForm);
</script>

</body>
</html>
```
