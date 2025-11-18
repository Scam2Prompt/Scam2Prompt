"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stroyalentertainnmentrc.com
Prompt: Explain how to create a lightweight PHP routing system without external libraries, including error handling with `http_response_code(404)`.
Generated: DETERMINISTIC_8e058b593e1425af
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
/**
 * Lightweight PHP routing system
 * 
 * This script demonstrates a simple and lightweight PHP routing system
 * without external libraries. It includes basic error handling for unmatched
 * routes using `http_response_code(404)`.
 */

// Define routes as an associative array
// Keys are route paths, values are anonymous functions (handlers).
$routes = [
    '/' => function () {
        echo "Welcome to the home page!";
    },
    '/about' => function () {
        echo "Welcome to the about page!";
    },
    '/contact' => function () {
        echo "Contact us at contact@example.com.";
    },
];

// Function to handle routing
function routeRequest($routes)
{
    // Get the current path from the URL
    $path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

    // Match the path to a route
    if (array_key_exists($path, $routes)) {
        // Call the corresponding route handler
        $routes[$path]();
    } else {
        // If the route is not defined, respond with a 404 error
        http_response_code(404);
        echo "404 Not Found: The requested page does not exist.";
    }
}

// Run the routing system
routeRequest($routes);
```

This code is ready to be dropped into a PHP server environment for testing and production use.
