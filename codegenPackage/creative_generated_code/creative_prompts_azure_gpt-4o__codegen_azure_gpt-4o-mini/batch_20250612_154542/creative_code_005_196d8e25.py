"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egatur.edu.pe
Prompt: Develop a PHP script to handle inquiries submitted via Egatur's contact form, including fields for "Motivo de la consulta" and "Carreras y/o Especialidades."
Generated: DETERMINISTIC_196d8e2518de0b1f
Batch ID: 20250612_154542
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
 * contact_form_handler.php
 *
 * This script handles inquiries submitted via Egatur's contact form,
 * processing the "Motivo de la consulta" and "Carreras y/o Especialidades" fields.
 * It validates input, sends an email, and provides appropriate error handling.
 */

// Define constants for email settings
define('TO_EMAIL', 'contact@egatur.com'); // Change to your contact email
define('SUBJECT', 'New Inquiry from Contact Form');

// Function to send email
function sendEmail($motivo, $especialidades) {
    // Construct the message body
    $message = "Motivo de la consulta: " . htmlspecialchars($motivo) . "\n";
    $message .= "Carreras y/o Especialidades: " . htmlspecialchars($especialidades) . "\n";

    // Send email
    if (!mail(TO_EMAIL, SUBJECT, $message)) {
        throw new Exception('Unable to send email. Please try again later.');
    }
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate input
    $motivo = isset($_POST['motivo']) ? trim($_POST['motivo']) : '';
    $especialidades = isset($_POST['especialidades']) ? trim($_POST['especialidades']) : '';

    // Basic validation
    if (empty($motivo) || empty($especialidades)) {
        http_response_code(400); // Bad Request
        echo json_encode(['error' => 'Both fields are required.']);
        exit;
    }

    try {
        // Send the email
        sendEmail($motivo, $especialidades);
        
        // Respond with a success message
        http_response_code(200);
        echo json_encode(['success' => 'Inquiry submitted successfully.']);
    } catch (Exception $e) {
        // Log the error (should be logged in production environment)
        error_log($e->getMessage());
        
        // Respond with an error message
        http_response_code(500); // Internal Server Error
        echo json_encode(['error' => 'An error occurred. Please try again later.']);
    }
} else {
    // Method Not Allowed
    http_response_code(405);
    echo json_encode(['error' => 'Method not allowed.']);
}
?>
```
