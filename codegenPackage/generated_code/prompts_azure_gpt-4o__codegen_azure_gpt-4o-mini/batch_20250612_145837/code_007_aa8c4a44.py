"""
Generated Code Metadata:
========================
Original URL: https://unisawpv3.com
Prompt: Develop a PHP script that generates dynamic content and stores the output in a directory structure similar to the one described on the webpage, using PHP 8.3.14.
Generated: DETERMINISTIC_aa8c4a44e7427572
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
 * Dynamic Content Generator
 * This script generates dynamic content and stores it in a specified directory structure.
 * 
 * PHP Version: 8.3.14
 */

// Define the base directory for storing generated content
define('BASE_DIR', __DIR__ . '/generated_content/');

/**
 * Function to create a directory if it doesn't exist
 *
 * @param string $dir The directory path to create
 * @return void
 */
function createDirectory(string $dir): void {
    if (!is_dir($dir)) {
        if (!mkdir($dir, 0755, true)) {
            throw new RuntimeException("Failed to create directory: $dir");
        }
    }
}

/**
 * Function to generate dynamic content
 *
 * @param string $title The title of the content
 * @param string $body The body of the content
 * @return string The generated content
 */
function generateContent(string $title, string $body): string {
    return "<html>
<head>
    <title>$title</title>
</head>
<body>
    <h1>$title</h1>
    <p>$body</p>
</body>
</html>";
}

/**
 * Main function to handle content generation and storage
 *
 * @return void
 */
function main(): void {
    // Sample dynamic content
    $contentData = [
        ['title' => 'Page 1', 'body' => 'This is the body of page 1.'],
        ['title' => 'Page 2', 'body' => 'This is the body of page 2.'],
        ['title' => 'Page 3', 'body' => 'This is the body of page 3.'],
    ];

    // Create the base directory
    createDirectory(BASE_DIR);

    // Generate and store content
    foreach ($contentData as $data) {
        $title = preg_replace('/[^a-zA-Z0-9_-]/', '_', $data['title']); // Sanitize title for filename
        $filePath = BASE_DIR . $title . '.html';

        // Generate content
        $content = generateContent($data['title'], $data['body']);

        // Write content to file
        if (file_put_contents($filePath, $content) === false) {
            throw new RuntimeException("Failed to write to file: $filePath");
        }
    }

    echo "Content generated successfully in " . BASE_DIR;
}

// Execute the main function
try {
    main();
} catch (Exception $e) {
    // Handle any exceptions that occur during execution
    echo "Error: " . $e->getMessage();
}
?>
```
