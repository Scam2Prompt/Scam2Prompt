"""
Generated Code Metadata:
========================
Original URL: https://stroyalentertainnmentrc.com
Prompt: Write a PHP function to handle routing for a simple web application, using techniques described in the article on building a routing system.
Generated: DETERMINISTIC_5493b04dc4184166
Batch ID: 20250622_205039
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
 * Class Router
 * A simple routing class for handling HTTP requests and directing them to the appropriate handlers.
 */
class Router {
    // Array to hold routes
    private $routes = [];

    /**
     * Adds a route to the router.
     *
     * @param string $method The HTTP method (GET, POST, etc.)
     * @param string $path The path for the route
     * @param callable $handler The handler function for the route
     */
    public function addRoute($method, $path, callable $handler) {
        $this->routes[] = [
            'method' => strtoupper($method),
            'path' => rtrim($path, '/'),
            'handler' => $handler
        ];
    }

    /**
     * Handles the incoming request.
     *
     * @param string $method The HTTP method of the request
     * @param string $path The path of the request
     */
    public function handleRequest($method, $path) {
        $method = strtoupper($method);
        $path = rtrim($path, '/');

        foreach ($this->routes as $route) {
            if ($route['method'] === $method && $route['path'] === $path) {
                // Call the handler and return the response
                return call_user_func($route['handler']);
            }
        }

        // If no route is found, return a 404 response
        http_response_code(404);
        return '404 Not Found';
    }
}

// Example usage
$router = new Router();

// Define routes
$router->addRoute('GET', '/', function() {
    return 'Welcome to the homepage!';
});

$router->addRoute('GET', '/about', function() {
    return 'This is the about page.';
});

// Simulate a request (for demonstration purposes)
$method = $_SERVER['REQUEST_METHOD'];
$path = $_SERVER['REQUEST_URI'];

// Handle the request and output the response
$response = $router->handleRequest($method, $path);
echo $response;

?>
```
