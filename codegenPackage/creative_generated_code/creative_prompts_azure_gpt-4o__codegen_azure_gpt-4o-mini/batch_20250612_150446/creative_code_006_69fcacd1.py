"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artorvias.com
Prompt: Generate code in PHP to upload a 3D artwork to the Artorvia platform, including functionality to add a title, description, and customize properties and stats.
Generated: DETERMINISTIC_69fcacd1b7c3a313
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// upload_artwork.php

/**
 * Handles the upload of a 3D artwork to the Artorvia platform.
 * 
 * This script processes the uploaded file, saves it to the server, 
 * and records the artwork details in the database.
 */

require 'config.php'; // Include database configuration

// Define constants for maximum file size and allowed file types
define('MAX_FILE_SIZE', 10 * 1024 * 1024); // 10 MB
define('ALLOWED_FILE_TYPES', ['model/gltf+json', 'model/vnd.gltf+json', 'application/octet-stream']);

// Check if the form has been submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate and sanitize input data
    $title = htmlspecialchars(trim($_POST['title']));
    $description = htmlspecialchars(trim($_POST['description']));
    $customProperties = htmlspecialchars(trim($_POST['custom_properties']));

    // Validate file upload
    if (isset($_FILES['artwork']) && $_FILES['artwork']['error'] === UPLOAD_ERR_OK) {
        $fileTmpPath = $_FILES['artwork']['tmp_name'];
        $fileName = $_FILES['artwork']['name'];
        $fileSize = $_FILES['artwork']['size'];
        $fileType = $_FILES['artwork']['type'];
        $fileNameCmps = explode(".", $fileName);
        $fileExtension = strtolower(end($fileNameCmps));

        // Check file size
        if ($fileSize > MAX_FILE_SIZE) {
            die("Error: File size exceeds the maximum limit of 10 MB.");
        }

        // Check file type
        if (!in_array($fileType, ALLOWED_FILE_TYPES)) {
            die("Error: Invalid file type. Allowed types are: " . implode(", ", ALLOWED_FILE_TYPES));
        }

        // Define the upload directory and move the file
        $uploadFileDir = 'uploads/';
        $destPath = $uploadFileDir . uniqid() . '-' . $fileName;

        if (move_uploaded_file($fileTmpPath, $destPath)) {
            // Prepare SQL statement to insert artwork details into the database
            $query = "INSERT INTO artworks (title, description, file_path, custom_properties) VALUES (:title, :description, :file_path, :custom_properties)";
            $stmt = $pdo->prepare($query);

            // Bind parameters
            $stmt->bindParam(':title', $title);
            $stmt->bindParam(':description', $description);
            $stmt->bindParam(':file_path', $destPath);
            $stmt->bindParam(':custom_properties', $customProperties);

            // Execute the query and handle any errors
            try {
                $stmt->execute();
                echo "Artwork uploaded successfully!";
            } catch (PDOException $e) {
                die("Error: Unable to upload artwork. " . $e->getMessage());
            }
        } else {
            die("Error: There was an error moving the uploaded file.");
        }
    } else {
        die("Error: " . $_FILES['artwork']['error']);
    }
} else {
    die("Error: Invalid request method.");
}
?>
```

```html
<!-- upload_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload 3D Artwork</title>
</head>
<body>
    <h1>Upload 3D Artwork</h1>
    <form action="upload_artwork.php" method="POST" enctype="multipart/form-data">
        <label for="title">Title:</label>
        <input type="text" name="title" required>
        <br>
        <label for="description">Description:</label>
        <textarea name="description" required></textarea>
        <br>
        <label for="custom_properties">Custom Properties:</label>
        <input type="text" name="custom_properties">
        <br>
        <label for="artwork">Upload 3D Model:</label>
        <input type="file" name="artwork" accept=".gltf,.glb" required>
        <br>
        <input type="submit" value="Upload Artwork">
    </form>
</body>
</html>
``` 

Make sure to create a `config.php` file containing the database connection setup using PDO.
