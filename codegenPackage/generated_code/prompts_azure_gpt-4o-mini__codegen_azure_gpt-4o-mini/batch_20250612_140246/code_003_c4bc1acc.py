"""
Generated Code Metadata:
========================
Original URL: https://ugge.cc
Prompt: Develop a PHP script that sends a notification to users about their account security, similar to the system notification displayed on the webpage.
Generated: DETERMINISTIC_c4bc1accd7ec9a9e
Batch ID: 20250612_140246
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
 * NotificationSender Class
 * This class is responsible for sending account security notifications to users.
 */
class NotificationSender {
    private $dbConnection;

    /**
     * Constructor to initialize database connection.
     *
     * @param PDO $dbConnection Database connection object.
     */
    public function __construct(PDO $dbConnection) {
        $this->dbConnection = $dbConnection;
    }

    /**
     * Sends a security notification to a user.
     *
     * @param int $userId The ID of the user to notify.
     * @param string $message The notification message.
     * @return bool True on success, false on failure.
     */
    public function sendNotification(int $userId, string $message): bool {
        try {
            // Prepare the SQL statement to insert the notification
            $stmt = $this->dbConnection->prepare("INSERT INTO notifications (user_id, message, created_at) VALUES (:user_id, :message, NOW())");
            $stmt->bindParam(':user_id', $userId, PDO::PARAM_INT);
            $stmt->bindParam(':message', $message, PDO::PARAM_STR);

            // Execute the statement
            return $stmt->execute();
        } catch (PDOException $e) {
            // Log the error message for debugging
            error_log("Database error: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Fetches all notifications for a user.
     *
     * @param int $userId The ID of the user.
     * @return array An array of notifications.
     */
    public function getUserNotifications(int $userId): array {
        try {
            // Prepare the SQL statement to fetch notifications
            $stmt = $this->dbConnection->prepare("SELECT message, created_at FROM notifications WHERE user_id = :user_id ORDER BY created_at DESC");
            $stmt->bindParam(':user_id', $userId, PDO::PARAM_INT);
            $stmt->execute();

            // Fetch all notifications as an associative array
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            // Log the error message for debugging
            error_log("Database error: " . $e->getMessage());
            return [];
        }
    }
}

// Example usage
try {
    // Database connection parameters
    $dsn = 'mysql:host=localhost;dbname=your_database;charset=utf8';
    $username = 'your_username';
    $password = 'your_password';

    // Create a new PDO instance
    $dbConnection = new PDO($dsn, $username, $password);
    $dbConnection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Create an instance of NotificationSender
    $notificationSender = new NotificationSender($dbConnection);

    // Send a security notification to a user
    $userId = 1; // Example user ID
    $message = "We noticed a login from a new device. Please review your account security.";
    if ($notificationSender->sendNotification($userId, $message)) {
        echo "Notification sent successfully.";
    } else {
        echo "Failed to send notification.";
    }

    // Fetch and display notifications for the user
    $notifications = $notificationSender->getUserNotifications($userId);
    foreach ($notifications as $notification) {
        echo "[" . $notification['created_at'] . "] " . $notification['message'] . "<br>";
    }
} catch (PDOException $e) {
    // Handle connection errors
    error_log("Connection error: " . $e->getMessage());
    echo "Database connection failed.";
}
?>
```
