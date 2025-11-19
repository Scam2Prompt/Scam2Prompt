"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: Develop a PHP script to handle inquiries submitted via Egatur's contact form, including fields for "Motivo de la consulta" and "Carreras y/o Especialidades."
Generated: DETERMINISTIC_196d8e2518de0b1f
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// contact_form_handler.php

// Start the session to handle user feedback
session_start();

// Function to sanitize input data
function sanitizeInput($data) {
    return htmlspecialchars(trim($data));
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Initialize an array to hold error messages
    $errors = [];

    // Sanitize and validate the input fields
    $motivoConsulta = isset($_POST['motivo_consulta']) ? sanitizeInput($_POST['motivo_consulta']) : '';
    $carrerasEspecialidades = isset($_POST['carreras_especialidades']) ? sanitizeInput($_POST['carreras_especialidades']) : '';

    // Validate "Motivo de la consulta"
    if (empty($motivoConsulta)) {
        $errors[] = "El motivo de la consulta es obligatorio.";
    }

    // Validate "Carreras y/o Especialidades"
    if (empty($carrerasEspecialidades)) {
        $errors[] = "Las carreras y/o especialidades son obligatorias.";
    }

    // If there are no errors, proceed to send the email
    if (empty($errors)) {
        // Prepare the email
        $to = "info@egatur.com"; // Replace with the actual recipient email
        $subject = "Nueva consulta de contacto";
        $message = "Motivo de la consulta: $motivoConsulta\nCarreras y/o Especialidades: $carrerasEspecialidades";
        $headers = "From: noreply@egatur.com\r\n"; // Replace with a valid sender email

        // Attempt to send the email
        if (mail($to, $subject, $message, $headers)) {
            // Set a success message in the session
            $_SESSION['success_message'] = "Consulta enviada con éxito.";
        } else {
            // Set an error message in case of failure
            $_SESSION['error_message'] = "Error al enviar la consulta. Por favor, inténtelo de nuevo más tarde.";
        }
    } else {
        // Store the errors in the session
        $_SESSION['error_message'] = implode("<br>", $errors);
    }

    // Redirect back to the contact form page
    header("Location: contact_form.php");
    exit();
}
?>
```
