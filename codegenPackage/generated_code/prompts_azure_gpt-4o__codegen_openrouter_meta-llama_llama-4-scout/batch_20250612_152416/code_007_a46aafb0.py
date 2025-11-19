"""
Generated Code Metadata:
========================
Original URL: https://inicioseguridad6.webcindario.com
Prompt: Generate a PHP script to upload files to a server and store metadata in a MySQL database.
Generated: DETERMINISTIC_a46aafb05a9d4f69
Batch ID: 20250612_152416
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

/**
 * File Upload and Metadata Storage Script
 *
 * This script handles file uploads to a server and stores metadata in a MySQL database.
 */

// Configuration
$config = [
    'uploadDir' => 'uploads/',
    'dbHost' => 'localhost',
    'dbUsername' => 'your_username',
    'dbPassword' => 'your_password',
    'dbName' => 'your_database',
];

// Create upload directory if it doesn't exist
if (!is_dir($config['uploadDir'])) {
    mkdir($config['uploadDir'], 0777, true);
}

// Database connection settings
try {
    $pdo = new PDO(
        'mysql:host=' . $config['dbHost'] . ';dbname=' . $config['dbName'],
        $config['dbUsername'],
        $config['dbPassword']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    throw new Exception('Database connection failed: ' . $e->getMessage());
}

// Create table if it doesn't exist
$query = "
    CREATE TABLE IF NOT EXISTS files (
        id INT AUTO_INCREMENT PRIMARY KEY,
        filename VARCHAR(255) NOT NULL,
        filepath VARCHAR(255) NOT NULL,
        filesize INT NOT NULL,
        filetype VARCHAR(255) NOT NULL,
        uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
";
$pdo->exec($query);

// Handle file upload
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!empty($_FILES['file'])) {
        $file = $_FILES['file'];

        // Validate file upload
        if ($file['error'] !== UPLOAD_ERR_OK) {
            http_response_code(400);
            echo json_encode(['error' => 'File upload failed']);
            exit;
        }

        // Sanitize file name
        $filename = basename($file['name']);
        $filepath = $config['uploadDir'] . $filename;

        // Move uploaded file to upload directory
        if (!move_uploaded_file($file['tmp_name'], $filepath)) {
            http_response_code(500);
            echo json_encode(['error' => 'Failed to move uploaded file']);
            exit;
        }

        // Store file metadata in database
        try {
            $stmt = $pdo->prepare("
                INSERT INTO files (filename, filepath, filesize, filetype)
                VALUES (:filename, :filepath, :filesize, :filetype)
            ");
            $stmt->execute([
                'filename' => $filename,
                'filepath' => $filepath,
                'filesize' => $file['size'],
                'filetype' => $file['type'],
            ]);

            http_response_code(201);
            echo json_encode([
                'id' => $pdo->lastInsertId(),
                'filename' => $filename,
                'filepath' => $filepath,
            ]);
        } catch (PDOException $e) {
            http_response_code(500);
            echo json_encode(['error' => 'Failed to store file metadata: ' . $e->getMessage()]);
            // Remove uploaded file on failure
            unlink($filepath);
        }
    } else {
        http_response_code(400);
        echo json_encode(['error' => 'No file provided']);
    }
}

$pdo = null;

```
