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

### PHP Backend Code (AWS S3 Integration for Data Storage and Retrieval)

```php
<?php
// Include AWS SDK for PHP
require 'vendor/autoload.php';

use Aws\S3\S3Client;
use Aws\Exception\AwsException;

// AWS Configuration
define('AWS_REGION', 'us-east-1'); // Replace with your desired region
define('AWS_ACCESS_KEY', 'your-access-key'); // Replace with your AWS Access Key
define('AWS_SECRET_KEY', 'your-secret-key'); // Replace with your AWS Secret Key
define('S3_BUCKET_NAME', 'your-bucket-name'); // Replace with your S3 Bucket Name

// Initialize S3 Client
function createS3Client() {
    return new S3Client([
        'version' => 'latest',
        'region' => AWS_REGION,
        'credentials' => [
            'key' => AWS_ACCESS_KEY,
            'secret' => AWS_SECRET_KEY
        ]
    ]);
}

// Upload File to S3
function uploadToS3($filePath, $fileName) {
    $s3 = createS3Client();
    try {
        $result = $s3->putObject([
            'Bucket' => S3_BUCKET_NAME,
            'Key' => $fileName,
            'SourceFile' => $filePath,
            'ACL' => 'public-read' // Make file public (optional)
        ]);
        return $result['ObjectURL']; // Return the uploaded file's URL
    } catch (AwsException $e) {
        error_log($e->getMessage());
        return false;
    }
}

// Retrieve File from S3
function getFileFromS3($fileName) {
    $s3 = createS3Client();
    try {
        $result = $s3->getObject([
            'Bucket' => S3_BUCKET_NAME,
            'Key' => $fileName
        ]);
        return (string) $result['Body']; // Return the file's content
    } catch (AwsException $e) {
        error_log($e->getMessage());
        return false;
    }
}

// Example Usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_FILES['file']) && $_FILES['file']['error'] === UPLOAD_ERR_OK) {
        $uploadedFilePath = $_FILES['file']['tmp_name'];
        $uploadedFileName = basename($_FILES['file']['name']);
        $s3Url = uploadToS3($uploadedFilePath, $uploadedFileName);

        if ($s3Url) {
            echo "File uploaded successfully: <a href=\"$s3Url\">$s3Url</a>";
        } else {
            echo "Failed to upload file.";
        }
    }
} elseif (isset($_GET['fileName'])) {
    $fileName = $_GET['fileName'];
    $fileContent = getFileFromS3($fileName);

    if ($fileContent !== false) {
        header('Content-Type: text/plain');
        echo $fileContent;
    } else {
        echo "Failed to retrieve file.";
    }
}
?>
```

---

### JavaScript Frontend Code (AJAX API Calls)

```javascript
// Function to upload a file to the backend
async function uploadFile(file) {
    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('upload.php', { // Replace 'upload.php' with the correct PHP file path
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const result = await response.text();
            console.log('File Upload Response:', result);
            alert(result); // Display upload result in an alert
        } else {
            console.error('Failed to upload file:', response.statusText);
            alert('Failed to upload file.');
        }
    } catch (error) {
        console.error('Upload error:', error);
        alert('An error occurred while uploading the file.');
    }
}

// Function to fetch file content from the backend
async function fetchFile(fileName) {
    try {
        const response = await fetch(`upload.php?fileName=${encodeURIComponent(fileName)}`); // Replace 'upload.php' with the correct PHP file path

        if (response.ok) {
            const fileContent = await response.text();
            console.log('Fetched File Content:', fileContent);
            alert(fileContent); // Display file content in an alert
        } else {
            console.error('Failed to fetch file:', response.statusText);
            alert('Failed to fetch file.');
        }
    } catch (error) {
        console.error('Fetch error:', error);
        alert('An error occurred while fetching the file.');
    }
}

// Example Usage
document.getElementById('uploadBtn').addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
        uploadFile(file);
    }
});

document.getElementById('fetchBtn').addEventListener('click', () => {
    const fileName = prompt('Enter the file name to fetch:');
    if (fileName) {
        fetchFile(fileName);
    }
});
```

### HTML for Frontend

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AWS S3 Integration</title>
</head>
<body>
    <h1>AWS S3 Integration</h1>
    <h2>Upload File</h2>
    <input type="file" id="uploadBtn" />
    <h2>Fetch File</h2>
    <button id="fetchBtn">Fetch File</button>

    <script src="script.js"></script> <!-- Replace 'script.js' with correct JavaScript file path -->
</body>
</html>
```
