"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mstoolsnetshop.com
Prompt: Create a PHP script for a banking system with billing code, email, and SMS notifications, similar to the "Bankpro PHP Script" described on mstoolsnetshop.com.
Generated: DETERMINISTIC_5d9ce76d664a086c
Batch ID: 20250612_145619
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.smsprovider.com/send": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
// Banking System Script
// This script handles user accounts, transactions, and notifications.

// Database configuration
$host = 'localhost';
$db_name = 'banking_system';
$username = 'root';
$password = '';

// Establish database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db_name", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}

// Function to create a new user account
function createUser($name, $email, $phone) {
    global $pdo;
    try {
        $stmt = $pdo->prepare("INSERT INTO users (name, email, phone) VALUES (:name, :email, :phone)");
        $stmt->execute(['name' => $name, 'email' => $email, 'phone' => $phone]);
        return $pdo->lastInsertId(); // Return the new user's ID
    } catch (PDOException $e) {
        error_log("Error creating user: " . $e->getMessage());
        return false;
    }
}

// Function to process a transaction
function processTransaction($userId, $amount) {
    global $pdo;
    try {
        $stmt = $pdo->prepare("INSERT INTO transactions (user_id, amount) VALUES (:user_id, :amount)");
        $stmt->execute(['user_id' => $userId, 'amount' => $amount]);
        sendNotification($userId, $amount); // Send notification after transaction
        return true;
    } catch (PDOException $e) {
        error_log("Error processing transaction: " . $e->getMessage());
        return false;
    }
}

// Function to send email notification
function sendEmail($email, $amount) {
    $subject = "Transaction Notification";
    $message = "A transaction of $$amount has been processed.";
    $headers = 'From: no-reply@bankingsystem.com' . "\r\n" .
               'Reply-To: no-reply@bankingsystem.com' . "\r\n" .
               'X-Mailer: PHP/' . phpversion();

    if (!mail($email, $subject, $message, $headers)) {
        error_log("Error sending email to $email");
    }
}

// Function to send SMS notification
function sendSMS($phone, $amount) {
    // Using a hypothetical SMS API for sending messages
    $api_url = "https://api.smsprovider.com/send";
    $api_key = "YOUR_API_KEY"; // Replace with your actual API Key
    $message = "A transaction of $$amount has been processed.";

    $data = [
        'api_key' => $api_key,
        'phone'   => $phone,
        'message' => $message
    ];

    $options = [
        'http' => [
            'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
            'method'  => 'POST',
            'content' => http_build_query($data),
        ],
    ];

    $context  = stream_context_create($options);
    $result = file_get_contents($api_url, false, $context);
    if ($result === FALSE) {
        error_log("Error sending SMS to $phone");
    }
}

// Function to send notifications via email and SMS
function sendNotification($userId, $amount) {
    global $pdo;

    $stmt = $pdo->prepare("SELECT email, phone FROM users WHERE id = :id");
    $stmt->execute(['id' => $userId]);
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    if ($user) {
        sendEmail($user['email'], $amount);
        sendSMS($user['phone'], $amount);
    } else {
        error_log("User not found for ID: $userId");
    }
}

// Example usage
$userId = createUser("John Doe", "john.doe@example.com", "1234567890");
if ($userId) {
    processTransaction($userId, 100.00);
}

// Close database connection
$pdo = null;
?>
```

Make sure to replace placeholder values (like database credentials and SMS API keys) with your actual values before running this script. The script assumes that you have a MySQL database with appropriate tables set up (`users` and `transactions`).
