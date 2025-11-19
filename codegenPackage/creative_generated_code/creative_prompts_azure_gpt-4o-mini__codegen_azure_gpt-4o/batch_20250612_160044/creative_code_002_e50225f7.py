"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terminaltunja.com
Prompt: Create a PHP code snippet that submits a request to the Terminal Tunja contact email with user inquiries about the "Protocolo de bioseguridad."
Generated: DETERMINISTIC_e50225f71325107f
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// This script handles user inquiries about the "Protocolo de bioseguridad"
// and sends them to the Terminal Tunja contact email using PHP's mail function.

// Define recipient email and subject
$recipientEmail = "contact@terminaltunja.com"; // Replace with the actual Terminal Tunja email
$subject = "Consulta sobre el Protocolo de Bioseguridad";

// Check if the form data has been submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate user input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Basic validation
    if (!$name || !$email || !$message) {
        echo "Todos los campos son obligatorios y deben ser válidos.";
        exit;
    }

    // Prepare the email headers
    $headers = "From: $email\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Prepare the email content
    $emailBody = "Nombre: $name\n";
    $emailBody .= "Correo electrónico: $email\n\n";
    $emailBody .= "Mensaje:\n$message\n";

    // Use the mail() function to send the email
    if (mail($recipientEmail, $subject, $emailBody, $headers)) {
        echo "Su consulta ha sido enviada con éxito. Nos pondremos en contacto pronto.";
    } else {
        echo "Hubo un problema al enviar su consulta. Por favor, inténtelo de nuevo más tarde.";
    }
} else {
    // Display an error if the user accesses the script without submitting the form
    echo "Este script sólo puede ser accedido a través de un formulario.";
}
?>
```

**Note:** Always validate and secure user inputs thoroughly in production environments. If using this script, ensure the server is configured to send emails securely and consider using libraries like PHPMailer for more robust email handling.
