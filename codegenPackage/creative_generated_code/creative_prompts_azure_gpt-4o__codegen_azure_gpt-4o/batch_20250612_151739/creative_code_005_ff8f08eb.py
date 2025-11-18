"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://urlz.fr
Prompt: Write PHP code to build a web interface for shortening URLs, inspired by the functionality described on URLz.fr, including a button to generate and display the shortened link.
Generated: DETERMINISTIC_ff8f08eb1b68141d
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// ShortURL.php
// A simple URL shortener script written in PHP.

// Start a session to store shortened URLs temporarily
session_start();

// Function to generate a random short code
function generateShortCode($length = 6) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $charactersLength = strlen($characters);
    $shortCode = '';
    for ($i = 0; $i < $length; $i++) {
        $shortCode .= $characters[random_int(0, $charactersLength - 1)];
    }
    return $shortCode;
}

// Function to validate URL format
function validateURL($url) {
    return filter_var($url, FILTER_VALIDATE_URL) !== false;
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $originalURL = $_POST['url'] ?? '';
    if (validateURL($originalURL)) {
        // Generate a unique short code
        $shortCode = generateShortCode();
        
        // Store the mapping in the session (for simplicity; production systems should use a database)
        $_SESSION['shortened_urls'][$shortCode] = $originalURL;

        // Create the shortened URL
        $shortenedURL = sprintf(
            '%s://%s%s?code=%s',
            isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] === 'on' ? 'https' : 'http',
            $_SERVER['HTTP_HOST'],
            $_SERVER['PHP_SELF'],
            $shortCode
        );

        $message = "Shortened URL: <a href=\"{$shortenedURL}\" target=\"_blank\">{$shortenedURL}</a>";
    } else {
        $message = 'Invalid URL. Please provide a valid URL.';
    }
}

// Handle redirect if a short code is accessed via GET
if (isset($_GET['code'])) {
    $code = $_GET['code'];
    if (isset($_SESSION['shortened_urls'][$code])) {
        header('Location: ' . $_SESSION['shortened_urls'][$code]);
        exit;
    } else {
        $message = 'Invalid short code.';
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP URL Shortener</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0 auto;
            max-width: 600px;
            padding: 20px;
            text-align: center;
        }
        form {
            margin-bottom: 20px;
        }
        input[type="text"] {
            width: 80%;
            padding: 10px;
            margin-right: 10px;
        }
        button {
            padding: 10px 20px;
        }
        .message {
            margin-top: 20px;
            font-weight: bold;
            color: #333;
        }
    </style>
</head>
<body>
    <h1>URL Shortener</h1>

    <!-- Form for URL input -->
    <form method="POST" action="">
        <input type="text" name="url" placeholder="Enter a URL to shorten" required>
        <button type="submit">Shorten URL</button>
    </form>

    <!-- Display messages -->
    <?php if (!empty($message)): ?>
        <div class="message">
            <?= $message ?>
        </div>
    <?php endif; ?>
</body>
</html>
```
