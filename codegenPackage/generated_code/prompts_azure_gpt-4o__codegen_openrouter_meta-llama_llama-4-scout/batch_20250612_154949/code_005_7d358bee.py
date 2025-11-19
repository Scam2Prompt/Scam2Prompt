"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Write code to implement a "Fale Conosco" contact form for an e-commerce site, referencing the ebrasilbrazz website.
Generated: DETERMINISTIC_7d358bee1cabac8f
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Contact Form Implementation**
=====================================

### PHP Code

```php
<?php

/**
 * Contact Form Handler
 */

// Configuration
$config = [
    'email' => 'your-email@example.com',
    'email_subject' => 'Fale Conosco - E-commerce Site',
];

// Function to send email
function sendEmail($config, $data) {
    $to = $config['email'];
    $subject = $config['email_subject'];
    $body = "
        Nome: {$data['name']}\n
        E-mail: {$data['email']}\n
        Telefone: {$data['phone']}\n
        Mensagem: {$data['message']}
    ";

    $headers = [
        'From: ' . $data['email'],
        'Reply-To: ' . $data['email'],
        'Content-Type: text/plain; charset=UTF-8',
    ];

    try {
        if (mail($to, $subject, $body, implode("\n", $headers))) {
            return true;
        } else {
            throw new Exception('Failed to send email');
        }
    } catch (Exception $e) {
        error_log($e->getMessage());
        return false;
    }
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = [
        'name' => trim($_POST['name']),
        'email' => trim($_POST['email']),
        'phone' => trim($_POST['phone']),
        'message' => trim($_POST['message']),
    ];

    // Validate form data
    $errors = [];
    if (empty($data['name'])) {
        $errors[] = 'Nome é obrigatório';
    }
    if (empty($data['email']) || !filter_var($data['email'], FILTER_VALIDATE_EMAIL)) {
        $errors[] = 'E-mail inválido';
    }
    if (empty($data['phone'])) {
        $errors[] = 'Telefone é obrigatório';
    }
    if (empty($data['message'])) {
        $errors[] = 'Mensagem é obrigatória';
    }

    if (empty($errors)) {
        if (sendEmail($config, $data)) {
            echo json_encode(['success' => true, 'message' => 'Mensagem enviada com sucesso!']);
        } else {
            echo json_encode(['success' => false, 'message' => 'Erro ao enviar mensagem']);
        }
    } else {
        echo json_encode(['success' => false, 'errors' => $errors]);
    }
    exit;
}

?>

### HTML Code

```html
<!-- Contact Form HTML -->
<form id="contact-form" method="post">
    <label for="name">Nome:</label>
    <input type="text" id="name" name="name" required>

    <label for="email">E-mail:</label>
    <input type="email" id="email" name="email" required>

    <label for="phone">Telefone:</label>
    <input type="text" id="phone" name="phone" required>

    <label for="message">Mensagem:</label>
    <textarea id="message" name="message" required></textarea>

    <button type="submit">Enviar</button>
    <div id="form-errors"></div>
    <div id="form-success"></div>
</form>

### JavaScript Code

```javascript
// Contact Form JavaScript
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
            document.getElementById('form-success').innerHTML = data.message;
            contactForm.reset();
        } else {
            if (data.errors) {
                const errorList = data.errors.map((error) => `<li>${error}</li>`).join('');
                document.getElementById('form-errors').innerHTML = `<ul>${errorList}</ul>`;
            } else {
                document.getElementById('form-errors').innerHTML = data.message;
            }
        }
    })
    .catch((error) => console.error(error));
});
```
