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
define('DB_HOST', 'localhost'); // Replace with your database host
define('DB_USER', 'root'); // Replace with your database username
define('DB_PASS', ''); // Replace with your database password
define('DB_NAME', 'file_storage'); // Replace with your database name

/**
 * Connects to the MySQL database.
 * Returns a PDO object or exits on failure.
 */
function connectDatabase()
{
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        exit("Database connection failed: " . $e->getMessage());
    }
}

// Handle file upload
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    try {
        $pdo = connectDatabase();

        // Validate uploaded file
        if ($_FILES['file']['error'] !== UPLOAD_ERR_OK) {
            throw new Exception('File upload error.');
        }

        $fileName = $_FILES['file']['name'];
        $fileType = $_FILES['file']['type'];
        $fileData = file_get_contents($_FILES['file']['tmp_name']);

        // Insert file into the database
        $stmt = $pdo->prepare("INSERT INTO files (name, type, data) VALUES (:name, :type, :data)");
        $stmt->bindParam(':name', $fileName);
        $stmt->bindParam(':type', $fileType);
        $stmt->bindParam(':data', $fileData, PDO::PARAM_LOB);

        if ($stmt->execute()) {
            echo "File uploaded successfully.";
        } else {
            throw new Exception('Failed to upload file.');
        }
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage();
    }
}

// Handle file retrieval
if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['id'])) {
    try {
        $pdo = connectDatabase();

        $fileId = intval($_GET['id']); // Sanitize input
        $stmt = $pdo->prepare("SELECT name, type, data FROM files WHERE id = :id");
        $stmt->bindParam(':id', $fileId, PDO::PARAM_INT);
        $stmt->execute();

        if ($stmt->rowCount() === 1) {
            $file = $stmt->fetch(PDO::FETCH_ASSOC);

            // Return the file to the browser
            header("Content-Type: " . $file['type']);
            header("Content-Disposition: attachment; filename=\"" . $file['name'] . "\"");
            echo $file['data'];
            exit;
        } else {
            throw new Exception('File not found.');
        }
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage();
    }
}
?>

<!-- HTML Form for file upload -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload</title>
</head>
<body>
    <h1>Upload a File</h1>
    <form action="upload.php" method="POST" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Upload</button>
    </form>

    <h1>Retrieve a File</h1>
    <form action="upload.php" method="GET">
        <label for="file-id">File ID: </label>
        <input type="text" id="file-id" name="id" required>
        <button type="submit">Retrieve</button>
    </form>
</body>
</html>

<?php
// SQL schema for the 'files' table
// CREATE TABLE `files` (
//     `id` INT AUTO_INCREMENT PRIMARY KEY,
//     `name` VARCHAR(255) NOT NULL,
//     `type` VARCHAR(50) NOT NULL,
//     `data` LONGBLOB NOT NULL,
//     `uploaded_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
// );
?>
```
