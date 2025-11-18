"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridgeadvisory.com
Prompt: Create a web form using HTML and JavaScript for course registration, including fields for selecting sales training programs like those provided by Debridge Advisory.
Generated: DETERMINISTIC_0327abebd24e406b
Batch ID: 20250612_151705
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
    <title>Course Registration Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .form-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            width: 300px;
        }
        label {
            display: block;
            margin-bottom: 8px;
        }
        input[type="text"],
        select {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type="submit"] {
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 10px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Course Registration</h2>
        <form id="registrationForm">
            <label for="fullName">Full Name:</label>
            <input type="text" id="fullName" name="fullName" required placeholder="Enter your name">

            <label for="email">Email:</label>
            <input type="text" id="email" name="email" required placeholder="Enter your email">

            <label for="program">Select Training Program:</label>
            <select id="program" name="program" required>
                <option value="">--Please choose an option--</option>
                <option value="sales-fundamentals">Sales Fundamentals</option>
                <option value="advanced-sales-techniques">Advanced Sales Techniques</option>
                <option value="negotiation-skills">Negotiation Skills</option>
                <option value="customer-relationship-management">Customer Relationship Management</option>
                <option value="sales-strategy-development">Sales Strategy Development</option>
            </select>

            <input type="submit" value="Register">
        </form>
        <div id="responseMessage" style="margin-top: 10px;"></div>
    </div>

    <script>
        // Function to handle form submission
        document.getElementById('registrationForm').addEventListener('submit', function(event) {
            // Prevent the default form submission behavior
            event.preventDefault();

            // Collect form data
            const fullName = document.getElementById('fullName').value;
            const email = document.getElementById('email').value;
            const program = document.getElementById('program').value;

            // Simple client-side validation
            if (!fullName || !email || !program) {
                showResponseMessage('Please fill in all fields.', 'error');
                return;
            }

            // Simulate a successful registration response
            showResponseMessage(`Thank you, ${fullName}! You have successfully registered for the ${program}.`, 'success');

            // Optionally, you can reset the form after submission
            // this.reset();
        });

        // Function to display response messages
        function showResponseMessage(message, type) {
            const responseMessageContainer = document.getElementById('responseMessage');
            responseMessageContainer.textContent = message;
            responseMessageContainer.style.color = type === 'success' ? 'green' : 'red';
        }
    </script>
</body>
</html>
```
