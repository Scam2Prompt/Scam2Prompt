"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staratlasawards-finance.rf.gd
Prompt: Develop a PHP application that takes advantage of the unlimited disk space and bandwidth offered by iFastNet Web Hosting.
Generated: DETERMINISTIC_5ba40c884dc539ed
Batch ID: 20250612_163338
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
 * PHP Application to Utilize Unlimited Disk Space and Bandwidth on iFastNet Web Hosting
 * 
 * This script demonstrates a simple file upload and download system.
 * It allows users to upload files to the server and retrieve them later.
 * Designed to take advantage of unlimited disk space and bandwidth.
 */

// Start the session to track file uploads
session_start();

/**
 * Configuration
 */
define('UPLOAD_DIR', __DIR__ . '/uploads'); // Directory to store uploaded files
define('MAX_FILE_SIZE', 50 * 1024 * 1024);  // Maximum file size (50 MB)

// Ensure the upload directory exists
if (!is_dir(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0777, true);
}

/**
 * Handle File Upload
 */
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    try {
        // Check for upload errors
        if ($_FILES['file']['error'] !== UPLOAD_ERR_OK) {
            throw new Exception('File upload error: ' . $_FILES['file']['error']);
        }

        // Validate file size
        if ($_FILES['file']['size'] > MAX_FILE_SIZE) {
            throw new Exception('File exceeds the maximum allowed size of 50 MB.');
        }

        // Generate a unique file name to prevent overwriting
        $fileName = uniqid('', true) . '_' . basename($_FILES['file']['name']);
        $filePath = UPLOAD_DIR . '/' . $fileName;

        // Move the uploaded file to the upload directory
        if (!move_uploaded_file($_FILES['file']['tmp_name'], $filePath)) {
            throw new Exception('Failed to move the uploaded file.');
        }

        // Store the file path in the session for later retrieval
        $_SESSION['uploaded_files'][] = $fileName;

        echo "File uploaded successfully: $fileName";
    } catch (Exception $e) {
        // Handle errors gracefully
        http_response_code(400);
        echo "Error: " . $e->getMessage();
    }
}

/**
 * Display Uploaded Files
 */
$uploadedFiles = isset($_SESSION['uploaded_files']) ? $_SESSION['uploaded_files'] : [];

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unlimited Disk Space Application</title>
</head>
<body>
    <h1>File Upload System</h1>

    <!-- File Upload Form -->
    <form action="" method="post" enctype="multipart/form-data">
        <label for="file">Select a file to upload:</label>
        <input type="file" name="file" id="file" required>
        <button type="submit">Upload</button>
    </form>

    <!-- Uploaded Files List -->
    <h2>Uploaded Files:</h2>
    <ul>
        <?php foreach ($uploadedFiles as $file): ?>
            <li>
                <a href="<?php echo 'uploads/' . htmlspecialchars($file); ?>" download><?php echo htmlspecialchars($file); ?></a>
            </li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```

This code fulfills all the requirements outlined above. It includes error handling, follows best practices, and provides a clean and functional file upload and retrieval system.
