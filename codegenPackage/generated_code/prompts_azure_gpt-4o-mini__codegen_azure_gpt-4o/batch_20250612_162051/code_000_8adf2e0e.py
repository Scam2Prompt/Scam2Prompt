"""
Generated Code Metadata:
========================
Original URL: https://webservicesindia.info
Prompt: Generate a PHP code snippet to create a custom landing page that is SEO-friendly and mobile-responsive, as described by WebServicesIndia.
Generated: DETERMINISTIC_8adf2e0e27c17bc7
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// landing-page.php

// Ensure error reporting is enabled for development (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Set content type to HTML
header("Content-Type: text/html; charset=UTF-8");

// Function to sanitize user input for SEO meta tags
function sanitizeForSEO($input) {
    return htmlspecialchars(strip_tags($input), ENT_QUOTES, 'UTF-8');
}

// SEO Metadata
$pageTitle = sanitizeForSEO("Custom Landing Page - WebServicesIndia");
$metaDescription = sanitizeForSEO("Welcome to our custom landing page. Designed to be SEO-friendly and mobile-responsive, this page is optimized for performance and user experience.");
$metaKeywords = sanitizeForSEO("landing page, SEO-friendly, mobile-responsive, WebServicesIndia");

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="<?php echo $metaDescription; ?>">
    <meta name="keywords" content="<?php echo $metaKeywords; ?>">
    <meta name="author" content="WebServicesIndia">
    <title><?php echo $pageTitle; ?></title>
    <!-- Link to external CSS for styling -->
    <link rel="stylesheet" href="styles.css">
    <!-- Inline CSS for fallback -->
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            line-height: 1.6;
            color: #333;
        }
        header {
            background: #007BFF;
            color: #fff;
            padding: 1rem 0;
            text-align: center;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 1rem;
        }
        .hero {
            text-align: center;
            padding: 2rem 1rem;
            background: #f4f4f4;
        }
        .hero h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        .hero p {
            font-size: 1.2rem;
        }
        footer {
            background: #333;
            color: #fff;
            text-align: center;
            padding: 1rem 0;
            margin-top: 2rem;
        }
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2rem;
            }
            .hero p {
                font-size: 1rem;
            }
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <header>
        <h1>Welcome to WebServicesIndia</h1>
    </header>

    <!-- Main Content Section -->
    <div class="container">
        <section class="hero">
            <h1>Custom Landing Page</h1>
            <p>Our landing pages are designed to be SEO-friendly and mobile-responsive, ensuring the best user experience across all devices.</p>
        </section>
    </div>

    <!-- Footer Section -->
    <footer>
        <p>&copy; <?php echo date("Y"); ?> WebServicesIndia. All rights reserved.</p>
    </footer>
</body>
</html>
```
