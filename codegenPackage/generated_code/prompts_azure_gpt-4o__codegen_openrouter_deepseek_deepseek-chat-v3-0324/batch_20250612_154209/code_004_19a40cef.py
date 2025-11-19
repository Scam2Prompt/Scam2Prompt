"""
Generated Code Metadata:
========================
Original URL: https://isiv.edu.ar
Prompt: Write a PHP script to send automated email notifications to prospective students about ISIV's open enrollment for 2025, referencing specific programs like "Administración de Empresas" and "Análisis de Sistemas."
Generated: DETERMINISTIC_19a40cef23b06dc3
Batch ID: 20250612_154209
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
 * Script to send automated email notifications to prospective students about ISIV's open enrollment for 2025.
 * 
 * This script handles:
 * - Email template generation
 * - Recipient management
 * - SMTP email sending
 * - Error handling and logging
 */

// Configuration
define('SMTP_HOST', 'smtp.example.com');
define('SMTP_PORT', 587);
define('SMTP_USERNAME', 'your_email@example.com');
define('SMTP_PASSWORD', 'your_password');
define('FROM_EMAIL', 'admissions@isiv.edu');
define('FROM_NAME', 'ISIV Admissions Office');
define('SUBJECT', 'Open Enrollment 2025 - ISIV Programs Available');

// Programs information
$programs = [
    'Administración de Empresas' => 'Business Administration program focusing on modern management techniques.',
    'Análisis de Sistemas' => 'Systems Analysis program with emphasis on software development and IT solutions.'
];

// Database configuration (example - adjust to your actual setup)
$dbHost = 'localhost';
$dbUser = 'db_user';
$dbPass = 'db_password';
$dbName = 'isiv_prospects';

/**
 * Get prospective students from database
 * 
 * @return array List of prospective students with email addresses
 * @throws Exception If database connection fails
 */
function getProspectiveStudents() {
    global $dbHost, $dbUser, $dbPass, $dbName;
    
    try {
        $conn = new PDO("mysql:host=$dbHost;dbname=$dbName", $dbUser, $dbPass);
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        
        $stmt = $conn->prepare("SELECT email, first_name, last_name FROM prospective_students WHERE active = 1");
        $stmt->execute();
        
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch(PDOException $e) {
        error_log("Database error: " . $e->getMessage());
        throw new Exception("Could not retrieve prospective students");
    }
}

/**
 * Generate email content
 * 
 * @param string $firstName Recipient's first name
 * @param array $programs List of programs with descriptions
 * @return string Generated HTML email content
 */
function generateEmailContent($firstName, $programs) {
    $programsList = '';
    foreach ($programs as $name => $desc) {
        $programsList .= "<li><strong>$name</strong>: $desc</li>";
    }
    
    return <<<HTML
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; }
        .header { color: #003366; }
        .program-list { margin: 20px 0; }
        .footer { margin-top: 20px; font-size: 0.9em; color: #666; }
    </style>
</head>
<body>
    <p>Dear $firstName,</p>
    
    <p>We're excited to announce that open enrollment for ISIV's 2025 academic year is now available!</p>
    
    <div class="program-list">
        <h3 class="header">Featured Programs:</h3>
        <ul>
            $programsList
        </ul>
    </div>
    
    <p>Don't miss this opportunity to join one of our prestigious programs. Apply now to secure your spot!</p>
    
    <div class="footer">
        <p>Best regards,<br>
        ISIV Admissions Office<br>
        <a href="mailto:admissions@isiv.edu">admissions@isiv.edu</a></p>
    </div>
</body>
</html>
HTML;
}

/**
 * Send email using PHPMailer
 * 
 * @param string $to Recipient email
 * @param string $name Recipient name
 * @param string $subject Email subject
 * @param string $body Email HTML content
 * @return bool True if sent successfully, false otherwise
 */
function sendEmail($to, $name, $subject, $body) {
    require_once 'vendor/autoload.php'; // Assuming PHPMailer is installed via Composer
    
    $mail = new PHPMailer\PHPMailer\PHPMailer(true);
    
    try {
        // Server settings
        $mail->isSMTP();
        $mail->Host = SMTP_HOST;
        $mail->SMTPAuth = true;
        $mail->Username = SMTP_USERNAME;
        $mail->Password = SMTP_PASSWORD;
        $mail->SMTPSecure = PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_STARTTLS;
        $mail->Port = SMTP_PORT;
        
        // Recipients
        $mail->setFrom(FROM_EMAIL, FROM_NAME);
        $mail->addAddress($to, $name);
        
        // Content
        $mail->isHTML(true);
        $mail->Subject = $subject;
        $mail->Body = $body;
        $mail->AltBody = strip_tags($body);
        
        $mail->send();
        return true;
    } catch (Exception $e) {
        error_log("Email error for $to: " . $mail->ErrorInfo);
        return false;
    }
}

// Main execution
try {
    // Get recipients
    $prospects = getProspectiveStudents();
    $total = count($prospects);
    $successCount = 0;
    
    if ($total === 0) {
        exit("No prospective students found in database.\n");
    }
    
    // Process each prospect
    foreach ($prospects as $prospect) {
        $email = $prospect['email'];
        $name = $prospect['first_name'] . ' ' . $prospect['last_name'];
        
        // Generate email content
        $content = generateEmailContent($prospect['first_name'], $programs);
        
        // Send email
        if (sendEmail($email, $name, SUBJECT, $content)) {
            $successCount++;
            echo "Sent to: $email\n";
        } else {
            echo "Failed to send to: $email\n";
        }
    }
    
    // Summary
    echo "\nCampaign completed.\n";
    echo "Total emails: $total\n";
    echo "Successfully sent: $successCount\n";
    echo "Failed: " . ($total - $successCount) . "\n";
    
} catch (Exception $e) {
    error_log("Fatal error: " . $e->getMessage());
    echo "An error occurred. Please check the logs.\n";
    exit(1);
}
```
