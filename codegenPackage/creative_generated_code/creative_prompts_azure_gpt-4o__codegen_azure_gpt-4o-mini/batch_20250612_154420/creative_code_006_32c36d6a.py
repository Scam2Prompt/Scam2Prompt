"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://credidavivienta.webcindario.com
Prompt: Create a PHP script to upload and retrieve files from a MySQL database, suitable for a free website setup similar to the one described.
Generated: DETERMINISTIC_32c36d6a158b6161
Batch ID: 20250612_154420
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
$host = 'localhost'; // Database host
$dbname = 'file_upload_db'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

// Create a connection to the database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}

// Handle file upload
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fileToUpload'])) {
    // Validate file upload
    $file = $_FILES['fileToUpload'];
    $fileName = $file['name'];
    $fileTmpName = $file['tmp_name'];
    $fileSize = $file['size'];
    $fileError = $file['error'];
    $fileType = $file['type'];

    // Check for upload errors
    if ($fileError !== 0) {
        die("Error uploading file.");
    }

    // Limit file size to 2MB
    if ($fileSize > 2000000) {
        die("File size exceeds 2MB limit.");
    }

    // Prepare the SQL statement
    $stmt = $pdo->prepare("INSERT INTO files (file_name, file_data) VALUES (:file_name, :file_data)");

    // Read file contents
    $fileData = file_get_contents($fileTmpName);

    // Bind parameters and execute the statement
    $stmt->bindParam(':file_name', $fileName);
    $stmt->bindParam(':file_data', $fileData, PDO::PARAM_LOB);

    if ($stmt->execute()) {
        echo "File uploaded successfully.";
    } else {
        echo "Failed to upload file.";
    }
}

// Retrieve files from the database
$files = [];
try {
    $stmt = $pdo->query("SELECT id, file_name FROM files");
    $files = $stmt->fetchAll(PDO::FETCH_ASSOC);
} catch (PDOException $e) {
    die("Error fetching files: " . $e->getMessage());
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload and Retrieve</title>
</head>
<body>
    <h1>Upload a File</h1>
    <form action="" method="POST" enctype="multipart/form-data">
        <input type="file" name="fileToUpload" required>
        <button type="submit">Upload</button>
    </form>

    <h2>Uploaded Files</h2>
    <ul>
        <?php foreach ($files as $file): ?>
            <li>
                <a href="download.php?id=<?= htmlspecialchars($file['id']) ?>">
                    <?= htmlspecialchars($file['file_name']) ?>
                </a>
            </li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```

```php
<?php
// download.php - Script to download files from the database

// Database configuration
$host = 'localhost'; // Database host
$dbname = 'file_upload_db'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

// Create a connection to the database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}

// Handle file download
if (isset($_GET['id'])) {
    $fileId = (int)$_GET['id']; // Sanitize input

    // Prepare the SQL statement to fetch the file
    $stmt = $pdo->prepare("SELECT file_name, file_data FROM files WHERE id = :id");
    $stmt->bindParam(':id', $fileId, PDO::PARAM_INT);

    if ($stmt->execute()) {
        $file = $stmt->fetch(PDO::FETCH_ASSOC);
        if ($file) {
            // Set headers for download
            header('Content-Type: application/octet-stream');
            header('Content-Disposition: attachment; filename="' . $file['file_name'] . '"');
            echo $file['file_data'];
            exit;
        } else {
            die("File not found.");
        }
    } else {
        die("Error retrieving file.");
    }
} else {
    die("No file specified.");
}
?>
```

### Database Schema
To use the above PHP scripts, create a MySQL database named `file_upload_db` and run the following SQL to create the `files` table:

```sql
CREATE TABLE files (
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_name VARCHAR(255) NOT NULL,
    file_data LONGBLOB NOT NULL
);
``` 

This code provides a basic file upload and retrieval system with error handling, suitable for a free website setup.
