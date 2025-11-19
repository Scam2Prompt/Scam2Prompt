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
// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'username');
define('DB_PASS', 'password');
define('DB_NAME', 'database_name');

// Establish database connection
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to sanitize input data
function sanitizeInput($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

// Process form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Validate and sanitize inputs
        $name = isset($_POST['name']) ? sanitizeInput($_POST['name']) : '';
        $email = isset($_POST['email']) ? sanitizeInput($_POST['email']) : '';
        $phone = isset($_POST['phone']) ? sanitizeInput($_POST['phone']) : '';
        $subject = isset($_POST['subject']) ? sanitizeInput($_POST['subject']) : '';
        $message = isset($_POST['message']) ? sanitizeInput($_POST['message']) : '';

        // Validate required fields
        if (empty($name) || empty($email) || empty($subject) || empty($message)) {
            throw new Exception('Please fill in all required fields.');
        }

        // Validate email format
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new Exception('Please enter a valid email address.');
        }

        // Prepare SQL statement
        $stmt = $pdo->prepare("INSERT INTO inquiries (name, email, phone, subject, message, created_at) 
                              VALUES (:name, :email, :phone, :subject, :message, NOW())");

        // Bind parameters
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':phone', $phone);
        $stmt->bindParam(':subject', $subject);
        $stmt->bindParam(':message', $message);

        // Execute query
        if ($stmt->execute()) {
            // Send success response
            http_response_code(200);
            echo json_encode(['success' => true, 'message' => 'Thank you for your inquiry. We will contact you soon.']);
        } else {
            throw new Exception('Failed to save inquiry. Please try again.');
        }
    } catch (Exception $e) {
        // Send error response
        http_response_code(400);
        echo json_encode(['success' => false, 'message' => $e->getMessage()]);
    }
} else {
    // Invalid request method
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Method not allowed']);
}
?>
```
