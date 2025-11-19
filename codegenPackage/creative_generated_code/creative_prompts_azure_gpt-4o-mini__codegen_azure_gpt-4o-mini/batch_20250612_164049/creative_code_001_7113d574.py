"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tubellaesteticaduepuntozero.it
Prompt: Write a code snippet for a contact form that collects user inquiries for a beauty center, inspired by the contact options available at TuBella Estetica 2.0.
Generated: DETERMINISTIC_7113d574d97af39a
Batch ID: 20250612_164049
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
    <title>Contact Us - Beauty Center</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="contact-container">
        <h1>Contact Us</h1>
        <form id="contactForm" action="submitForm.php" method="POST">
            <!-- User Name Input -->
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required placeholder="Your Name">
            
            <!-- User Email Input -->
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="Your Email Address">
            
            <!-- User Phone Input -->
            <label for="phone">Phone (Optional):</label>
            <input type="tel" id="phone" name="phone" placeholder="Your Phone Number">
            
            <!-- Inquiry Type Selection -->
            <label for="inquiryType">Inquiry Type:</label>
            <select id="inquiryType" name="inquiryType" required>
                <option value="">Select an option</option>
                <option value="appointment">Appointment Booking</option>
                <option value="services">Services Inquiry</option>
                <option value="feedback">Feedback</option>
                <option value="other">Other</option>
            </select>
            
            <!-- User Message Input -->
            <label for="message">Message:</label>
            <textarea id="message" name="message" required placeholder="Your Message" rows="5"></textarea>
            
            <!-- Submit Button -->
            <button type="submit">Send Inquiry</button>
        </form>
    </div>

    <script>
        // Form submission handling
        document.getElementById('contactForm').onsubmit = function(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = new FormData(this);

            // Send data to the server
            fetch('submitForm.php', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // Handle successful response (e.g., show a thank you message)
                alert('Your inquiry has been submitted successfully.');
                this.reset(); // Reset the form fields
            })
            .catch(error => {
                // Handle errors (e.g., show an error message)
                alert('There was a problem with your submission: ' + error.message);
            });
        };
    </script>
</body>
</html>
```

```php
<?php
// submitForm.php

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = filter_var(trim($_POST["name"]), FILTER_SANITIZE_STRING);
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $phone = filter_var(trim($_POST["phone"]), FILTER_SANITIZE_STRING);
    $inquiryType = filter_var(trim($_POST["inquiryType"]), FILTER_SANITIZE_STRING);
    $message = filter_var(trim($_POST["message"]), FILTER_SANITIZE_STRING);

    // Validate required fields
    if (empty($name) || empty($email) || empty($inquiryType) || empty($message)) {
        http_response_code(400); // Bad Request
        echo json_encode(["status" => "error", "message" => "Please fill all required fields."]);
        exit;
    }

    // Prepare email
    $to = "info@beautycenter.com"; // Change to your email address
    $subject = "New Inquiry from: $name";
    $body = "Name: $name\nEmail: $email\nPhone: $phone\nInquiry Type: $inquiryType\nMessage: $message";
    $headers = "From: $email";

    // Send the email
    if (mail($to, $subject, $body, $headers)) {
        echo json_encode(["status" => "success", "message" => "Inquiry sent successfully."]);
    } else {
        http_response_code(500); // Internal Server Error
        echo json_encode(["status" => "error", "message" => "There was a problem sending your inquiry."]);
    }
} else {
    http_response_code(405); // Method Not Allowed
    echo json_encode(["status" => "error", "message" => "Invalid request method."]);
}
?>
```
