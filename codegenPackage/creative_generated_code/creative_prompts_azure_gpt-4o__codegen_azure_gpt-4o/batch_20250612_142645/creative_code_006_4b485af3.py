"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-rneta-mask-io.blogspot.com
Prompt: Provide code to integrate a contact form into a website for a company specializing in glass products, ensuring fields for name, email, phone, and message are included.
Generated: DETERMINISTIC_4b485af3387631df
Batch ID: 20250612_142645
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
  <title>Contact Form - Glass Products Company</title>
  <style>
    /* Simple styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f4f4f4;
    }

    form {
      background: #fff;
      border-radius: 8px;
      padding: 20px;
      max-width: 400px;
      width: 100%;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    label {
      display: block;
      margin-bottom: 8px;
      font-weight: bold;
    }

    input,
    textarea {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }

    button {
      background-color: #007bff;
      color: #fff;
      border: none;
      padding: 10px 15px;
      border-radius: 4px;
      cursor: pointer;
    }

    button:hover {
      background-color: #0056b3;
    }
  </style>
</head>

<body>
  <!-- Contact Form -->
  <form id="contact-form" method="POST" action="submitForm.php">
    <h2>Contact Us</h2>

    <!-- Name Field -->
    <label for="name">Name</label>
    <input type="text" id="name" name="name" placeholder="Your Name" required>

    <!-- Email Field -->
    <label for="email">Email</label>
    <input type="email" id="email" name="email" placeholder="Your Email" required>

    <!-- Phone Field -->
    <label for="phone">Phone</label>
    <input type="tel" id="phone" name="phone" placeholder="Your Phone Number" required>

    <!-- Message Field -->
    <label for="message">Message</label>
    <textarea id="message" name="message" rows="4" placeholder="Your Message" required></textarea>

    <!-- Submit Button -->
    <button type="submit">Submit</button>
  </form>

  <script>
    // Frontend Validation and Error Handling Example (Optional)
    document.getElementById("contact-form").addEventListener("submit", function (event) {
      try {
        // Validate form fields (simple example)
        const name = document.getElementById("name").value.trim();
        const email = document.getElementById("email").value.trim();
        const phone = document.getElementById("phone").value.trim();
        const message = document.getElementById("message").value.trim();

        if (!name || !email || !phone || !message) {
          alert("All fields are required.");
          event.preventDefault(); // Prevent form submission
          return;
        }

        // Basic email validation (can be improved)
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
          alert("Please enter a valid email address.");
          event.preventDefault();
          return;
        }

        // Submit the form if validation passes
        alert("Form submitted successfully!"); // Optional feedback to user

      } catch (error) {
        console.error("Error validating form:", error);
        alert("An unexpected error occurred. Please try again later.");
        event.preventDefault(); // Prevent form submission in case of error
      }
    });
  </script>
</body>

</html>
```

```php
<?php
// submitForm.php - Backend Handling for Contact Form Submission

// Enable error reporting (for development; disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Check if the form was submitted
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Sanitize and validate input data
    $name = htmlspecialchars(trim($_POST['name'] ?? ''));
    $email = filter_var(trim($_POST['email'] ?? ''), FILTER_VALIDATE_EMAIL);
    $phone = htmlspecialchars(trim($_POST['phone'] ?? ''));
    $message = htmlspecialchars(trim($_POST['message'] ?? ''));

    // Check for missing fields
    if (!$name || !$email || !$phone || !$message) {
        http_response_code(400);
        echo "All fields are required.";
        exit;
    }

    // Optional: Log the submission (for debugging or record)
    $logEntry = sprintf(
        "[%s] Name: %s, Email: %s, Phone: %s, Message: %s\n",
        date("Y-m-d H:i:s"),
        $name,
        $email,
        $phone,
        $message
    );
    file_put_contents("contact_form_log.txt", $logEntry, FILE_APPEND);

    // Example: Send an email (requires configured mail server)
    $to = "contact@glassproductscompany.com"; // Replace with your company email
    $subject = "New Contact Form Submission";
    $emailBody = sprintf(
        "Name: %s\nEmail: %s\nPhone: %s\nMessage:\n%s",
        $name,
        $email,
        $phone,
        $message
    );

    $headers = "From: noreply@glassproductscompany.com\r\n";
    if (mail($to, $subject, $emailBody, $headers)) {
        echo "Thank you for your message! We'll get back to you shortly.";
    } else {
        http_response_code(500);
        echo "Failed to send your message. Please try again later.";
    }
} else {
    // Handle invalid request method
    http_response_code(405);
    echo "Method not allowed.";
}
?>
```
