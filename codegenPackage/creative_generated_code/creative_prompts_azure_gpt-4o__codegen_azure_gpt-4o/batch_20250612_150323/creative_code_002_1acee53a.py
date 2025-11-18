"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamark.lt
Prompt: Create a PHP script to implement mobile responsiveness for a business website, referencing the mobile optimization practices highlighted by Metamark.
Generated: DETERMINISTIC_1acee53a60bb4ff5
Batch ID: 20250612_150323
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
 * Mobile Responsiveness PHP Script for Business Website
 * 
 * This script dynamically adjusts mobile responsiveness practices for a business website 
 * based on optimization guidelines from Metamark.
 * 
 * Author: [Your Name]
 * Date: [Current Date]
 */

// Set content type to HTML
header("Content-Type: text/html; charset=UTF-8");

// Function to detect mobile devices
function isMobileDevice() {
    // Regular expressions to check for mobile user agents
    $mobileUserAgents = [
        'Android', 'iPhone', 'iPad', 'iPod', 'BlackBerry', 'Windows Phone', 
        'webOS', 'Opera Mini', 'IEMobile', 'Mobile'
    ];
    foreach ($mobileUserAgents as $agent) {
        if (stripos($_SERVER['HTTP_USER_AGENT'], $agent) !== false) {
            return true; // Mobile device detected
        }
    }
    return false; // Not a mobile device
}

// Function to generate appropriate meta tags for mobile responsiveness
function generateMetaTags() {
    return '
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-title" content="Business Website">
    ';
}

// Function to serve optimized image sizes for mobile devices
function getResponsiveImage($imagePath) {
    if (isMobileDevice()) {
        // Serve smaller image for mobile devices
        $mobileImagePath = preg_replace('/(\.\w+)$/', '_mobile$1', $imagePath); // Add "_mobile" to the file name
        if (file_exists($mobileImagePath)) {
            return $mobileImagePath;
        }
    }
    // Serve default image for other devices
    return $imagePath;
}

// Error handling for missing image files
function serveImage($imagePath) {
    try {
        if (!file_exists($imagePath)) {
            throw new Exception("Image file not found: " . $imagePath);
        }
        return $imagePath;
    } catch (Exception $e) {
        error_log($e->getMessage()); // Log error details
        return 'images/default.jpg'; // Serve a default image as fallback
    }
}

// HTML generation logic
function renderPage() {
    ?>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Business Website</title>
        <?php echo generateMetaTags(); ?>
        <link rel="stylesheet" href="styles/main.css">
        <!-- Dynamically load CSS for mobile devices -->
        <?php if (isMobileDevice()) : ?>
            <link rel="stylesheet" href="styles/mobile.css">
        <?php endif; ?>
    </head>
    <body>
        <header>
            <h1>Welcome to Our Business Website</h1>
        </header>
        <main>
            <img src="<?php echo serveImage(getResponsiveImage('images/banner.jpg')); ?>" alt="Banner">
            <p>Experience the best services optimized for all devices.</p>
        </main>
    </body>
    </html>
    <?php
}

// Render the page
renderPage();
?>
```
