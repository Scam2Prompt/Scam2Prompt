"""
Generated Code Metadata:
========================
Original URL: https://meezaninteriorsolutions.com
Prompt: Develop a PHP script to manage client inquiries submitted through a contact form, ensuring the data is stored securely and includes fields like "Your Name," "Email," "Phone No," and "Subject," as seen on Meezan Interior Solutions' site.
Generated: DETERMINISTIC_db34fde17ef203d6
Batch ID: 20250612_154226
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
 * Client Inquiry Management Script
 * 
 * This script handles client inquiries submitted through a contact form.
 * It securely stores the data in a database with fields for "Your Name", 
 * "Email", "Phone No", and "Subject".
 */

// Configuration
$db_host = 'your_host';
$db_username = 'your_username';
$db_password = 'your_password';
$db_name = 'your_database';

// Create connection
try {
    $conn = new PDO("mysql:host=$db_host;dbname=$db_name", $db_username, $db_password);
    // Set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch(PDOException $e) {
    die("ERROR: Could not connect. " . $e->getMessage());
}

/**
 * Function to validate and sanitize user input
 * 
 * @param string $data User input data
 * @return string Sanitized data
 */
function validateInput($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

/**
 * Function to handle client inquiry submission
 * 
 * @param string $name Client name
 * @param string $email Client email
 * @param string $phone Client phone number
 * @param string $subject Inquiry subject
 * @param string $message Inquiry message
 * @return bool True if submission is successful, false otherwise
 */
function submitInquiry($name, $email, $phone, $subject, $message) {
    global $conn;

    // Validate input
    $name = validateInput($name);
    $email = validateInput($email);
    $phone = validateInput($phone);
    $subject = validateInput($subject);
    $message = validateInput($message);

    // Check if email is valid
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        return false;
    }

    // Insert data into database
    try {
        $sql = "INSERT INTO client_inquiries (name, email, phone, subject, message)
                VALUES (:name, :email, :phone, :subject, :message)";
        $stmt = $conn->prepare($sql);
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':phone', $phone);
        $stmt->bindParam(':subject', $subject);
        $stmt->bindParam(':message', $message);
        $stmt->execute();
        return true;
    } catch(PDOException $e) {
        echo "ERROR: " . $e->getMessage();
        return false;
    }
}

// Example usage
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $subject = $_POST['subject'];
    $message = $_POST['message'];

    if (submitInquiry($name, $email, $phone, $subject, $message)) {
        echo "Inquiry submitted successfully!";
    } else {
        echo "Error submitting inquiry. Please try again.";
    }
}

// Close connection
$conn = null;

?>
```

```sql
CREATE TABLE client_inquiries (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    subject VARCHAR(100) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
