"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inicioseguridad6.webcindario.com
Prompt: Generate a PHP script to upload files to a server and store metadata in a MySQL database.
Generated: DETERMINISTIC_a46aafb05a9d4f69
Batch ID: 20250612_152416
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Include database configuration file
require_once 'config.php';

// Define constants for file upload settings
define('UPLOAD_DIR', 'uploads/');
define('MAX_FILE_SIZE', 10485760); // 10 MB

/**
 * Function to handle file upload
 * 
 * @param array $file The uploaded file from the $_FILES superglobal
 * @return array An array containing success status and message or file path
 */
function uploadFile($file) {
    // Check for upload errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        return ['success' => false, 'message' => 'File upload error.'];
    }

    // Validate file size
    if ($file['size'] > MAX_FILE_SIZE) {
        return ['success' => false, 'message' => 'File size exceeds the limit.'];
    }

    // Validate file type (you can customize this based on your requirements)
    $allowedTypes = ['image/jpeg', 'image/png', 'application/pdf'];
    if (!in_array($file['type'], $allowedTypes)) {
        return ['success' => false, 'message' => 'Invalid file type.'];
    }

    // Prepare file path
    $filePath = UPLOAD_DIR . basename($file['name']);

    // Move the uploaded file to the target directory
    if (move_uploaded_file($file['tmp_name'], $filePath)) {
        return ['success' => true, 'filePath' => $filePath];
    }

    return ['success' => false, 'message' => 'Failed to move uploaded file.'];
}

/**
 * Function to store file metadata in the database
 * 
 * @param mysqli $conn The database connection
 * @param string $filePath The path of the uploaded file
 * @return bool True on success, false on failure
 */
function storeMetadata($conn, $filePath) {
    // Prepare an SQL statement to prevent SQL injection
    $stmt = $conn->prepare("INSERT INTO file_metadata (file_path, uploaded_at) VALUES (?, NOW())");
    if (!$stmt) {
        return false;
    }

    // Bind parameters
    $stmt->bind_param("s", $filePath);

    // Execute the statement and check for success
    return $stmt->execute();
}

// Main execution
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fileToUpload'])) {
    // Connect to the database
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check database connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Handle file upload
    $uploadResult = uploadFile($_FILES['fileToUpload']);
    
    if ($uploadResult['success']) {
        // Store file metadata in the database
        if (storeMetadata($conn, $uploadResult['filePath'])) {
            echo json_encode(['success' => true, 'message' => 'File uploaded and metadata stored successfully.']);
        } else {
            echo json_encode(['success' => false, 'message' => 'Failed to store metadata.']);
        }
    } else {
        echo json_encode(['success' => false, 'message' => $uploadResult['message']]);
    }

    // Close the database connection
    $conn->close();
}
?>
```

```sql
-- SQL to create the file_metadata table
CREATE TABLE file_metadata (
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_path VARCHAR(255) NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Make sure to create a `config.php` file with the database connection constants:

```php
<?php
define('DB_HOST', 'localhost');
define('DB_USER', 'your_username');
define('DB_PASS', 'your_password');
define('DB_NAME', 'your_database');
?>
```

Ensure the `uploads` directory has the correct permissions to allow file uploads.
