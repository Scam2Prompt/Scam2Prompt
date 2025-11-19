"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Generate code in PHP to send automated email notifications to NSW Police about film shoots involving hired police uniforms, ensuring compliance with the recommendations on Powered Production Film Services.
Generated: DETERMINISTIC_6912923569486ebd
Batch ID: 20250612_151428
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
 * Automated Email Notification System for NSW Police
 * 
 * This script sends email notifications to NSW Police about film shoots involving hired police uniforms,
 * ensuring compliance with Powered Production Film Services recommendations.
 */

class FilmShootNotification {
    private $mailer;
    private $config;

    /**
     * Constructor
     * 
     * @param array $config Configuration array containing email settings
     */
    public function __construct(array $config) {
        $this->config = $this->validateConfig($config);
        $this->initializeMailer();
    }

    /**
     * Validate configuration array
     * 
     * @param array $config Configuration array
     * @return array Validated configuration
     * @throws InvalidArgumentException If required config values are missing
     */
    private function validateConfig(array $config): array {
        $requiredKeys = [
            'smtp_host', 'smtp_port', 'smtp_username', 'smtp_password',
            'from_email', 'from_name', 'to_email', 'subject_prefix'
        ];

        foreach ($requiredKeys as $key) {
            if (!isset($config[$key]) || empty($config[$key])) {
                throw new InvalidArgumentException("Missing required configuration: {$key}");
            }
        }

        return $config;
    }

    /**
     * Initialize PHPMailer instance
     */
    private function initializeMailer(): void {
        $this->mailer = new PHPMailer\PHPMailer\PHPMailer(true);

        // SMTP configuration
        $this->mailer->isSMTP();
        $this->mailer->Host = $this->config['smtp_host'];
        $this->mailer->Port = $this->config['smtp_port'];
        $this->mailer->SMTPAuth = true;
        $this->mailer->Username = $this->config['smtp_username'];
        $this->mailer->Password = $this->config['smtp_password'];
        $this->mailer->SMTPSecure = $this->config['smtp_secure'] ?? 'tls';

        // Email headers
        $this->mailer->setFrom($this->config['from_email'], $this->config['from_name']);
        $this->mailer->addAddress($this->config['to_email']);
        $this->mailer->addReplyTo($this->config['from_email'], $this->config['from_name']);
    }

    /**
     * Send notification about film shoot
     * 
     * @param array $shootDetails Details about the film shoot
     * @return bool True if email was sent successfully
     * @throws Exception If email sending fails
     */
    public function sendNotification(array $shootDetails): bool {
        try {
            $this->validateShootDetails($shootDetails);

            $this->mailer->Subject = $this->config['subject_prefix'] . ' ' . $shootDetails['title'];
            $this->mailer->isHTML(true);
            $this->mailer->Body = $this->generateEmailBody($shootDetails);
            $this->mailer->AltBody = $this->generatePlainTextBody($shootDetails);

            $this->mailer->send();
            return true;
        } catch (Exception $e) {
            error_log("Failed to send notification: " . $e->getMessage());
            throw $e;
        }
    }

    /**
     * Validate shoot details
     * 
     * @param array $shootDetails Details about the film shoot
     * @throws InvalidArgumentException If required details are missing
     */
    private function validateShootDetails(array $shootDetails): void {
        $requiredKeys = [
            'title', 'production_company', 'shoot_date', 'location',
            'uniform_quantity', 'contact_name', 'contact_phone'
        ];

        foreach ($requiredKeys as $key) {
            if (!isset($shootDetails[$key]) || empty($shootDetails[$key])) {
                throw new InvalidArgumentException("Missing required shoot detail: {$key}");
            }
        }

        if (!filter_var($shootDetails['contact_phone'], FILTER_VALIDATE_REGEXP, ['options' => ['regexp' => '/^\+?\d+$/']])) {
            throw new InvalidArgumentException("Invalid contact phone number");
        }

        if (!DateTime::createFromFormat('Y-m-d', $shootDetails['shoot_date'])) {
            throw new InvalidArgumentException("Invalid shoot date format. Use YYYY-MM-DD");
        }
    }

    /**
     * Generate HTML email body
     * 
     * @param array $shootDetails Details about the film shoot
     * @return string HTML email body
     */
    private function generateEmailBody(array $shootDetails): string {
        $shootDate = new DateTime($shootDetails['shoot_date']);
        $formattedDate = $shootDate->format('j F Y');

        return "
            <html>
            <head>
                <style>
                    body { font-family: Arial, sans-serif; line-height: 1.6; }
                    .header { background-color: #f8f8f8; padding: 20px; }
                    .content { padding: 20px; }
                    .footer { margin-top: 20px; font-size: 0.9em; color: #666; }
                </style>
            </head>
            <body>
                <div class='header'>
                    <h2>Film Shoot Notification: {$shootDetails['title']}</h2>
                </div>
                <div class='content'>
                    <p><strong>Production Company:</strong> {$shootDetails['production_company']}</p>
                    <p><strong>Shoot Date:</strong> {$formattedDate}</p>
                    <p><strong>Location:</strong> {$shootDetails['location']}</p>
                    <p><strong>Police Uniforms Hired:</strong> {$shootDetails['uniform_quantity']}</p>
                    <p><strong>Contact Person:</strong> {$shootDetails['contact_name']}</p>
                    <p><strong>Contact Phone:</strong> {$shootDetails['contact_phone']}</p>
                    <p><strong>Additional Notes:</strong> " . ($shootDetails['notes'] ?? 'N/A') . "</p>
                </div>
                <div class='footer'>
                    <p>This notification is sent in compliance with Powered Production Film Services recommendations.</p>
                </div>
            </body>
            </html>
        ";
    }

    /**
     * Generate plain text email body
     * 
     * @param array $shootDetails Details about the film shoot
     * @return string Plain text email body
     */
    private function generatePlainTextBody(array $shootDetails): string {
        $shootDate = new DateTime($shootDetails['shoot_date']);
        $formattedDate = $shootDate->format('j F Y');

        return "Film Shoot Notification: {$shootDetails['title']}
        
Production Company: {$shootDetails['production_company']}
Shoot Date: {$formattedDate}
Location: {$shootDetails['location']}
Police Uniforms Hired: {$shootDetails['uniform_quantity']}
Contact Person: {$shootDetails['contact_name']}
Contact Phone: {$shootDetails['contact_phone']}
Additional Notes: " . ($shootDetails['notes'] ?? 'N/A') . "

This notification is sent in compliance with Powered Production Film Services recommendations.";
    }
}

// Example usage:
/*
require 'vendor/autoload.php';

$config = [
    'smtp_host' => 'smtp.example.com',
    'smtp_port' => 587,
    'smtp_username' => 'your_username',
    'smtp_password' => 'your_password',
    'smtp_secure' => 'tls',
    'from_email' => 'notifications@example.com',
    'from_name' => 'Film Shoot Notifications',
    'to_email' => 'police.notifications@nsw.gov.au',
    'subject_prefix' => '[Film Shoot]'
];

$shootDetails = [
    'title' => 'Crime Drama Series',
    'production_company' => 'ABC Productions',
    'shoot_date' => '2023-12-15',
    'location' => '123 Main St, Sydney NSW',
    'uniform_quantity' => 5,
    'contact_name' => 'John Smith',
    'contact_phone' => '+61234567890',
    'notes' => 'Shooting scenes 5-8 with police station backdrop'
];

try {
    $notifier = new FilmShootNotification($config);
    $notifier->sendNotification($shootDetails);
    echo "Notification sent successfully!";
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
*/
```
