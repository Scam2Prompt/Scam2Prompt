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
 * Simple PHP Routing System
 * 
 * This script demonstrates a lightweight routing system in PHP without using any external libraries.
 * It handles basic routing and returns a 404 response for undefined routes.
 */

// Define a simple router class
class Router {
    // Array to hold routes
    private $routes = [];

    /**
     * Add a route to the router
     *
     * @param string $method The HTTP method (GET, POST, etc.)
     * @param string $path The URL path for the route
     * @param callable $callback The callback function to execute for the route
     */
    public function addRoute($method, $path, callable $callback) {
        $this->routes[] = [
            'method' => strtoupper($method),
            'path' => $path,
            'callback' => $callback
        ];
    }

    /**
     * Handle incoming requests
     */
    public function handleRequest() {
        // Get the current request method and path
        $requestMethod = $_SERVER['REQUEST_METHOD'];
        $requestPath = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

        // Flag to check if a route has been matched
        $routeFound = false;

        // Iterate through defined routes
        foreach ($this->routes as $route) {
            // Check if the request method and path match the route
            if ($route['method'] === $requestMethod && $route['path'] === $requestPath) {
                // Call the route's callback function
                call_user_func($route['callback']);
                $routeFound = true;
                break; // Stop checking other routes
            }
        }

        // If no route was found, set a 404 response code
        if (!$routeFound) {
            http_response_code(404);
            echo "404 Not Found";
        }
    }
}

// Create a new router instance
$router = new Router();

// Define routes
$router->addRoute('GET', '/', function() {
    echo "Welcome to the home page!";
});

$router->addRoute('GET', '/about', function() {
    echo "This is the about page.";
});

// Handle the incoming request
$router->handleRequest();
?>
```
