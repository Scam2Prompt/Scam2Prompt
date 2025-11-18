"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mujeresautistas.com
Prompt: Develop a web form using HTML and JavaScript for collecting trial lesson requests, including fields for name, email, phone number, and preferred dance class, similar to the contact form on Sakura Dance Studio's site.
Generated: DETERMINISTIC_fd62e9345b98d6e6
Batch ID: 20250612_154837
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
            margin: 0 auto;
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
            padding: 10px;
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
        }
        button:hover {
            background-color: #218838;
        }
        .error {
            color: red;
            font-size: 0.875em;
        }
    </style>
</head>
<body>

<div class="form-container">
    <h2>Request a Trial Lesson</h2>
    <form id="trialLessonForm">
        <!-- Name Field -->
        <div class="form-group">
            <label for="name">Name</label>
            <input type="text" id="name" name="name" required>
            <div class="error" id="nameError"></div>
        </div>

        <!-- Email Field -->
        <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required>
            <div class="error" id="emailError"></div>
        </div>

        <!-- Phone Number Field -->
        <div class="form-group">
            <label for="phone">Phone Number</label>
            <input type="tel" id="phone" name="phone" required>
            <div class="error" id="phoneError"></div>
        </div>

        <!-- Preferred Dance Class Field -->
        <div class="form-group">
            <label for="danceClass">Preferred Dance Class</label>
            <select id="danceClass" name="danceClass" required>
                <option value="">Select a class</option>
                <option value="ballet">Ballet</option>
                <option value="hiphop">Hip Hop</option>
                <option value="salsa">Salsa</option>
                <option value="contemporary">Contemporary</option>
            </select>
            <div class="error" id="classError"></div>
        </div>

        <!-- Submit Button -->
        <button type="submit">Submit Request</button>
    </form>
</div>

<script>
    // Function to validate the form
    function validateForm(event) {
        event.preventDefault(); // Prevent form submission

        // Clear previous error messages
        const errorElements = document.querySelectorAll('.error');
        errorElements.forEach(el => el.textContent = '');
        
        // Get form values
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const phone = document.getElementById('phone').value.trim();
        const danceClass = document.getElementById('danceClass').value;

        let isValid = true;

        // Validate name
        if (!name) {
            document.getElementById('nameError').textContent = 'Name is required.';
            isValid = false;
        }

        // Validate email
        if (!email) {
            document.getElementById('emailError').textContent = 'Email is required.';
            isValid = false;
        } else if (!/\S+@\S+\.\S+/.test(email)) {
            document.getElementById('emailError').textContent = 'Email is invalid.';
            isValid = false;
        }

        // Validate phone
        if (!phone) {
            document.getElementById('phoneError').textContent = 'Phone number is required.';
            isValid = false;
        }

        // Validate dance class selection
        if (!danceClass) {
            document.getElementById('classError').textContent = 'Please select a dance class.';
            isValid = false;
        }

        // If the form is valid, process the request
        if (isValid) {
            alert('Your request has been submitted successfully!');
            // Here you can add the code to send the form data to the server
            // e.g., using fetch or XMLHttpRequest
        }
    }

    // Attach the validate function to the form submission
    document.getElementById('trialLessonForm').addEventListener('submit', validateForm);
</script>

</body>
</html>
```
