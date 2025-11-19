"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webautomigrate.hstn.me
Prompt: Create a PHP application that takes advantage of the unlimited disk space offered by iFastNet for file storage.
Generated: DETERMINISTIC_9004c8d11063ac09
Batch ID: 20250612_155401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File: FileStorage.php

/**
 * A simple PHP application for managing file uploads to unlimited disk space
 * offered by iFastNet.
 */
class FileStorage
{
    private $uploadDir;

    // Constructor to set the upload directory
    public function __construct($uploadDir)
    {
        // Set the upload directory and create it if it doesn't exist
        $this->uploadDir = rtrim($uploadDir, '/') . '/';
        if (!is_dir($this->uploadDir) && !mkdir($this->uploadDir, 0755, true)) {
            throw new Exception("Failed to create upload directory: " . $this->uploadDir);
        }
    }

    /**
     * Handle file upload from the HTTP POST request.
     *
     * @return void
     * @throws Exception When upload fails
     */
    public function uploadFile()
    {
        // Check if the file was uploaded without errors
        if (isset($_FILES['fileToUpload']) && $_FILES['fileToUpload']['error'] == UPLOAD_ERR_OK) {
            $fileTmpPath = $_FILES['fileToUpload']['tmp_name'];
            $fileName = basename($_FILES['fileToUpload']['name']);
            $destPath = $this->uploadDir . $fileName;

            // Move the uploaded file to the destination directory
            if (!move_uploaded_file($fileTmpPath, $destPath)) {
                throw new Exception("Error moving uploaded file to destination");
            }

            echo "File uploaded successfully: " . htmlspecialchars($fileName);
        } else {
            throw new Exception("File upload error: " . $_FILES['fileToUpload']['error']);
        }
    }
}

// Entry point of the application
try {
    // Set the directory for uploads, make sure to change this to your desired path
    $uploadDirectory = __DIR__ . '/uploads';
    $fileStorage = new FileStorage($uploadDirectory);

    // Check for a POST request to handle file upload
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $fileStorage->uploadFile();
    }
} catch (Exception $e) {
    // Handle exceptions and display error messages
    echo "Error: " . htmlspecialchars($e->getMessage());
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
    <h1>File Upload</h1>
    <form action="" method="post" enctype="multipart/form-data">
        <label for="fileToUpload">Select file to upload:</label>
        <input type="file" name="fileToUpload" id="fileToUpload" required>
        <input type="submit" value="Upload File">
    </form>
</body>
</html>
```

### Instructions for Running the Code
1. Save the PHP code in a file named `FileStorage.php`.
2. Ensure the server environment supports PHP and has access to the filesystem.
3. Access the script via a web browser, and use the provided form to upload files.
4. Files will be saved in the `uploads` directory relative to the script's location.
