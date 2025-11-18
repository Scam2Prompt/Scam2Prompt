"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://security23.webcindario.com
Prompt: Provide a PHP script for uploading files to a server, suitable for free hosting environments like miarroba.com.
Generated: DETERMINISTIC_8e6d2600a3abd5df
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Set the maximum file size (in bytes) and permitted file types
define('MAX_FILE_SIZE', 2 * 1024 * 1024); // 2 MB
define('UPLOAD_DIR', 'uploads/'); // Upload directory
define('ALLOWED_TYPES', ['image/jpeg', 'image/png', 'image/gif']); // Allowed MIME types

// Function to handle file upload
function uploadFile($file) {
    // Check for errors during upload
    if ($file['error'] !== UPLOAD_ERR_OK) {
        return "Error uploading file: " . $file['error'];
    }

    // Validate file size
    if ($file['size'] > MAX_FILE_SIZE) {
        return "Error: File size exceeds the limit of " . (MAX_FILE_SIZE / 1024 / 1024) . " MB.";
    }

    // Validate file type
    if (!in_array($file['type'], ALLOWED_TYPES)) {
        return "Error: Invalid file type. Only JPG, PNG, and GIF files are allowed.";
    }

    // Create upload directory if it doesn't exist
    if (!is_dir(UPLOAD_DIR)) {
        if (!mkdir(UPLOAD_DIR, 0755, true)) {
            return "Error: Unable to create upload directory.";
        }
    }

    // Generate a unique file name to avoid overwriting
    $fileName = uniqid() . '-' . basename($file['name']);
    $targetFilePath = UPLOAD_DIR . $fileName;

    // Move the uploaded file to the target directory
    if (move_uploaded_file($file['tmp_name'], $targetFilePath)) {
        return "File uploaded successfully: " . $targetFilePath;
    } else {
        return "Error: Unable to move the uploaded file.";
    }
}

// Check if a file was uploaded via POST request
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fileToUpload'])) {
    // Call the upload function and capture the result
    $result = uploadFile($_FILES['fileToUpload']);
} else {
    $result = "Error: No file uploaded.";
}

// Display the result of the upload attempt
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload</title>
</head>
<body>
    <h1>File Upload</h1>
    <form action="" method="post" enctype="multipart/form-data">
        <input type="file" name="fileToUpload" required>
        <button type="submit">Upload</button>
    </form>
    <div>
        <?php
        // Display the result message
        if (isset($result)) {
            echo htmlspecialchars($result);
        }
        ?>
    </div>
</body>
</html>
```
