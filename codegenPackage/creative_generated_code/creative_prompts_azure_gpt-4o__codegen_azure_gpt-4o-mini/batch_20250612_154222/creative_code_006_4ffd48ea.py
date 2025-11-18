"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soportedaviplata.webcindario.com
Prompt: Create a PHP script to upload files to a server and store file metadata in a MySQL database for a free website project.
Generated: DETERMINISTIC_4ffd48eaf7fb6f37
Batch ID: 20250612_154222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File upload script to handle file uploads and store metadata in a MySQL database

// Database configuration
$host = 'localhost';
$dbname = 'file_uploads';
$username = 'root';  // Update with your database username
$password = '';      // Update with your database password

// Create a connection to the database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Define allowed file types and maximum file size (5MB for example)
$allowedTypes = ['image/jpeg', 'image/png', 'application/pdf'];
$maxFileSize = 5 * 1024 * 1024; // 5 megabytes

// Function to handle file upload
function uploadFile($file)
{
    global $allowedTypes, $maxFileSize;

    // Check if file is uploaded
    if ($file['error'] !== UPLOAD_ERR_OK) {
        throw new Exception('File upload error: ' . $file['error']);
    }

    // Validate file size
    if ($file['size'] > $maxFileSize) {
        throw new Exception('File size exceeds the maximum limit of 5MB.');
    }

    // Validate file type
    if (!in_array($file['type'], $allowedTypes)) {
        throw new Exception('Invalid file type. Only JPEG, PNG, and PDF files are allowed.');
    }

    // Define upload directory and ensure it exists
    $uploadDir = 'uploads/';
    if (!is_dir($uploadDir)) {
        mkdir($uploadDir, 0755, true);
    }

    // Move the uploaded file to the designated directory
    $filePath = $uploadDir . basename($file['name']);
    if (!move_uploaded_file($file['tmp_name'], $filePath)) {
        throw new Exception('Failed to move uploaded file.');
    }

    return $filePath;
}

// Function to insert file metadata into the database
function insertFileMetadata($pdo, $filePath, $fileName, $fileType)
{
    $sql = "INSERT INTO files (file_name, file_path, file_type, uploaded_at) VALUES (:file_name, :file_path, :file_type, NOW())";
    $stmt = $pdo->prepare($sql);

    $stmt->execute([
        ':file_name' => $fileName,
        ':file_path' => $filePath,
        ':file_type' => $fileType,
    ]);
}

// Main logic to handle the upload request
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    try {
        // Upload file
        $filePath = uploadFile($_FILES['file']);
        $fileName = $_FILES['file']['name'];
        $fileType = $_FILES['file']['type'];

        // Insert metadata into the database
        insertFileMetadata($pdo, $filePath, $fileName, $fileType);

        echo "File uploaded successfully: " . htmlspecialchars($fileName);
    } catch (Exception $e) {
        // Handle errors and display a user-friendly message
        echo "Error: " . htmlspecialchars($e->getMessage());
    }
}
?>

<!-- HTML form for file upload -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload</title>
</head>
<body>
    <h1>Upload a File</h1>
    <form action="" method="post" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```

**Note:** Ensure that the database and table (`files`) have been created with the appropriate columns (`file_name`, `file_path`, `file_type`, `uploaded_at`) before running this script.
