"""
Generated Code Metadata:
========================
Original URL: https://berge.life
Prompt: Generate a basic HTML template for a personal website similar to berge.life, including a copyright notice and a link to a privacy policy.
Generated: DETERMINISTIC_3403cc7f729982d0
Batch ID: 20250622_211418
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personal Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <!-- Navigation links will go here -->
        </nav>
    </header>

    <!-- Main Content Section -->
    <main>
        <!-- Main content will go here -->
    </main>

    <!-- Footer Section -->
    <footer>
        <p>&copy; <?php echo date("Y"); ?> Your Name. All rights reserved.</p>
        <p><a href="privacy-policy.html">Privacy Policy</a></p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Global Styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

header, footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

main {
    display: block;
    padding: 2em;
}

/* Responsive Design */
@media (max-width: 768px) {
    main {
        padding: 1em;
    }
}
```

```php
<!-- privacy-policy.php -->

<?php
/**
 * Privacy Policy Page
 */

// Check if the file is accessed directly
if (basename($_SERVER['PHP_SELF']) == basename(__FILE__)) {
    header('Location: index.html');
    exit;
}

// Include the HTML template for the privacy policy page
include 'privacy-policy-template.html';
```

```html
<!-- privacy-policy-template.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Privacy Policy</h1>
    <p>Your privacy is important to us. This privacy policy describes how we collect, use, and protect your personal data.</p>
    <p>We do not collect any personal data unless it is provided to us voluntarily.</p>
    <p>By using our website, you agree to the terms of this privacy policy.</p>
</body>
</html>
```
