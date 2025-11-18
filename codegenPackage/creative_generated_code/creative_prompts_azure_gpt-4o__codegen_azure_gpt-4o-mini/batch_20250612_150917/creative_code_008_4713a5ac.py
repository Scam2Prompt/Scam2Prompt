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
// Start the session to manage user state
session_start();

// Database connection parameters
$host = 'localhost'; // Database host
$db = 'your_database_name'; // Database name
$user = 'your_database_user'; // Database user
$pass = 'your_database_password'; // Database password

// Create a connection to the MySQL database
$conn = new mysqli($host, $user, $pass, $db);

// Check for connection errors
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to handle file uploads
function handleFileUpload($file) {
    // Specify the directory to store uploaded files
    $targetDir = "uploads/";
    // Get the file extension
    $fileType = pathinfo($file['name'], PATHINFO_EXTENSION);
    // Generate a unique name for the file
    $fileName = uniqid() . '.' . $fileType;
    // Specify the target file path
    $targetFilePath = $targetDir . $fileName;

    // Check for upload errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        throw new Exception("File upload error: " . $file['error']);
    }

    // Validate the file type (for example, allow only images)
    $allowedTypes = ['jpg', 'jpeg', 'png', 'gif'];
    if (!in_array($fileType, $allowedTypes)) {
        throw new Exception("Invalid file type. Allowed types: " . implode(", ", $allowedTypes));
    }

    // Move the uploaded file to the target directory
    if (!move_uploaded_file($file['tmp_name'], $targetFilePath)) {
        throw new Exception("Failed to move uploaded file.");
    }

    return $fileName;
}

// Function to store file metadata in the database
function storeFileMetadata($conn, $fileName, $fileType) {
    // Prepare the SQL statement to insert metadata
    $stmt = $conn->prepare("INSERT INTO file_metadata (file_name, file_type, upload_time) VALUES (?, ?, NOW())");
    // Bind parameters to the SQL statement
    $stmt->bind_param("ss", $fileName, $fileType);

    // Execute the statement and check for errors
    if (!$stmt->execute()) {
        throw new Exception("Database error: " . $stmt->error);
    }

    // Close the statement
    $stmt->close();
}

// Main logic to handle file upload
try {
    // Check if a file has been uploaded
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fileToUpload'])) {
        // Handle the file upload
        $fileName = handleFileUpload($_FILES['fileToUpload']);
        // Store the file metadata in the database
        storeFileMetadata($conn, $fileName, $_FILES['fileToUpload']['type']);
        // Redirect or inform the user of success
        echo "File uploaded successfully: " . htmlspecialchars($fileName);
    }
} catch (Exception $e) {
    // Handle exceptions and display the error message
    echo "Error: " . htmlspecialchars($e->getMessage());
}

// Close the database connection
$conn->close();
?>

<!-- HTML Form for file upload -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>File Upload</title>
</head>
<body>
    <h2>Upload a File</h2>
    <form action="" method="post" enctype="multipart/form-data">
        <input type="file" name="fileToUpload" required>
        <input type="submit" value="Upload">
    </form>
</body>
</html>
```
