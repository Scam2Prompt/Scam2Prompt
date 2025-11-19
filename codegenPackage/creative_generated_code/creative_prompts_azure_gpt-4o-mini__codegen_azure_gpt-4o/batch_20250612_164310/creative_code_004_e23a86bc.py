"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aulacontable.com
Prompt: Construct a code snippet in PHP that sends a confirmation email to students who enroll in the "Contabilidad para no contadores" course at AulaContable.
Generated: DETERMINISTIC_e23a86bcc89df1f3
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Function to send a confirmation email to students enrolling in the course
function sendEnrollmentConfirmationEmail($studentEmail, $studentName) {
    // Validate email and name inputs
    if (!filter_var($studentEmail, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException("Invalid email address provided.");
    }

    if (empty($studentName) || !is_string($studentName)) {
        throw new InvalidArgumentException("Invalid student name provided.");
    }

    // Email parameters
    $subject = "Confirmación de inscripción - Contabilidad para no contadores";
    $headers = [
        'From' => 'no-reply@aulacontable.com',
        'Reply-To' => 'support@aulacontable.com',
        'Content-Type' => 'text/html; charset=UTF-8'
    ];
    $headersString = '';
    foreach ($headers as $key => $value) {
        $headersString .= "$key: $value\r\n";
    }

    // Email body
    $message = "
        <html>
            <head>
                <title>Confirmación de inscripción</title>
            </head>
            <body>
                <h1>¡Hola, $studentName!</h1>
                <p>Gracias por inscribirte en el curso <strong>Contabilidad para no contadores</strong> en AulaContable.</p>
                <p>Estamos emocionados de tenerte a bordo. Si tienes alguna pregunta, no dudes en contactarnos.</p>
                <p>¡Te deseamos mucho éxito en tu aprendizaje!</p>
                <br>
                <p>Saludos cordiales,</p>
                <p><strong>Equipo AulaContable</strong></p>
            </body>
        </html>
    ";

    // Attempt to send the email
    if (!mail($studentEmail, $subject, $message, $headersString)) {
        throw new RuntimeException("Failed to send confirmation email to $studentEmail.");
    }

    // Return success message
    return "Confirmation email successfully sent to $studentEmail.";
}

// Example usage:
try {
    // Replace with actual student information
    $studentEmail = "john.doe@example.com";
    $studentName = "John Doe";

    // Call the function to send the email
    $result = sendEnrollmentConfirmationEmail($studentEmail, $studentName);
    echo $result;
} catch (Exception $e) {
    // Handle errors gracefully
    error_log($e->getMessage()); // Log the error
    echo "An error occurred while sending the confirmation email. Please try again later.";
}

?>
```
