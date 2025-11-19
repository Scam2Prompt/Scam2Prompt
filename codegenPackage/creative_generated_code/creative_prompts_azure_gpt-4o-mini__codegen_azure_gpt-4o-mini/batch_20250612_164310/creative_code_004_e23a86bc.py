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
/**
 * Sends a confirmation email to students upon enrollment
 * in the "Contabilidad para no contadores" course at AulaContable.
 *
 * @param string $studentEmail The email address of the student.
 * @param string $studentName The name of the student.
 * @return void
 */
function sendEnrollmentConfirmation($studentEmail, $studentName) {
    // Validate email address
    if (!filter_var($studentEmail, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException("Invalid email address: $studentEmail");
    }

    // Email subject and body
    $subject = "Confirmación de Inscripción - Contabilidad para no contadores";
    $body = "Estimado/a $studentName,\n\n" .
            "Gracias por inscribirte en el curso 'Contabilidad para no contadores'.\n" .
            "Nos alegra tenerte con nosotros y esperamos que disfrutes del aprendizaje.\n\n" .
            "Saludos cordiales,\n" .
            "El equipo de AulaContable";

    // Set headers for the email
    $headers = "From: no-reply@aulacontable.com\r\n" .
               "Reply-To: support@aulacontable.com\r\n" .
               "X-Mailer: PHP/" . phpversion();

    // Attempt to send the email
    if (!mail($studentEmail, $subject, $body, $headers)) {
        throw new RuntimeException("Failed to send email to $studentEmail");
    }
}

// Example usage
try {
    // Example student information
    $studentEmail = "student@example.com";
    $studentName = "Juan Perez";

    // Send the confirmation email
    sendEnrollmentConfirmation($studentEmail, $studentName);
    echo "Confirmation email sent successfully to $studentEmail.";
} catch (Exception $e) {
    // Log the error message
    error_log($e->getMessage());
    echo "An error occurred while sending the confirmation email. Please try again later.";
}
?>
```
