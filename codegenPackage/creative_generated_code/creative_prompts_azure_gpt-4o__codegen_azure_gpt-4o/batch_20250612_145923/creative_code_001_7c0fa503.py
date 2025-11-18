"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinmaarokatcap.com
Prompt: Using PHP 8.3.14, create a script similar to `build.php` that dynamically generates HTML pages based on user input.
Generated: DETERMINISTIC_7c0fa5033b28cbd3
Batch ID: 20250612_145923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// build.php - Dynamically generates an HTML page based on user input.
//
// This script takes user input, validates it, and generates an HTML file.
// The HTML file is saved to the "output" directory with a unique filename.

// Ensure the output directory exists
define('OUTPUT_DIR', __DIR__ . '/output');
if (!is_dir(OUTPUT_DIR)) {
    mkdir(OUTPUT_DIR, 0755, true);
}

// Function to sanitize user inputs
function sanitizeInput(string $input): string {
    return htmlspecialchars(trim($input), ENT_QUOTES, 'UTF-8');
}

// Function to generate a unique filename
function generateFilename(): string {
    return 'page_' . time() . '_' . bin2hex(random_bytes(4)) . '.html';
}

// Check if the form has been submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    // Validate required fields
    $title = sanitizeInput($_POST['title'] ?? '');
    $body = sanitizeInput($_POST['body'] ?? '');

    if (empty($title) || empty($body)) {
        die('Error: Both title and body are required.');
    }

    // Build HTML content
    $html = <<<HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{$title}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            color: #333;
        }
    </style>
</head>
<body>
    <h1>{$title}</h1>
    <div>
        {$body}
    </div>
</body>
</html>
HTML;

    // Generate unique filename and save the file
    $filename = generateFilename();
    $filepath = OUTPUT_DIR . '/' . $filename;

    if (file_put_contents($filepath, $html) === false) {
        die('Error: Failed to create HTML file.');
    }

    // Display success message
    echo "HTML page generated successfully! <a href='output/{$filename}' target='_blank'>View Page</a>";
} else {
    // Display the form if no POST request is made
    ?>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>HTML Page Builder</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
            }
            form {
                max-width: 600px;
                margin: 0 auto;
            }
            label {
                display: block;
                margin: 10px 0 5px;
            }
            input, textarea {
                width: 100%;
                padding: 10px;
                margin-bottom: 15px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            button {
                padding: 10px 15px;
                background-color: #007BFF;
                color: #fff;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <h1>HTML Page Builder</h1>
        <form method="POST" action="">
            <label for="title">Page Title:</label>
            <input type="text" id="title" name="title" required>
            <label for="body">Page Content:</label>
            <textarea id="body" name="body" rows="10" required></textarea>
            <button type="submit">Generate Page</button>
        </form>
    </body>
    </html>
    <?php
}
?>
```
