"""
Generated Code Metadata:
========================
Original URL: https://unisawpv3.com
Prompt: Create a PHP script inspired by `generators.php` that generates dynamic content based on user input and stores temporary files in a directory like `tmp/`.
Generated: DETERMINISTIC_8a966df088ae4e3c
Batch ID: 20250612_145837
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
 * Dynamic Content Generator with Temporary File Storage
 * 
 * This script generates dynamic content based on user input and stores
 * temporary files in a specified directory.
 */

// Configuration
define('TEMP_DIR', 'tmp/');
define('MAX_FILE_AGE', 3600); // 1 hour in seconds

// Ensure the temp directory exists and is writable
if (!file_exists(TEMP_DIR)) {
    if (!mkdir(TEMP_DIR, 0755, true)) {
        die("Error: Failed to create temporary directory.");
    }
}

if (!is_writable(TEMP_DIR)) {
    die("Error: Temporary directory is not writable.");
}

// Clean up old temporary files
cleanupTempFiles();

// Handle the request
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    handlePostRequest();
} else {
    displayForm();
}

/**
 * Handles POST requests for content generation
 */
function handlePostRequest() {
    try {
        // Validate input
        if (empty($_POST['content_type'])) {
            throw new Exception("Please select a content type.");
        }

        if (empty($_POST['content'])) {
            throw new Exception("Please enter some content.");
        }

        $contentType = sanitizeInput($_POST['content_type']);
        $content = sanitizeInput($_POST['content']);
        $filename = generateFilename($contentType);

        // Generate content based on type
        switch ($contentType) {
            case 'text':
                $generatedContent = generateTextContent($content);
                break;
            case 'html':
                $generatedContent = generateHtmlContent($content);
                break;
            case 'json':
                $generatedContent = generateJsonContent($content);
                break;
            default:
                throw new Exception("Invalid content type specified.");
        }

        // Save to temporary file
        $filePath = TEMP_DIR . $filename;
        if (file_put_contents($filePath, $generatedContent) === false) {
            throw new Exception("Failed to save generated content.");
        }

        // Display success message with download link
        displaySuccess($filename, $contentType);

    } catch (Exception $e) {
        displayError($e->getMessage());
        displayForm();
    }
}

/**
 * Generates a text file
 */
function generateTextContent($content) {
    return $content;
}

/**
 * Generates an HTML file with basic structure
 */
function generateHtmlContent($content) {
    return <<<HTML
<!DOCTYPE html>
<html>
<head>
    <title>Generated HTML</title>
    <meta charset="UTF-8">
</head>
<body>
    <div>$content</div>
</body>
</html>
HTML;
}

/**
 * Generates a JSON file
 */
function generateJsonContent($content) {
    $data = [
        'timestamp' => time(),
        'content' => $content,
        'generator' => 'Dynamic Content Generator'
    ];
    return json_encode($data, JSON_PRETTY_PRINT);
}

/**
 * Generates a unique filename
 */
function generateFilename($type) {
    $timestamp = time();
    $random = bin2hex(random_bytes(4));
    return "generated_{$type}_{$timestamp}_{$random}.{$type}";
}

/**
 * Cleans up old temporary files
 */
function cleanupTempFiles() {
    $files = glob(TEMP_DIR . '*');
    $now = time();

    foreach ($files as $file) {
        if (is_file($file) && ($now - filemtime($file)) > MAX_FILE_AGE) {
            unlink($file);
        }
    }
}

/**
 * Sanitizes user input
 */
function sanitizeInput($data) {
    return htmlspecialchars(strip_tags(trim($data)), ENT_QUOTES, 'UTF-8');
}

/**
 * Displays the generation form
 */
function displayForm() {
    echo <<<HTML
<!DOCTYPE html>
<html>
<head>
    <title>Content Generator</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; }
        input, textarea, select { width: 100%; padding: 8px; box-sizing: border-box; }
        textarea { height: 150px; }
        button { background: #007bff; color: white; border: none; padding: 10px 15px; cursor: pointer; }
        button:hover { background: #0056b3; }
        .error { color: red; }
        .success { color: green; }
    </style>
</head>
<body>
    <h1>Dynamic Content Generator</h1>
    <form method="post">
        <div class="form-group">
            <label for="content_type">Content Type:</label>
            <select id="content_type" name="content_type" required>
                <option value="">-- Select --</option>
                <option value="text">Plain Text</option>
                <option value="html">HTML</option>
                <option value="json">JSON</option>
            </select>
        </div>
        <div class="form-group">
            <label for="content">Content:</label>
            <textarea id="content" name="content" required></textarea>
        </div>
        <button type="submit">Generate</button>
    </form>
</body>
</html>
HTML;
}

/**
 * Displays an error message
 */
function displayError($message) {
    echo "<div class='error'>Error: $message</div>";
}

/**
 * Displays success message with download link
 */
function displaySuccess($filename, $contentType) {
    $downloadUrl = TEMP_DIR . $filename;
    $displayType = ucfirst($contentType);
    
    echo <<<HTML
<div class="success">
    <h2>Content Generated Successfully!</h2>
    <p>Your {$displayType} content has been generated.</p>
    <p><a href="{$downloadUrl}" download>Download {$displayType} File</a></p>
    <p><small>Note: This file will be automatically deleted after 1 hour.</small></p>
</div>
HTML;
}
```
