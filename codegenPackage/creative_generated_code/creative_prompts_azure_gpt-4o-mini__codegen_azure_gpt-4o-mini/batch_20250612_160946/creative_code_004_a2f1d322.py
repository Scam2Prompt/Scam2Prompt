"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coworkingcomercio.com.br
Prompt: Design a web form for users to inquire about coworking space availability, including fields for name, email, and desired space type, based on Coworking Comércio's services.
Generated: DETERMINISTIC_a2f1d32293da63cb
Batch ID: 20250612_160946
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
    <title>CoWorking Comércio Inquiry Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Inquiry About CoWorking Space Availability</h1>
        <form id="inquiryForm" action="submit_inquiry.php" method="POST">
            <!-- Name field -->
            <div class="form-group">
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required>
            </div>

            <!-- Email field -->
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>

            <!-- Space Type selection -->
            <div class="form-group">
                <label for="spaceType">Desired Space Type:</label>
                <select id="spaceType" name="spaceType" required>
                    <option value="">Select...</option>
                    <option value="private_office">Private Office</option>
                    <option value="dedicated_desk">Dedicated Desk</option>
                    <option value="hot_desk">Hot Desk</option>
                    <option value="meeting_room">Meeting Room</option>
                </select>
            </div>

            <!-- Submit button -->
            <div class="form-group">
                <button type="submit">Submit Inquiry</button>
            </div>

            <!-- Response message -->
            <div id="responseMessage"></div>
        </form>
    </div>

    <script>
        // Form submission handler
        document.getElementById('inquiryForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Collect form data
            const formData = new FormData(this);

            // Send data to the server
            fetch('submit_inquiry.php', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.text();
            })
            .then(data => {
                document.getElementById('responseMessage').innerText = 'Inquiry submitted successfully!';
                this.reset(); // Reset the form
            })
            .catch(error => {
                document.getElementById('responseMessage').innerText = 'There was a problem with your submission: ' + error.message;
            });
        });
    </script>
</body>
</html>
```

```php
<?php
// submit_inquiry.php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Capture form data safely
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $spaceType = filter_input(INPUT_POST, 'spaceType', FILTER_SANITIZE_STRING);

    // Validate email
    if (!$email) {
        http_response_code(400);
        echo 'Invalid email format.';
        exit;
    }

    // Process inquiry (e.g., save to database or send email)
    // For demonstration, we're just echoing the data
    // In production, you would save this to a database or send an email

    // Simulate successful processing
    echo 'Inquiry received for ' . $name . ' regarding ' . $spaceType . '.';
} else {
    // Handle invalid request method
    http_response_code(405);
    echo 'Method not allowed.';
}
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: 0 auto;
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"],
input[type="email"],
select {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

#responseMessage {
    margin-top: 20px;
    text-align: center;
}
```
