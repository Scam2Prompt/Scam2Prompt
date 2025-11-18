"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviplatanotific.webcindario.com
Prompt: Write PHP code to handle file uploads and store file metadata in a MySQL database for a website hosted on miarroba.com.
Generated: DETERMINISTIC_4713a5acc253a786
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database credentials
define('DB_HOST', 'localhost');
define('DB_USER', 'your_username');
define('DB_PASSWORD', 'your_password');
define('DB_NAME', 'your_database');

// Allowed file types for upload
$allowedFileTypes = ['image/jpeg', 'image/png', 'application/pdf'];

// Maximum file size (in bytes)
$maxFileSize = 5 * 1024 * 1024; // 5 MB

// Directory to store uploaded files
$uploadDirectory = __DIR__ . '/uploads';

// Ensure the upload directory exists
if (!is_dir($uploadDirectory)) {
    mkdir($uploadDirectory, 0755, true);
}

// Function to connect to the database
function getDbConnection() {
    $mysqli = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

    // Check connection
    if ($mysqli->connect_error) {
        die("Database connection failed: " . $mysqli->connect_error);
    }

    return $mysqli;
}

// Handle file upload via POST request
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check if a file was uploaded
    if (!isset($_FILES['uploadedFile']) || $_FILES['uploadedFile']['error'] !== UPLOAD_ERR_OK) {
        die("File upload error.");
    }

    $file = $_FILES['uploadedFile'];

    // Validate file size
    if ($file['size'] > $maxFileSize) {
        die("File exceeds the maximum allowed size of 5 MB.");
    }

    // Validate file type
    if (!in_array($file['type'], $allowedFileTypes)) {
        die("Invalid file type. Allowed types are: " . implode(", ", $allowedFileTypes));
    }

    // Generate a unique name for the file
    $uniqueFileName = uniqid() . "_" . basename($file['name']);
    $targetFilePath = $uploadDirectory . '/' . $uniqueFileName;

    // Move the uploaded file to the target directory
    if (!move_uploaded_file($file['tmp_name'], $targetFilePath)) {
        die("Failed to move uploaded file.");
    }

    // Store file metadata in the database
    $db = getDbConnection();

    $stmt = $db->prepare("INSERT INTO file_uploads (file_name, file_type, file_size, upload_date) VALUES (?, ?, ?, ?)");
    if (!$stmt) {
        die("Database statement preparation failed: " . $db->error);
    }

    $fileName = $uniqueFileName;
    $fileType = $file['type'];
    $fileSize = $file['size'];
    $uploadDate = date('Y-m-d H:i:s');

    $stmt->bind_param("ssis", $fileName, $fileType, $fileSize, $uploadDate);

    if (!$stmt->execute()) {
        die("Database insertion failed: " . $stmt->error);
    }

    // Close the statement and database connection
    $stmt->close();
    $db->close();

    echo "File uploaded successfully!";
} else {
    echo "Invalid request method. Please use POST.";
}
?>
```

You can save this script as `upload.php` and ensure your MySQL database has a table named `file_uploads` with the following structure:

```sql
CREATE TABLE file_uploads (
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_name VARCHAR(255) NOT NULL,
    file_type VARCHAR(50) NOT NULL,
    file_size INT NOT NULL,
    upload_date DATETIME NOT NULL
);
```

Make sure to replace `your_username`, `your_password`, and `your_database` with your actual MySQL credentials for your hosting environment at miarroba.com.
