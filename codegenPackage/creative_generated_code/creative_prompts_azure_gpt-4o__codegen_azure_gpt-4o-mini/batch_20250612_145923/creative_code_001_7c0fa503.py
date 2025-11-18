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
/**
 * Dynamic HTML Page Generator
 * This script generates HTML pages based on user input.
 * It accepts a title and content via GET parameters and displays a formatted HTML page.
 * 
 * PHP Version: 8.3.14
 */

// Set content type to HTML
header('Content-Type: text/html; charset=utf-8');

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(trim($data), ENT_QUOTES, 'UTF-8');
}

// Initialize variables
$title = '';
$content = '';

// Check if user input is provided
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    // Sanitize user inputs
    $title = isset($_GET['title']) ? sanitizeInput($_GET['title']) : 'Default Title';
    $content = isset($_GET['content']) ? sanitizeInput($_GET['content']) : 'Default content goes here.';
}

// Start output buffering
ob_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $title; ?></title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external stylesheet -->
</head>
<body>
    <header>
        <h1><?php echo $title; ?></h1>
    </header>
    <main>
        <article>
            <p><?php echo nl2br($content); ?></p> <!-- Convert newlines to <br> tags -->
        </article>
    </main>
    <footer>
        <p>&copy; <?php echo date("Y"); ?> Dynamic Page Generator</p>
    </footer>
</body>
</html>
<?php
// Get the contents of the output buffer
$htmlContent = ob_get_clean();

// Save HTML to a file (optional)
// $filename = 'generated_page.html';
// if (file_put_contents($filename, $htmlContent) === false) {
//     error_log("Error: Unable to write to file $filename");
// }

// Output the generated HTML
echo $htmlContent;
?>
```
