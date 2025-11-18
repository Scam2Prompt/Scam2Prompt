"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stroyalentertainnmentrc.com
Prompt: Write a PHP script to implement a custom routing system, ensuring the use of `http_response_code(404)` for undefined routes.
Generated: DETERMINISTIC_68bf23c534cf93bf
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
// Custom routing system in PHP

// Define the router class
class Router {
    // Array to hold the routes
    private $routes = [];

    // Method to define a route
    public function addRoute($method, $path, $callback) {
        $this->routes[] = [
            'method' => strtoupper($method),
            'path' => rtrim($path, '/'),
            'callback' => $callback
        ];
    }

    // Method to handle the incoming request
    public function handleRequest($method, $uri) {
        // Normalize the URI
        $uri = rtrim($uri, '/');

        // Iterate through the defined routes
        foreach ($this->routes as $route) {
            if ($route['method'] === strtoupper($method) && $route['path'] === $uri) {
                // Call the corresponding callback
                return call_user_func($route['callback']);
            }
        }

        // If no route matched, send a 404 response
        http_response_code(404);
        echo "404 Not Found";
    }
}

// Create an instance of the Router
$router = new Router();

// Define the routes
$router->addRoute('GET', '/', function() {
    return "Welcome to the home page!";
});

$router->addRoute('GET', '/about', function() {
    return "This is the about page.";
});

// Handle the request
try {
    $method = $_SERVER['REQUEST_METHOD']; // Get the request method
    $uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH); // Get the request URI
    $router->handleRequest($method, $uri); // Handle the request
} catch (Exception $e) {
    // In case of any unexpected error, set a general error response
    http_response_code(500);
    echo "500 Internal Server Error";
}
?>
```
