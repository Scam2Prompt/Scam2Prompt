"""
Generated Code Metadata:
========================
Original URL: https://ptei.edu.bd
Prompt: Write a JavaScript code snippet to create a simple online application form for the BTEB Admission process, as mentioned on the PTEI website.
Generated: DETERMINISTIC_0c09a464ee14d1a6
Batch ID: 20250622_211723
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
    <title>BTEB Admission Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>BTEB Admission Application Form</h1>
        <form id="admissionForm" onsubmit="return handleSubmit(event)">
            <label for="fullName">Full Name:</label>
            <input type="text" id="fullName" name="fullName" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required>

            <label for="program">Program of Study:</label>
            <select id="program" name="program" required>
                <option value="">Select a program</option>
                <option value="Computer Science">Computer Science</option>
                <option value="Electrical Engineering">Electrical Engineering</option>
                <option value="Mechanical Engineering">Mechanical Engineering</option>
                <option value="Civil Engineering">Civil Engineering</option>
            </select>

            <label for="dob">Date of Birth:</label>
            <input type="date" id="dob" name="dob" required>

            <button type="submit">Submit Application</button>
        </form>
        <div id="responseMessage"></div>
    </div>

    <script>
        /**
         * Handles the form submission.
         * @param {Event} event - The submit event.
         * @returns {boolean} - Returns false to prevent default form submission.
         */
        function handleSubmit(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = {
                fullName: document.getElementById('fullName').value,
                email: document.getElementById('email').value,
                phone: document.getElementById('phone').value,
                program: document.getElementById('program').value,
                dob: document.getElementById('dob').value
            };

            // Validate form data
            if (!validateFormData(formData)) {
                displayMessage('Please fill in all fields correctly.', 'error');
                return false;
            }

            // Simulate form submission (e.g., to a server)
            console.log('Form submitted successfully:', formData);
            displayMessage('Application submitted successfully!', 'success');

            // Reset the form
            document.getElementById('admissionForm').reset();
            return false; // Prevent default form submission
        }

        /**
         * Validates the form data.
         * @param {Object} data - The form data to validate.
         * @returns {boolean} - Returns true if valid, false otherwise.
         */
        function validateFormData(data) {
            // Basic validation: check if all fields are filled
            return Object.values(data).every(value => value.trim() !== '');
        }

        /**
         * Displays a message to the user.
         * @param {string} message - The message to display.
         * @param {string} type - The type of message ('success' or 'error').
         */
        function displayMessage(message, type) {
            const responseMessage = document.getElementById('responseMessage');
            responseMessage.textContent = message;
            responseMessage.className = type; // Set class for styling
        }
    </script>
    <style>
        /* Basic styles for the form */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
        }
        label {
            display: block;
            margin: 10px 0 5px;
        }
        input, select, button {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #28a745;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        #responseMessage {
            text-align: center;
            margin-top: 20px;
        }
        .success {
            color: green;
        }
        .error {
            color: red;
        }
    </style>
</body>
</html>
```
