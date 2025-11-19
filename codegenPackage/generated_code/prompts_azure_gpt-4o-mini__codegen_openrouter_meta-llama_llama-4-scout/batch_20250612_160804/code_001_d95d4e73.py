"""
Generated Code Metadata:
========================
Original URL: https://www.hdadpanaderos.es
Prompt: How can I implement a contact form for a religious organization like the one found on the Hermandad de los Panaderos site, ensuring it includes fields for inquiries and feedback?
Generated: DETERMINISTIC_d95d4e73ad466e69
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

// Configuration for the contact form
$config = [
    'admin_email' => 'your-admin-email@example.com',
    'sender_email' => 'your-sender-email@example.com',
    'email_subject' => 'Inquiry from Hermandad de los Panaderos Contact Form',
];

// Contact form handler class
class ContactFormHandler
{
    private $config;

    public function __construct($config)
    {
        $this->config = $config;
    }

    // Validate form data
    private function validateFormData($data)
    {
        $errors = [];

        if (empty($data['name'])) {
            $errors[] = 'Name is required';
        }

        if (empty($data['email'])) {
            $errors[] = 'Email is required';
        } elseif (!filter_var($data['email'], FILTER_VALIDATE_EMAIL)) {
            $errors[] = 'Invalid email address';
        }

        if (empty($data['message'])) {
            $errors[] = 'Message is required';
        }

        return $errors;
    }

    // Send email using PHPMailer
    private function sendEmail($data)
    {
        try {
            $mail = new PHPMailer(true);

            $mail->isSMTP();
            $mail->Host = 'your-smtp-host';
            $mail->SMTPAuth = true;
            $mail->Username = $this->config['sender_email'];
            $mail->Password = 'your-smtp-password';
            $mail->SMTPSecure = 'tls';
            $mail->Port = 587;

            $mail->setFrom($this->config['sender_email'], $data['name']);
            $mail->addAddress($this->config['admin_email']);

            $mail->isHTML(true);

            $mail->Subject = $this->config['email_subject'];
            $mail->Body    = "Name: {$data['name']}<br>Email: {$data['email']}<br>Message: {$data['message']}";
            $mail->AltBody = "Name: {$data['name']}\nEmail: {$data['email']}\nMessage: {$data['message']}";

            $mail->send();

            return true;
        } catch (Exception $e) {
            error_log($e->getMessage());
            return false;
        }
    }

    // Handle form submission
    public function handleFormSubmission($data)
    {
        $errors = $this->validateFormData($data);

        if (!empty($errors)) {
            return ['success' => false, 'errors' => $errors];
        }

        if ($this->sendEmail($data)) {
            return ['success' => true, 'message' => 'Message sent successfully'];
        } else {
            return ['success' => false, 'errors' => ['Failed to send message']];
        }
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $contactFormHandler = new ContactFormHandler($config);

    $data = [
        'name' => $_POST['name'],
        'email' => $_POST['email'],
        'message' => $_POST['message'],
    ];

    $response = $contactFormHandler->handleFormSubmission($data);

    header('Content-Type: application/json');
    echo json_encode($response);
    exit;
}
```

```html
<!-- Contact form HTML -->
<form id="contact-form" method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>

    <label for="message">Message:</label>
    <textarea id="message" name="message" required></textarea>

    <button type="submit">Send Message</button>

    <div id="form-errors"></div>
    <div id="form-success"></div>
</form>

<script>
    const contactForm = document.getElementById('contact-form');

    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(contactForm);

        try {
            const response = await fetch('', {
                method: 'POST',
                body: formData,
            });

            const data = await response.json();

            if (data.success) {
                document.getElementById('form-success').innerText = data.message;
                contactForm.reset();
            } else {
                const errorList = document.getElementById('form-errors');
                errorList.innerHTML = '';

                data.errors.forEach((error) => {
                    const errorItem = document.createElement('li');
                    errorItem.innerText = error;
                    errorList.appendChild(errorItem);
                });
            }
        } catch (error) {
            console.error(error);
        }
    });
</script>
```
