"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jieyasoft.com
Prompt: Create a responsive web design for a direct selling system that supports multiple platforms (PC, WAP, app, WeChat) using .NET or PHP, as described by JieyaSoft.
Generated: DETERMINISTIC_582592c771e14e1f
Batch ID: 20250612_154422
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://code.jquery.com/jquery-3.5.1.slim.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
// index.php
// This file serves as the entry point for the Direct Selling System
// It implements a responsive web design using Bootstrap for front-end framework

// Start a session for user management
session_start();

// Include necessary files for database connection and user authentication
require 'config.php';
require 'functions.php';

try {
    // Connect to the database
    $db = new PDO("mysql:host=$dbHost;dbname=$dbName", $dbUser, $dbPass);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle database connection error
    die("Database connection failed: " . $e->getMessage());
}

// Check if user is logged in
$user = isset($_SESSION['user']) ? $_SESSION['user'] : null;

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Direct Selling System</title>
    <!-- Include Bootstrap CSS for responsive design -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="styles.css">
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Direct Selling</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
            <li class="nav-item active">
                <a class="nav-link" href="#">Home</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="products.php">Products</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="contact.php">Contact</a>
            </li>
            <?php if ($user): ?>
                <li class="nav-item">
                    <a class="nav-link" href="logout.php">Logout</a>
                </li>
            <?php else: ?>
                <li class="nav-item">
                    <a class="nav-link" href="login.php">Login</a>
                </li>
            <?php endif; ?>
        </ul>
    </div>
</nav>

<div class="container mt-4">
    <h1>Welcome to Direct Selling System</h1>
    <p>This platform allows you to manage your direct selling operations efficiently.</p>
</div>

<!-- Include Bootstrap JS and dependencies -->
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
```

```php
<?php
// config.php
// Configuration for database connection
$dbHost = 'localhost'; // Database host
$dbName = 'direct_selling'; // Database name
$dbUser = 'user'; // Database user
$dbPass = 'password'; // Database password
?>
```

```php
<?php
// functions.php
// This file contains helper functions for the Direct Selling System

/**
 * Redirect to a specified URL
 *
 * @param string $url URL to redirect to
 */
function redirect($url) {
    header("Location: $url");
    exit;
}

/**
 * Sanitize user input
 *
 * @param mixed $data User input
 * @return mixed Sanitized input
 */
function sanitize($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}
?>
```

```css
/* styles.css */
/* Custom styles for the Direct Selling System */

body {
    background-color: #f8f9fa; /* Light background for better readability */
}

.container {
    margin-top: 20px; /* Spacing for the main container */
}

.navbar {
    margin-bottom: 20px; /* Spacing below the navbar */
}
```

This code provides the foundation for a responsive web design for a direct selling system using PHP and Bootstrap. It includes error handling, session management, and functions for URL redirection and input sanitization. The CSS is minimal and can be expanded based on specific design requirements.
