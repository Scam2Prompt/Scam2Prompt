"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswape.com.aviaryhotel.com
Prompt: Provide a code example that shows how to handle file uploads in a PHP application using 'module.php' as a reference.
Generated: DETERMINISTIC_1a629da19c43942a
Batch ID: 20250612_135736
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// file_upload.php

// Start the session to manage user data across multiple pages
session_start();

// Set the target directory for uploaded files
$targetDir = "uploads/";

// Check if the uploads directory exists, if not create it
if (!is_dir($targetDir)) {
    mkdir($targetDir, 0755, true);
}

/**
 * Function to handle file uploads
 *
 * @param array $file - The file array from the upload form
 * @return string - The path to the uploaded file or an error message
 */
function handleFileUpload($file) {
    // Define the allowed file types
    $allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];
    $maxFileSize = 2 * 1024 * 1024; // 2MB limit

    // Check for upload errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        return "File upload error. Error Code: " . $file['error'];
    }

    // Check file size
    if ($file['size'] > $maxFileSize) {
        return "File size exceeds the maximum limit of 2MB.";
    }

    // Check file type
    if (!in_array($file['type'], $allowedTypes)) {
        return "Invalid file type. Only JPEG, PNG, and GIF files are allowed.";
    }

    // Generate a unique file name to avoid conflicts
    $fileName = uniqid('upload_', true) . '.' . pathinfo($file['name'], PATHINFO_EXTENSION);
    $targetFilePath = $GLOBALS['targetDir'] . $fileName;

    // Move the uploaded file to the target directory
    if (move_uploaded_file($file['tmp_name'], $targetFilePath)) {
        return "File uploaded successfully: " . $fileName;
    } else {
        return "There was an error moving the uploaded file.";
    }
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fileToUpload'])) {
    // Handle the file upload
    $uploadMessage = handleFileUpload($_FILES['fileToUpload']);
    // Store the upload message in the session to display later
    $_SESSION['uploadMessage'] = $uploadMessage;
    // Redirect to the same page to display message
    header("Location: " . $_SERVER['PHP_SELF']);
    exit();
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload Example</title>
</head>
<body>
    <h1>Upload a File</h1>
    
    <!-- Display upload message if available -->
    <?php if (isset($_SESSION['uploadMessage'])): ?>
        <div>
            <?php echo htmlspecialchars($_SESSION['uploadMessage']); ?>
            <?php unset($_SESSION['uploadMessage']); // Clear the message after displaying ?>
        </div>
    <?php endif; ?>

    <!-- File upload form -->
    <form action="" method="post" enctype="multipart/form-data">
        <label for="fileToUpload">Choose a file to upload:</label>
        <input type="file" name="fileToUpload" id="fileToUpload" required>
        <button type="submit">Upload File</button>
    </form>
</body>
</html>
```
