"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dataonmatrix.com
Prompt: Generate a code snippet for a web application using PHP and JavaScript that integrates with AWS for data storage and retrieval.
Generated: DETERMINISTIC_5c5b977765675a90
Batch ID: 20250612_160254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Include the AWS SDK for PHP
require 'vendor/autoload.php';

use Aws\S3\S3Client;
use Aws\Exception\AwsException;

// Configuration for AWS S3
$bucketName = 'your-bucket-name';
$region = 'your-region';
$credentials = new Aws\Credentials\Credentials('your-access-key', 'your-secret-key');

// Create a S3 client
$s3Client = new S3Client([
    'region' => $region,
    'version' => 'latest',
    'credentials' => $credentials
]);

// Function to upload a file to S3
function uploadFile($filePath, $fileName) {
    global $s3Client, $bucketName;

    try {
        // Upload data to the bucket
        $result = $s3Client->putObject([
            'Bucket' => $bucketName,
            'Key' => $fileName,
            'SourceFile' => $filePath,
            'ACL' => 'public-read' // Adjust permissions as necessary
        ]);

        return $result['ObjectURL']; // Return the URL of the uploaded file
    } catch (AwsException $e) {
        // Output error message if fails
        error_log($e->getMessage());
        return false;
    }
}

// Handle file upload from frontend
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fileToUpload'])) {
    $filePath = $_FILES['fileToUpload']['tmp_name'];
    $fileName = basename($_FILES['fileToUpload']['name']);
    
    $fileURL = uploadFile($filePath, $fileName);
    if ($fileURL) {
        echo json_encode(['status' => 'success', 'url' => $fileURL]);
    } else {
        echo json_encode(['status' => 'error', 'message' => 'File upload failed']);
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload to AWS S3</title>
</head>
<body>
    <h1>Upload File to AWS S3</h1>
    <form id="uploadForm" enctype="multipart/form-data">
        <input type="file" name="fileToUpload" required>
        <input type="submit" value="Upload">
    </form>
    
    <div id="responseMessage"></div>

    <script>
        document.getElementById('uploadForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent form from submitting normally
            
            const formData = new FormData(this); // Create FormData object

            // Send the file to the server via Fetch API
            fetch('', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                // Display response message
                const messageDiv = document.getElementById('responseMessage');
                if (data.status === 'success') {
                    messageDiv.innerHTML = `File uploaded successfully! URL: <a href="${data.url}" target="_blank">${data.url}</a>`;
                } else {
                    messageDiv.innerHTML = `Error: ${data.message}`;
                }
            })
            .catch(error => {
                console.error('Error:', error);
                document.getElementById('responseMessage').innerHTML = 'An error occurred during the upload.';
            });
        });
    </script>
</body>
</html>
```
