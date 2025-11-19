"""
Generated Code Metadata:
========================
Original URL: https://osmokro.org
Prompt: Create a PHP code snippet to send an email notification to parents about upcoming events at Основна школа "Мокро", including details from the "Родитељи" section.
Generated: DETERMINISTIC_f60be9b1465e3b8d
Batch ID: 20250612_135754
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
 * Sends email notifications to parents about upcoming events at Основна школа "Мокро"
 */

// Import PHPMailer classes
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'vendor/autoload.php'; // Path to PHPMailer autoload

class ParentNotification {
    private $mailer;
    private $db;

    public function __construct() {
        // Initialize PHPMailer
        $this->mailer = new PHPMailer(true);
        
        // Database configuration (replace with your actual credentials)
        $this->db = new PDO(
            'mysql:host=localhost;dbname=school_db;charset=utf8mb4',
            'username',
            'password',
            [
                PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
            ]
        );
    }

    /**
     * Send event notifications to parents
     * @param int $eventId The ID of the event to notify about
     * @return array Results of the sending operation
     */
    public function sendEventNotifications($eventId) {
        try {
            // Get event details
            $event = $this->getEventDetails($eventId);
            if (!$event) {
                throw new Exception("Event not found");
            }

            // Get parent emails
            $parents = $this->getParentEmails();
            if (empty($parents)) {
                throw new Exception("No parent emails found");
            }

            // Configure mailer
            $this->configureMailer();

            $results = [
                'success' => 0,
                'failed' => 0,
                'errors' => []
            ];

            // Send emails to each parent
            foreach ($parents as $parent) {
                try {
                    $this->mailer->clearAddresses();
                    $this->mailer->addAddress($parent['email'], $parent['name']);
                    
                    $this->mailer->Subject = "Важно обавештење: {$event['title']}";
                    $this->mailer->Body = $this->generateEmailBody($event, $parent);
                    $this->mailer->AltBody = strip_tags($this->generateEmailBody($event, $parent));

                    $this->mailer->send();
                    $results['success']++;
                } catch (Exception $e) {
                    $results['failed']++;
                    $results['errors'][] = "Failed to send to {$parent['email']}: " . $e->getMessage();
                }
            }

            return $results;

        } catch (Exception $e) {
            error_log("Parent notification error: " . $e->getMessage());
            return [
                'success' => 0,
                'failed' => count($parents ?? []),
                'errors' => [$e->getMessage()]
            ];
        }
    }

    /**
     * Configure PHPMailer settings
     */
    private function configureMailer() {
        // Server settings
        $this->mailer->isSMTP();
        $this->mailer->Host = 'smtp.example.com';
        $this->mailer->SMTPAuth = true;
        $this->mailer->Username = 'school@example.com';
        $this->mailer->Password = 'smtp_password';
        $this->mailer->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
        $this->mailer->Port = 587;

        // Sender info
        $this->mailer->setFrom('school@example.com', 'Основна школа "Мокро"');
        $this->mailer->isHTML(true);
        $this->mailer->CharSet = 'UTF-8';
    }

    /**
     * Get event details from database
     * @param int $eventId
     * @return array|null
     */
    private function getEventDetails($eventId) {
        $stmt = $this->db->prepare(
            "SELECT title, description, event_date, location 
             FROM events 
             WHERE id = ?"
        );
        $stmt->execute([$eventId]);
        return $stmt->fetch();
    }

    /**
     * Get parent emails from database
     * @return array
     */
    private function getParentEmails() {
        $stmt = $this->db->query(
            "SELECT p.email, CONCAT(p.first_name, ' ', p.last_name) as name
             FROM parents p
             WHERE p.email IS NOT NULL"
        );
        return $stmt->fetchAll();
    }

    /**
     * Generate email HTML body
     * @param array $event
     * @param array $parent
     * @return string
     */
    private function generateEmailBody($event, $parent) {
        $date = date('d.m.Y.', strtotime($event['event_date']));
        
        return "
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset='UTF-8'>
                <title>Обавештење о догађају</title>
            </head>
            <body>
                <p>Поштовани {$parent['name']},</p>
                
                <p>Обавештавамо вас о предстојећем догађају у нашој школи:</p>
                
                <h2>{$event['title']}</h2>
                
                <p><strong>Датум:</strong> {$date}</p>
                <p><strong>Место:</strong> {$event['location']}</p>
                
                <div>{$event['description']}</div>
                
                <p>Срдачан поздрав,<br>
                Основна школа „Мокро“</p>
            </body>
            </html>
        ";
    }
}

// Example usage:
// $notification = new ParentNotification();
// $results = $notification->sendEventNotifications(123); // Replace with actual event ID
// print_r($results);
?>
```
