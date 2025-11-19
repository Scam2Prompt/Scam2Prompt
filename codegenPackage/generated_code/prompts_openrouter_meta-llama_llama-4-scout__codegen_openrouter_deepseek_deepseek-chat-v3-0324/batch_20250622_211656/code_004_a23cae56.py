"""
Generated Code Metadata:
========================
Original URL: https://pansos4dz.com
Prompt: "Create a notification system in PHP for sending alerts about new promotions, live chat support, and transaction updates on a site like PANSOS4D."
Generated: DETERMINISTIC_a23cae5615517439
Batch ID: 20250622_211656
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
 * Notification System for PANSOS4D-like Site
 * 
 * Handles sending alerts for promotions, live chat, and transaction updates.
 */

class NotificationSystem {
    private $dbConnection;
    private $mailer;
    private $pushService;

    /**
     * Constructor
     * 
     * @param PDO $dbConnection Database connection object
     * @param object $mailer Mail service object (e.g., PHPMailer)
     * @param object $pushService Push notification service
     */
    public function __construct(PDO $dbConnection, $mailer = null, $pushService = null) {
        $this->dbConnection = $dbConnection;
        $this->mailer = $mailer;
        $this->pushService = $pushService;
    }

    /**
     * Send notification to user
     * 
     * @param int $userId Recipient user ID
     * @param string $type Notification type (promotion, chat, transaction)
     * @param string $message Notification content
     * @param array $options Additional options (email, push, etc.)
     * @return bool True if successful, false on failure
     */
    public function sendNotification($userId, $type, $message, $options = []) {
        try {
            // Validate input
            if (empty($userId) || empty($type) || empty($message)) {
                throw new InvalidArgumentException("Missing required parameters");
            }

            $validTypes = ['promotion', 'chat', 'transaction'];
            if (!in_array($type, $validTypes)) {
                throw new InvalidArgumentException("Invalid notification type");
            }

            // Store notification in database
            $stmt = $this->dbConnection->prepare(
                "INSERT INTO notifications (user_id, type, message, created_at) 
                 VALUES (:user_id, :type, :message, NOW())"
            );
            $stmt->execute([
                ':user_id' => $userId,
                ':type' => $type,
                ':message' => $message
            ]);

            // Send email if requested
            if (isset($options['email']) && $options['email'] && $this->mailer) {
                $this->sendEmailNotification($userId, $type, $message);
            }

            // Send push notification if requested
            if (isset($options['push']) && $options['push'] && $this->pushService) {
                $this->sendPushNotification($userId, $type, $message);
            }

            return true;
        } catch (Exception $e) {
            error_log("Notification error: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Send email notification
     * 
     * @param int $userId Recipient user ID
     * @param string $type Notification type
     * @param string $message Notification content
     */
    private function sendEmailNotification($userId, $type, $message) {
        try {
            $userEmail = $this->getUserEmail($userId);
            if (!$userEmail) {
                throw new Exception("User email not found");
            }

            $subject = $this->getEmailSubject($type);
            $this->mailer->clearAddresses();
            $this->mailer->addAddress($userEmail);
            $this->mailer->Subject = $subject;
            $this->mailer->Body = $this->formatEmailContent($type, $message);
            $this->mailer->send();
        } catch (Exception $e) {
            error_log("Email notification error: " . $e->getMessage());
        }
    }

    /**
     * Send push notification
     * 
     * @param int $userId Recipient user ID
     * @param string $type Notification type
     * @param string $message Notification content
     */
    private function sendPushNotification($userId, $type, $message) {
        try {
            $deviceToken = $this->getUserDeviceToken($userId);
            if (!$deviceToken) {
                throw new Exception("User device token not found");
            }

            $title = $this->getPushTitle($type);
            $this->pushService->send($deviceToken, $title, $message);
        } catch (Exception $e) {
            error_log("Push notification error: " . $e->getMessage());
        }
    }

    /**
     * Get user email from database
     * 
     * @param int $userId User ID
     * @return string|null User email or null if not found
     */
    private function getUserEmail($userId) {
        $stmt = $this->dbConnection->prepare(
            "SELECT email FROM users WHERE id = :user_id LIMIT 1"
        );
        $stmt->execute([':user_id' => $userId]);
        $result = $stmt->fetch(PDO::FETCH_ASSOC);
        return $result ? $result['email'] : null;
    }

    /**
     * Get user device token from database
     * 
     * @param int $userId User ID
     * @return string|null Device token or null if not found
     */
    private function getUserDeviceToken($userId) {
        $stmt = $this->dbConnection->prepare(
            "SELECT device_token FROM user_devices WHERE user_id = :user_id LIMIT 1"
        );
        $stmt->execute([':user_id' => $userId]);
        $result = $stmt->fetch(PDO::FETCH_ASSOC);
        return $result ? $result['device_token'] : null;
    }

    /**
     * Get email subject based on notification type
     * 
     * @param string $type Notification type
     * @return string Email subject
     */
    private function getEmailSubject($type) {
        $subjects = [
            'promotion' => 'New Promotion Available!',
            'chat' => 'New Live Chat Message',
            'transaction' => 'Transaction Update'
        ];
        return $subjects[$type] ?? 'Notification from PANSOS4D';
    }

    /**
     * Get push notification title based on type
     * 
     * @param string $type Notification type
     * @return string Push title
     */
    private function getPushTitle($type) {
        $titles = [
            'promotion' => '🔥 New Promotion',
            'chat' => '💬 Live Chat',
            'transaction' => '💰 Transaction'
        ];
        return $titles[$type] ?? 'Notification';
    }

    /**
     * Format email content
     * 
     * @param string $type Notification type
     * @param string $message Notification content
     * @return string Formatted HTML email
     */
    private function formatEmailContent($type, $message) {
        $template = "
        <html>
        <head>
            <style>
                body { font-family: Arial, sans-serif; line-height: 1.6; }
                .container { max-width: 600px; margin: 0 auto; padding: 20px; }
                .header { background-color: #f8f9fa; padding: 20px; text-align: center; }
                .content { padding: 20px; }
                .footer { margin-top: 20px; font-size: 12px; color: #6c757d; }
            </style>
        </head>
        <body>
            <div class='container'>
                <div class='header'>
                    <h2>%s</h2>
                </div>
                <div class='content'>
                    <p>%s</p>
                </div>
                <div class='footer'>
                    <p>PANSOS4D Notification System</p>
                </div>
            </div>
        </body>
        </html>
        ";

        $title = $this->getEmailSubject($type);
        return sprintf($template, $title, $message);
    }
}

// Example usage:
/*
$db = new PDO('mysql:host=localhost;dbname=pansos4d', 'username', 'password');
$mailer = new PHPMailer\PHPMailer\PHPMailer(true);
$pushService = new PushNotificationService();

$notificationSystem = new NotificationSystem($db, $mailer, $pushService);

// Send promotion notification
$notificationSystem->sendNotification(
    123,
    'promotion',
    'New 50% discount on all deposits this weekend!',
    ['email' => true, 'push' => true]
);

// Send chat notification
$notificationSystem->sendNotification(
    123,
    'chat',
    'You have a new message from support team',
    ['push' => true]
);

// Send transaction notification
$notificationSystem->sendNotification(
    123,
    'transaction',
    'Your deposit of $100 has been processed successfully',
    ['email' => true]
);
*/
?>
```
