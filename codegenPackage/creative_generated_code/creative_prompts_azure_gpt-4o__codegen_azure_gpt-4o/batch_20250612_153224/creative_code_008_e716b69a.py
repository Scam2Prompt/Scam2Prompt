"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alpha-digitalsolutions.com
Prompt: Create a PHP script to manage client inquiries and consultations, referencing Alpha Digital Solutions' free consultation feature.
Generated: DETERMINISTIC_e716b69a974f618b
Batch ID: 20250612_153224
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
 * Client Inquiry and Consultation Management
 * This script manages client inquiries and consultations for Alpha Digital Solutions.
 * It includes features for storing inquiries, scheduling consultations, and sending email notifications.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'alpha_digital');
define('DB_USER', 'root');
define('DB_PASS', 'password');

// Establish database connection
function getDatabaseConnection() {
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS, [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        ]);
        return $pdo;
    } catch (PDOException $e) {
        error_log("Database connection failed: " . $e->getMessage());
        die("Database connection failed. Please try again later.");
    }
}

// Function to handle client inquiries
function handleInquiry($name, $email, $message) {
    $pdo = getDatabaseConnection();

    // Validate input
    if (empty($name) || empty($email) || empty($message)) {
        return ['success' => false, 'message' => 'All fields are required.'];
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        return ['success' => false, 'message' => 'Invalid email address.'];
    }

    // Insert inquiry into the database
    $stmt = $pdo->prepare("INSERT INTO inquiries (name, email, message, created_at) VALUES (:name, :email, :message, NOW())");
    try {
        $stmt->execute(['name' => $name, 'email' => $email, 'message' => $message]);
        return ['success' => true, 'message' => 'Inquiry submitted successfully.'];
    } catch (PDOException $e) {
        error_log("Failed to insert inquiry: " . $e->getMessage());
        return ['success' => false, 'message' => 'Failed to submit inquiry. Please try again later.'];
    }
}

// Function to schedule a free consultation
function scheduleConsultation($name, $email, $date, $time) {
    $pdo = getDatabaseConnection();

    // Validate input
    if (empty($name) || empty($email) || empty($date) || empty($time)) {
        return ['success' => false, 'message' => 'All fields are required.'];
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        return ['success' => false, 'message' => 'Invalid email address.'];
    }

    // Insert consultation details into the database
    $stmt = $pdo->prepare("INSERT INTO consultations (name, email, consultation_date, consultation_time, created_at) VALUES (:name, :email, :date, :time, NOW())");
    try {
        $stmt->execute(['name' => $name, 'email' => $email, 'date' => $date, 'time' => $time]);
        // Send email notification (dummy function for demonstration purposes)
        sendEmailNotification($email, "Your consultation is scheduled for $date at $time.");
        return ['success' => true, 'message' => 'Consultation scheduled successfully.'];
    } catch (PDOException $e) {
        error_log("Failed to schedule consultation: " . $e->getMessage());
        return ['success' => false, 'message' => 'Failed to schedule consultation. Please try again later.'];
    }
}

// Dummy function to send email notifications
function sendEmailNotification($email, $message) {
    // In production, use a proper mail library like PHPMailer or SwiftMailer
    mail($email, "Alpha Digital Solutions Consultation", $message);
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = $_POST['action'] ?? '';

    if ($action === 'submit_inquiry') {
        $response = handleInquiry($_POST['name'], $_POST['email'], $_POST['message']);
    } elseif ($action === 'schedule_consultation') {
        $response = scheduleConsultation($_POST['name'], $_POST['email'], $_POST['date'], $_POST['time']);
    } else {
        $response = ['success' => false, 'message' => 'Invalid action.'];
    }

    // Return JSON response
    header('Content-Type: application/json');
    echo json_encode($response);
    exit;
}
?>
```
