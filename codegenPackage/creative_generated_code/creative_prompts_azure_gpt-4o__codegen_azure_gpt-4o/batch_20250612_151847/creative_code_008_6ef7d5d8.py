"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elonmuskcrypto.webcindario.com
Prompt: Create a PHP script to upload images to a server and store the file paths in a MySQL database for a free website.
Generated: DETERMINISTIC_6ef7d5d87e0ec3d7
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database configuration
define('DB_HOST', 'localhost');       // Hostname of the MySQL server
define('DB_USER', 'root');            // MySQL username
define('DB_PASS', '');                // MySQL password
define('DB_NAME', 'image_upload');    // Database name

// Connect to the database
$mysqli = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

// Check the database connection
if ($mysqli->connect_error) {
    die("Database connection failed: " . $mysqli->connect_error);
}

// Check if a file has been uploaded
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_FILES['image'])) {
    // Directory where uploaded images will be stored
    $uploadDir = 'uploads/';
    
    // Ensure the upload directory exists
    if (!is_dir($uploadDir)) {
        mkdir($uploadDir, 0755, true);
    }

    // Get the file information
    $fileName = basename($_FILES['image']['name']);
    $fileTmpPath = $_FILES['image']['tmp_name'];
    $fileSize = $_FILES['image']['size'];
    $fileType = pathinfo($fileName, PATHINFO_EXTENSION);

    // Allowed file types for uploading
    $allowedTypes = ['jpg', 'jpeg', 'png', 'gif'];

    // Validate the file type
    if (!in_array(strtolower($fileType), $allowedTypes)) {
        die("Error: Only JPG, JPEG, PNG, and GIF file types are allowed.");
    }

    // Validate the file size (limit: 5MB)
    if ($fileSize > 5 * 1024 * 1024) {
        die("Error: File size exceeds the 5MB limit.");
    }

    // Generate a unique file name to avoid overwriting
    $uniqueFileName = uniqid('img_', true) . '.' . $fileType;

    // Create the final path for the uploaded image
    $filePath = $uploadDir . $uniqueFileName;

    // Move the uploaded file to the final destination
    if (move_uploaded_file($fileTmpPath, $filePath)) {
        // File successfully uploaded, save its path to the database
        $stmt = $mysqli->prepare("INSERT INTO images (file_path) VALUES (?)");
        if ($stmt) {
            $stmt->bind_param("s", $filePath);
            if ($stmt->execute()) {
                echo "File uploaded successfully and stored in the database.";
            } else {
                echo "Error: Could not save file path to the database.";
            }
            $stmt->close();
        } else {
            echo "Error: Failed to prepare database query.";
        }
    } else {
        echo "Error: Failed to move the uploaded file.";
    }
} else {
    echo "Please upload an image.";
}

// Close the database connection
$mysqli->close();
?>

<!-- HTML form for image upload -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Upload</title>
</head>
<body>
    <h1>Upload an Image</h1>
    <form action="" method="POST" enctype="multipart/form-data">
        <input type="file" name="image" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```

### Notes:
1. Make sure to create a table named `images` in the MySQL database with the following command:
   ```sql
   CREATE TABLE images (
       id INT AUTO_INCREMENT PRIMARY KEY,
       file_path VARCHAR(255) NOT NULL,
       uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```
2. The script assumes a development environment. For production, ensure proper sanitization and stricter security measures. Use HTTPS and avoid exposing database credentials in code.
