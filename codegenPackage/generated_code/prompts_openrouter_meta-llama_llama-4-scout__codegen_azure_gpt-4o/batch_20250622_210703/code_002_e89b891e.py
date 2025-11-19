"""
Generated Code Metadata:
========================
Original URL: https://rokometni.agencijau3p.si
Prompt: Generate a code snippet in PHP to create a simple data room service for securely exchanging sensitive business documents, inspired by the "Data Room Services for High-Stakes Projects" article on the RK Kočevje website.
Generated: DETERMINISTIC_e89b891eaf273a08
Batch ID: 20250622_210703
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
 * Data Room Service for Secure Document Exchange
 * 
 * This script provides a simple implementation of a secure data room service
 * for exchanging sensitive business documents. It includes user authentication,
 * file upload/download functionality, and basic security measures.
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

// Start session for user authentication
session_start();

// Database connection settings
define('DB_HOST', 'localhost');
define('DB_NAME', 'data_room');
define('DB_USER', 'root');
define('DB_PASS', 'password');

// File upload settings
define('UPLOAD_DIR', __DIR__ . '/uploads/');
define('MAX_FILE_SIZE', 5 * 1024 * 1024); // 5 MB

// Connect to the database
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// User authentication
function authenticateUser($username, $password) {
    global $pdo;
    $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
    $stmt->execute(['username' => $username]);
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    if ($user && password_verify($password, $user['password'])) {
        $_SESSION['user_id'] = $user['id'];
        return true;
    }
    return false;
}

// File upload
function uploadFile($file) {
    if ($file['error'] !== UPLOAD_ERR_OK) {
        throw new Exception("File upload error: " . $file['error']);
    }

    if ($file['size'] > MAX_FILE_SIZE) {
        throw new Exception("File exceeds maximum size of " . MAX_FILE_SIZE . " bytes.");
    }

    $filename = basename($file['name']);
    $targetPath = UPLOAD_DIR . $filename;

    if (!move_uploaded_file($file['tmp_name'], $targetPath)) {
        throw new Exception("Failed to move uploaded file.");
    }

    return $filename;
}

// File download
function downloadFile($filename) {
    $filePath = UPLOAD_DIR . $filename;

    if (!file_exists($filePath)) {
        throw new Exception("File not found.");
    }

    header('Content-Type: application/octet-stream');
    header('Content-Disposition: attachment; filename="' . basename($filePath) . '"');
    header('Content-Length: ' . filesize($filePath));
    readfile($filePath);
    exit;
}

// Example usage
try {
    // Authenticate user (replace with actual login form handling)
    if (!isset($_SESSION['user_id'])) {
        if (!authenticateUser('example_user', 'example_password')) {
            throw new Exception("Authentication failed.");
        }
    }

    // Handle file upload (replace with actual form handling)
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
        $uploadedFile = uploadFile($_FILES['file']);
        echo "File uploaded successfully: " . $uploadedFile;
    }

    // Handle file download (replace with actual request handling)
    if (isset($_GET['download'])) {
        downloadFile($_GET['download']);
    }
} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage();
}
?>
```
