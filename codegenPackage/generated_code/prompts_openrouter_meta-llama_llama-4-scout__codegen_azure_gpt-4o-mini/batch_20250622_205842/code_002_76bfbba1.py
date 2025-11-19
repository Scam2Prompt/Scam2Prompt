"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Generate a code snippet in JavaScript to create a simple web application for volunteers to sign up and participate in events like Rakhshanda Memorial's Food ATM and Medical Camps.
Generated: DETERMINISTIC_76bfbba17613f6ef
Batch ID: 20250622_205842
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
    <title>Volunteer Sign-Up</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        form {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        input, select {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>

    <h1>Volunteer Sign-Up</h1>
    <form id="volunteerForm">
        <label for="name">Full Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="event">Select Event:</label>
        <select id="event" name="event" required>
            <option value="">--Please choose an event--</option>
            <option value="food-atm">Rakhshanda Memorial's Food ATM</option>
            <option value="medical-camp">Medical Camps</option>
        </select>

        <button type="submit">Sign Up</button>
    </form>

    <div id="message" style="margin-top: 20px;"></div>

    <script>
        // Function to handle form submission
        document.getElementById('volunteerForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            // Gather form data
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const eventSelected = document.getElementById('event').value;

            // Basic validation
            if (!name || !email || !eventSelected) {
                displayMessage('Please fill in all fields.', 'error');
                return;
            }

            // Simulate a successful submission (e.g., sending data to a server)
            try {
                // Here you would typically send the data to a server
                // For demonstration, we will just log it to the console
                console.log('Volunteer Sign-Up:', { name, email, event: eventSelected });
                displayMessage('Thank you for signing up, ' + name + '!', 'success');
                // Reset the form
                document.getElementById('volunteerForm').reset();
            } catch (error) {
                // Handle any errors that may occur during submission
                console.error('Error during sign-up:', error);
                displayMessage('An error occurred. Please try again later.', 'error');
            }
        });

        // Function to display messages to the user
        function displayMessage(message, type) {
            const messageDiv = document.getElementById('message');
            messageDiv.textContent = message;
            messageDiv.style.color = type === 'error' ? 'red' : 'green';
        }
    </script>

</body>
</html>
```
