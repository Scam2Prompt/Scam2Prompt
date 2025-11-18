"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amirinternationalcharity.org
Prompt: Write a script in PHP to automate sending thank-you emails to donors who contribute to Amir International Charity Organization's single mothers aid program.
Generated: DETERMINISTIC_0400e1f9f8a2a096
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// thank_you_email.php

/**
 * Script to automate sending thank-you emails to donors
 * Amir International Charity Organization - Single Mothers Aid Program
 * Author: [Your Name]
 * Date: [Insert Date]
 */

// Load dependencies
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'vendor/autoload.php'; // Ensure PHPMailer is installed via Composer

/**
 * Configuration for the email server
 */
define('SMTP_HOST', 'smtp.example.com'); // Replace with your SMTP host
define('SMTP_PORT', 587);               // Replace with your SMTP port
define('SMTP_USERNAME', 'your_email@example.com'); // Replace with your email
define('SMTP_PASSWORD', 'your_password');          // Replace with your email password
define('CHARITY_EMAIL', 'charity@example.com');    // Charity organization's email
define('CHARITY_NAME', 'Amir International Charity Organization');

// Connect to the database
$dbHost = 'localhost';
$dbName = 'charity_db';
$dbUser = 'root';
$dbPass = 'password';

try {
    $pdo = new PDO("mysql:host=$dbHost;dbname=$dbName", $dbUser, $dbPass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Error connecting to the database: " . $e->getMessage());
}

/**
 * Fetch donors who have donated to the Single Mothers Aid Program
 * Donors who haven't yet received thank-you emails are identified via the 'thank_you_sent' flag.
 */
$query = "SELECT id, name, email, amount FROM donors WHERE program = 'single_mothers_aid' AND thank_you_sent = 0";

try {
    $stmt = $pdo->prepare($query);
    $stmt->execute();
    $donors = $stmt->fetchAll(PDO::FETCH_ASSOC);
} catch (Exception $e) {
    die("Error fetching donor data: " . $e->getMessage());
}

// Initialize PHPMailer instance
$mail = new PHPMailer(true);

foreach ($donors as $donor) {
    try {
        // Configure email settings
        $mail->isSMTP();
        $mail->Host = SMTP_HOST;
        $mail->Port = SMTP_PORT;
        $mail->SMTPAuth = true;
        $mail->Username = SMTP_USERNAME;
        $mail->Password = SMTP_PASSWORD;
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
        
        // Set email headers and content
        $mail->setFrom(CHARITY_EMAIL, CHARITY_NAME);
        $mail->addAddress($donor['email'], $donor['name']);
        $mail->Subject = 'Thank You for Your Generous Contribution!';
        $mail->Body = "Dear {$donor['name']},\n\n"
                    . "We sincerely thank you for your generous donation of $"
                    . number_format($donor['amount'], 2)
                    . " to the Single Mothers Aid Program. Your support is making a real difference in the lives of single mothers across the globe.\n\n"
                    . "Warm regards,\n"
                    . CHARITY_NAME;

        // Send the email
        $mail->send();

        // Update database to mark thank-you email as sent
        $updateQuery = "UPDATE donors SET thank_you_sent = 1 WHERE id = :id";
        $updateStmt = $pdo->prepare($updateQuery);
        $updateStmt->execute(['id' => $donor['id']]);

        echo "Thank-you email sent to {$donor['name']} ({$donor['email']}).\n";

    } catch (Exception $e) {
        // Log the error message
        error_log("Failed to send email to {$donor['email']}: " . $e->getMessage());
    }
}

// Close database connection
$pdo = null;

echo "Email automation script completed.\n";

?>
```
