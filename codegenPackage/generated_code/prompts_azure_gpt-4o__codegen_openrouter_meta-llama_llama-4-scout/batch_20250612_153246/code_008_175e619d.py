"""
Generated Code Metadata:
========================
Original URL: https://henfruit.ro
Prompt: Develop a PHP-based contact form for a web design agency, including fields for "Nume," "Email sau telefon," and a "Trimite" button, as seen on Henfruit's webpage.
Generated: DETERMINISTIC_175e619dfb5be81c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Contact Form Handler
 */

// Configuration
$config = [
    'to_email' => 'your_email@example.com', // Replace with your email
    'from_email' => 'your_email@example.com', // Replace with your email
    'subject' => 'Contact Form Submission',
];

// Function to send email
function sendEmail($config, $data) {
    $headers = [
        'From: ' . $config['from_email'],
        'Reply-To: ' . $data['email'],
        'Content-Type: text/plain; charset=UTF-8',
    ];

    $message = "Nume: " . $data['name'] . "\n";
    $message .= "Email sau telefon: " . $data['email_or_phone'] . "\n";

    $subject = $config['subject'];

    wp_mail($config['to_email'], $subject, $message, $headers);
}

// Check if form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Validate input
        $errors = [];
        $name = trim($_POST['name']);
        $email_or_phone = trim($_POST['email_or_phone']);

        if (empty($name)) {
            $errors[] = 'Nume este obligatoriu';
        }

        if (empty($email_or_phone)) {
            $errors[] = 'Email sau telefon este obligatoriu';
        }

        if (!empty($errors)) {
            $response = [
                'success' => false,
                'errors' => $errors,
            ];
        } else {
            // Send email
            $data = [
                'name' => $name,
                'email_or_phone' => $email_or_phone,
            ];

            sendEmail($config, $data);

            $response = [
                'success' => true,
                'message' => 'Mesajul dvs. a fost trimis cu succes!',
            ];
        }

        // Output JSON response
        header('Content-Type: application/json');
        echo json_encode($response);
        exit;
    } catch (Exception $e) {
        // Log error
        error_log($e->getMessage());

        $response = [
            'success' => false,
            'errors' => ['Eroare internă'],
        ];

        header('Content-Type: application/json');
        echo json_encode($response);
        exit;
    }
}
?>

<!-- Contact Form HTML -->
<form id="contact-form" method="post">
    <label for="name">Nume:</label>
    <input type="text" id="name" name="name" required>

    <label for="email_or_phone">Email sau telefon:</label>
    <input type="text" id="email_or_phone" name="email_or_phone" required>

    <button type="submit" id="trimite">Trimite</button>
    <div id="form-errors"></div>
    <div id="form-success"></div>
</form>

<!-- JavaScript for form submission -->
<script>
    const contactForm = document.getElementById('contact-form');

    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const formData = new FormData(contactForm);

        fetch('', {
            method: 'POST',
            body: formData,
        })
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                document.getElementById('form-success').innerText = data.message;
                contactForm.reset();
            } else {
                const errorsHtml = data.errors.map((error) => `<div>${error}</div>`).join('');
                document.getElementById('form-errors').innerHTML = errorsHtml;
            }
        })
        .catch((error) => console.error(error));
    });
</script>
```
