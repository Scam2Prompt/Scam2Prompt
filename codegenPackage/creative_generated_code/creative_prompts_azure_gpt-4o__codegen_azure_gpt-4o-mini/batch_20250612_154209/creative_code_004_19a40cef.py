"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isiv.edu.ar
Prompt: Write a PHP script to send automated email notifications to prospective students about ISIV's open enrollment for 2025, referencing specific programs like "Administración de Empresas" and "Análisis de Sistemas."
Generated: DETERMINISTIC_19a40cef23b06dc3
Batch ID: 20250612_154209
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
 * Sends automated email notifications to prospective students 
 * about ISIV's open enrollment for 2025.
 * 
 * This script targets specific programs: 
 * "Administración de Empresas" and "Análisis de Sistemas".
 */

// Configuration for email
define('SMTP_HOST', 'smtp.example.com'); // Replace with your SMTP server
define('SMTP_PORT', 587); // Replace with your SMTP port
define('SMTP_USER', 'your-email@example.com'); // Replace with your email
define('SMTP_PASS', 'your-email-password'); // Replace with your email password

/**
 * Sends an email notification to a prospective student.
 *
 * @param string $to The recipient's email address.
 * @param string $name The recipient's name.
 * @param string $program The program the email is about.
 * @return bool True on success, false on failure.
 */
function sendEmailNotification($to, $name, $program) {
    // Create the email subject and body
    $subject = 'Open Enrollment for 2025 at ISIV';
    $body = "Dear $name,\n\n" .
            "We are excited to announce that enrollment is now open for the year 2025! " .
            "We invite you to apply to our esteemed program: $program.\n\n" .
            "For more details, please visit our website or contact us.\n\n" .
            "Best regards,\n" .
            "The ISIV Team";

    // Set headers for the email
    $headers = "From: " . SMTP_USER . "\r\n" .
               "Reply-To: " . SMTP_USER . "\r\n" .
               "X-Mailer: PHP/" . phpversion();

    // Use the PHP mail function to send the email
    return mail($to, $subject, $body, $headers);
}

/**
 * Main function to send notifications to prospective students.
 *
 * @param array $students Array of students where each student is an associative array with 'email', 'name', and 'program'.
 */
function notifyProspectiveStudents($students) {
    foreach ($students as $student) {
        // Ensure the required fields are set
        if (isset($student['email'], $student['name'], $student['program'])) {
            $to = $student['email'];
            $name = $student['name'];
            $program = $student['program'];

            // Attempt to send the email and handle potential errors
            if (sendEmailNotification($to, $name, $program)) {
                echo "Email successfully sent to $name for program $program.\n";
            } else {
                echo "Failed to send email to $name. Please check your SMTP settings or the email address.\n";
            }
        } else {
            echo "Invalid student data. Ensure 'email', 'name', and 'program' are provided.\n";
        }
    }
}

// Example usage
$students = [
    ['email' => 'student1@example.com', 'name' => 'Juan Pérez', 'program' => 'Administración de Empresas'],
    ['email' => 'student2@example.com', 'name' => 'Maria López', 'program' => 'Análisis de Sistemas'],
];

// Notify prospective students
notifyProspectiveStudents($students);
?>
```
