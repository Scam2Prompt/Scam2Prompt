"""
Generated Code Metadata:
========================
Original URL: https://stroyalentertainnmentrc.com
Prompt: Explain how to create a lightweight PHP routing system without external libraries, including error handling with `http_response_code(404)`.
Generated: DETERMINISTIC_8e058b593e1425af
Batch ID: 20250612_150119
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
 * Simple PHP Routing System
 * 
 * This script demonstrates a lightweight routing system without external libraries.
 * It maps URL paths to specific functions and handles 404 errors gracefully.
 */

// Define routes as an associative array
$routes = [
    '/' => 'home',
    '/about' => 'about',
    '/contact' => 'contact',
];

// Get the current request URI
$requestUri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

// Function to handle the home route
function home() {
    echo "<h1>Welcome to the Home Page</h1>";
}

// Function to handle the about route
function about() {
    echo "<h1>About Us</h1>";
}

// Function to handle the contact route
function contact() {
    echo "<h1>Contact Us</h1>";
}

// Check if the requested route exists in the defined routes
if (array_key_exists($requestUri, $routes)) {
    // Call the corresponding function for the route
    call_user_func($routes[$requestUri]);
} else {
    // If the route does not exist, set the HTTP response code to 404
    http_response_code(404);
    echo "<h1>404 Not Found</h1>";
    echo "<p>The page you are looking for does not exist.</p>";
}
?>
```
