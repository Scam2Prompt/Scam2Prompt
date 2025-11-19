"""
Generated Code Metadata:
========================
Original URL: https://www.gpt-chat.info
Prompt: Write a code snippet for a contact form that handles errors, inspired by the "Lỗi: Không tìm thấy biểu mẫu liên hệ" message on the GPT-Chat page.
Generated: DETERMINISTIC_59046b636abc2043
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready contact form implementation with error handling in JavaScript (for frontend) and PHP (for backend processing):

```html
<!-- contact_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <style>
        .error { color: red; }
        .success { color: green; }
        .hidden { display: none; }
    </style>
</head>
<body>
    <form id="contactForm" method="POST" action="process_contact.php">
        <div id="formErrors" class="error hidden"></div>
        <div id="formSuccess" class="success hidden">Thank you! Your message has been sent.</div>

        <div>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <span id="nameError" class="error hidden"></span>
        </div>

        <div>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <span id="emailError" class="error hidden"></span>
        </div>

        <div>
            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>
            <span id="messageError" class="error hidden"></span>
        </div>

        <button type="submit">Submit</button>
    </form>

    <script>
        document.getElementById('contactForm').addEventListener('submit', function(e) {
            e.preventDefault();
            clearErrors();
            
            // Validate form
            let isValid = true;
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();

            if (!name) {
                showError('nameError', 'Name is required');
                isValid = false;
            }

            if (!email) {
                showError('emailError', 'Email is required');
                isValid = false;
            } else if (!validateEmail(email)) {
                showError('emailError', 'Please enter a valid email');
                isValid = false;
            }

            if (!message) {
                showError('messageError', 'Message is required');
                isValid = false;
            }

            if (isValid) {
                submitForm();
            }
        });

        function showError(elementId, message) {
            const element = document.getElementById(elementId);
            element.textContent = message;
            element.classList.remove('hidden');
        }

        function clearErrors() {
            document.querySelectorAll('.error').forEach(el => {
                el.textContent = '';
                el.classList.add('hidden');
            });
            document.getElementById('formErrors').classList.add('hidden');
            document.getElementById('formSuccess').classList.add('hidden');
        }

        function validateEmail(email) {
            const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return re.test(email);
        }

        async function submitForm() {
            const form = document.getElementById('contactForm');
            const formData = new FormData(form);
            
            try {
                const response = await fetch(form.action, {
                    method: 'POST',
                    body: formData
                });

                const result = await response.json();
                
                if (result.success) {
                    document.getElementById('formSuccess').classList.remove('hidden');
                    form.reset();
                } else {
                    document.getElementById('formErrors').textContent = 
                        result.message || 'Error submitting form';
                    document.getElementById('formErrors').classList.remove('hidden');
                }
            } catch (error) {
                document.getElementById('formErrors').textContent = 
                    'Network error. Please try again.';
                document.getElementById('formErrors').classList.remove('hidden');
            }
        }
    </script>
</body>
</html>
```

```php
<?php
// process_contact.php
header('Content-Type: application/json');

// Validate request
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Method not allowed']);
    exit;
}

// Get and sanitize input
$name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
$email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
$message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

// Validate input
$errors = [];
if (empty($name)) {
    $errors[] = 'Name is required';
}

if (empty($email)) {
    $errors[] = 'Email is required';
} elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $errors[] = 'Invalid email format';
}

if (empty($message)) {
    $errors[] = 'Message is required';
}

if (!empty($errors)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'message' => implode(', ', $errors)]);
    exit;
}

try {
    // Process the form (e.g., send email, save to database)
    // Replace this with your actual processing logic
    $to = 'contact@example.com';
    $subject = 'New Contact Form Submission';
    $body = "Name: $name\nEmail: $email\nMessage: $message";
    $headers = "From: $email";
    
    // In production, use a proper mailer library
    $mailSent = mail($to, $subject, $body, $headers);
    
    if ($mailSent) {
        echo json_encode(['success' => true]);
    } else {
        throw new Exception('Failed to send email');
    }
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode([
        'success' => false, 
        'message' => 'An error occurred while processing your request'
    ]);
    error_log('Contact form error: ' . $e->getMessage());
}
```
