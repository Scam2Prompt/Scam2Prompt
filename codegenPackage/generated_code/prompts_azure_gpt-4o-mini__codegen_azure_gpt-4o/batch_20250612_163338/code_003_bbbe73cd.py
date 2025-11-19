"""
Generated Code Metadata:
========================
Original URL: https://daddysoluniversity.com
Prompt: Develop a PHP script that sends an email notification to users when new author events are scheduled at Sakura Books, highlighting the community aspect of the store.
Generated: DETERMINISTIC_bbbe73cd9981d749
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Author: [Your Name]
// Date: [Today's Date]
// Description: This script sends email notifications to users when new author events are scheduled at Sakura Books.

// Configuration for email settings
define('SMTP_HOST', 'smtp.example.com'); // Replace with your SMTP host
define('SMTP_PORT', 587);               // Replace with your SMTP port
define('SMTP_USERNAME', 'your_email@example.com'); // Replace with your SMTP username
define('SMTP_PASSWORD', 'your_password');         // Replace with your SMTP password
define('FROM_EMAIL', 'notifications@sakurabooks.com'); // Sender email address
define('FROM_NAME', 'Sakura Books');              // Sender name

// Database configuration
define('DB_HOST', 'localhost'); // Replace with your database host
define('DB_NAME', 'sakurabooks'); // Replace with your database name
define('DB_USER', 'db_user'); // Replace with your database username
define('DB_PASS', 'db_password'); // Replace with your database password

// Function to send email notifications
function sendEmailNotification($toEmail, $toName, $eventDetails) {
    // Create the email subject and body
    $subject = "New Author Event at Sakura Books!";
    $body = "Hello $toName,\n\nWe are excited to announce a new author event at Sakura Books:\n\n" .
            "Event Details:\n" .
            "Title: {$eventDetails['title']}\n" .
            "Date: {$eventDetails['date']}\n" .
            "Time: {$eventDetails['time']}\n" .
            "Location: {$eventDetails['location']}\n\n" .
            "Join us to celebrate the community and meet the author!\n\n" .
            "Best regards,\nSakura Books Team";

    // Set up email headers
    $headers = "From: " . FROM_NAME . " <" . FROM_EMAIL . ">\r\n";
    $headers .= "Reply-To: " . FROM_EMAIL . "\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Send the email
    if (mail($toEmail, $subject, $body, $headers)) {
        return true;
    } else {
        return false;
    }
}

// Function to fetch users and event details from the database
function fetchUsersAndEventDetails() {
    try {
        // Connect to the database
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        // Fetch the latest event details
        $eventQuery = $pdo->query("SELECT title, date, time, location FROM events ORDER BY created_at DESC LIMIT 1");
        $eventDetails = $eventQuery->fetch(PDO::FETCH_ASSOC);

        if (!$eventDetails) {
            throw new Exception("No events found in the database.");
        }

        // Fetch all users
        $usersQuery = $pdo->query("SELECT name, email FROM users WHERE subscribed = 1");
        $users = $usersQuery->fetchAll(PDO::FETCH_ASSOC);

        return [$users, $eventDetails];
    } catch (Exception $e) {
        error_log("Error fetching data: " . $e->getMessage());
        return [[], null];
    }
}

// Main script execution
list($users, $eventDetails) = fetchUsersAndEventDetails();

if ($eventDetails && !empty($users)) {
    foreach ($users as $user) {
        $success = sendEmailNotification($user['email'], $user['name'], $eventDetails);
        if ($success) {
            echo "Email sent successfully to {$user['email']}.\n";
        } else {
            error_log("Failed to send email to {$user['email']}.");
        }
    }
} else {
    echo "No users or events found to send notifications.\n";
}
?>
```
