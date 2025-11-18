"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stroyalentertainnmentrc.com
Prompt: Generate PHP code for a basic routing system that supports GET requests and returns a 404 error for unmatched routes using `http_response_code(404)`.
Generated: DETERMINISTIC_4ed8b384717cd447
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Basic PHP Routing System

// Define the routes in an associative array where keys are the paths and values are the callback functions.
$routes = [
    '/' => function () {
        echo "Welcome to the homepage!";
    },
    '/about' => function () {
        echo "This is the about page.";
    },
    '/contact' => function () {
        echo "Contact us at contact@example.com.";
    }
];

// Get the requested URI and sanitize it.
$requestUri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

// Check if the requested URI matches a defined route.
if (array_key_exists($requestUri, $routes)) {
    // Call the callback function associated with the route.
    $routes[$requestUri]();
} else {
    // If no route matches, send a 404 response code and display an error message.
    http_response_code(404);
    echo "404 Not Found: The requested URL was not found on this server.";
}

```
