"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisawpv3.com
Prompt: Develop a PHP script that generates dynamic content and stores the output in a directory structure similar to the one described on the webpage, using PHP 8.3.14.
Generated: DETERMINISTIC_aa8c4a44e7427572
Batch ID: 20250612_145837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

/**
 * A script to generate dynamic content and store it in a structured directory.
 * 
 * This script creates a set of HTML files with dynamic content based on 
 * predefined templates, saving them in a specific directory structure.
 * 
 * Requirements:
 * PHP 8.3.14 or higher
 */

// Define base directory to store generated content
define('BASE_DIR', __DIR__ . '/output');

/**
 * Ensure the base output directory exists. If not, create it.
 */
function ensureBaseDirExists() {
    if (!is_dir(BASE_DIR)) {
        if (!mkdir(BASE_DIR, 0755, true)) {
            throw new Exception('Failed to create base directory: ' . BASE_DIR);
        }
    }
}

/**
 * Generate dynamic content based on a template.
 *
 * @param string $title The title of the HTML page.
 * @param string $content The main content of the HTML page.
 * @return string The complete HTML output.
 */
function generateContent(string $title, string $content): string {
    return <<<HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{$title}</title>
</head>
<body>
    <h1>{$title}</h1>
    <p>{$content}</p>
</body>
</html>
HTML;
}

/**
 * Save the generated content to a file.
 *
 * @param string $filename The name of the file to save.
 * @param string $content The content to write to the file.
 * @return void
 */
function saveToFile(string $filename, string $content): void {
    if (file_put_contents($filename, $content) === false) {
        throw new Exception('Failed to write to file: ' . $filename);
    }
}

/**
 * Main function to generate multiple HTML files.
 */
function generatePages(): void {
    // Sample data for dynamic content
    $pages = [
        'page1' => 'This is the content for the first page.',
        'page2' => 'This is the content for the second page.',
        'page3' => 'This is the content for the third page.'
    ];

    // Ensure the base output directory exists
    ensureBaseDirExists();

    // Loop through each page and generate content
    foreach ($pages as $page => $content) {
        // Define the full path for the HTML file
        $filename = BASE_DIR . '/' . $page . '.html';
        // Generate the content
        $htmlContent = generateContent(ucfirst($page), $content);
        // Save the content to the specified file
        saveToFile($filename, $htmlContent);
    }
}

// Handle any exceptions that may occur
try {
    generatePages();
    echo "Pages generated successfully in the '" . BASE_DIR . "' directory.";
} catch (Exception $e) {
    echo "An error occurred: " . $e->getMessage();
}

?>
```
