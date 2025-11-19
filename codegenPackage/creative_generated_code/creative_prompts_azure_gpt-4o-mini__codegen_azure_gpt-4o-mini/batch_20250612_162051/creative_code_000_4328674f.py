"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renovation-toiture-toulouse.com
Prompt: Generate a code snippet for a web form that allows users to request a free roofing estimate from a company specializing in roof renovation and repair in Toulouse.
Generated: DETERMINISTIC_4328674f3fbc2744
Batch ID: 20250612_162051
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
    <title>Free Roofing Estimate Request</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Request a Free Roofing Estimate</h1>
        <form id="estimate-form" action="submit_estimate.php" method="POST" novalidate>
            <div class="form-group">
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email Address:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required>
            </div>
            <div class="form-group">
                <label for="address">Property Address:</label>
                <input type="text" id="address" name="address" required>
            </div>
            <div class="form-group">
                <label for="details">Additional Details:</label>
                <textarea id="details" name="details" rows="4"></textarea>
            </div>
            <button type="submit">Request Estimate</button>
        </form>
        <div id="response-message" class="hidden"></div> <!-- Placeholder for response messages -->
    </div>

    <script>
        document.getElementById('estimate-form').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent form submission for validation
            
            // Validate form inputs
            let isValid = true;
            const inputs = this.querySelectorAll('input, textarea');
            inputs.forEach(input => {
                if (!input.checkValidity()) {
                    isValid = false;
                    input.classList.add('invalid'); // Highlight invalid fields
                } else {
                    input.classList.remove('invalid');
                }
            });

            if (isValid) {
                this.submit(); // Submit the form if valid
            } else {
                document.getElementById('response-message').innerText = "Please fill all required fields correctly.";
                document.getElementById('response-message').classList.remove('hidden');
            }
        });
    </script>
</body>
</html>
```

```php
<?php
// submit_estimate.php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Capture form data
    $name = htmlspecialchars(trim($_POST['name']));
    $email = htmlspecialchars(trim($_POST['email']));
    $phone = htmlspecialchars(trim($_POST['phone']));
    $address = htmlspecialchars(trim($_POST['address']));
    $details = htmlspecialchars(trim($_POST['details']));

    // Basic validation
    if (empty($name) || empty($email) || empty($phone) || empty($address)) {
        die('Please fill in all required fields.');
    }

    // Prepare to send email (replace with your email)
    $to = 'info@roofingcompany.com';
    $subject = 'New Roofing Estimate Request';
    $message = "Name: $name\nEmail: $email\nPhone: $phone\nAddress: $address\nDetails: $details";
    $headers = "From: $email";

    // Send email and check for success
    if (mail($to, $subject, $message, $headers)) {
        echo 'Thank you for your request! We will get back to you soon.';
    } else {
        echo 'There was a problem sending your request. Please try again later.';
    }
} else {
    // Handle incorrect request method
    http_response_code(405);
    echo 'Method Not Allowed';
}
?>
```
