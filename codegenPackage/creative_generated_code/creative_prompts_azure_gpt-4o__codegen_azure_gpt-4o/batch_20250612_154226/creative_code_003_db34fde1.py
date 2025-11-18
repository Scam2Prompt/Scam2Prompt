"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meezaninteriorsolutions.com
Prompt: Develop a PHP script to manage client inquiries submitted through a contact form, ensuring the data is stored securely and includes fields like "Your Name," "Email," "Phone No," and "Subject," as seen on Meezan Interior Solutions' site.
Generated: DETERMINISTIC_db34fde17ef203d6
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Contact Form Handling Script for Client Inquiries
// Author: [Your Name]
// Date: [Date]
// Version: 1.0

// Database configuration
define('DB_HOST', 'localhost'); // Database host
define('DB_NAME', 'meezan_interior'); // Database name
define('DB_USER', 'root'); // Database username
define('DB_PASS', 'password'); // Database password

// Function to sanitize user input
function sanitizeInput($data)
{
    return htmlspecialchars(trim($data));
}

// Function to establish a database connection
function getDatabaseConnection()
{
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        die("Database connection failed: " . $e->getMessage());
    }
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve and sanitize form data
    $name = sanitizeInput($_POST['name'] ?? '');
    $email = sanitizeInput($_POST['email'] ?? '');
    $phone = sanitizeInput($_POST['phone'] ?? '');
    $subject = sanitizeInput($_POST['subject'] ?? '');

    // Validate form data
    $errors = [];
    if (empty($name)) $errors[] = "Name is required.";
    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) $errors[] = "Valid email is required.";
    if (empty($phone) || !preg_match('/^\+?[0-9\- ]+$/', $phone)) $errors[] = "Valid phone number is required.";
    if (empty($subject)) $errors[] = "Subject is required.";

    // If validation fails, return errors
    if (!empty($errors)) {
        // Return errors to the user (In production, you may want to handle this differently)
        header('Content-Type: application/json');
        echo json_encode(['status' => 'error', 'errors' => $errors]);
        exit;
    }

    // Save data to the database
    try {
        $pdo = getDatabaseConnection();
        $stmt = $pdo->prepare("INSERT INTO inquiries (name, email, phone, subject) VALUES (:name, :email, :phone, :subject)");
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':phone', $phone);
        $stmt->bindParam(':subject', $subject);

        if ($stmt->execute()) {
            // Return success response
            header('Content-Type: application/json');
            echo json_encode(['status' => 'success', 'message' => 'Inquiry submitted successfully.']);
        } else {
            // Return failure response
            header('Content-Type: application/json');
            echo json_encode(['status' => 'error', 'message' => 'Failed to submit inquiry.']);
        }
    } catch (Exception $e) {
        // Handle database errors gracefully
        header('Content-Type: application/json');
        echo json_encode(['status' => 'error', 'message' => 'An error occurred: ' . $e->getMessage()]);
    }
} else {
    // If the form is not submitted using POST, return an error
    header('Content-Type: application/json');
    echo json_encode(['status' => 'error', 'message' => 'Invalid request method.']);
    exit;
}
```
