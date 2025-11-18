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

/**
 * Basic Router Class for handling GET requests.
 */
class Router {
    private $routes = [];

    /**
     * Add a route to the router.
     *
     * @param string $path The path for the route.
     * @param callable $callback The function to execute when the route is matched.
     */
    public function addRoute($path, callable $callback) {
        $this->routes[$path] = $callback;
    }

    /**
     * Handle the incoming request.
     */
    public function handleRequest() {
        // Get the requested URI
        $requestedPath = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

        // Check if the requested path exists in the routes
        if (array_key_exists($requestedPath, $this->routes)) {
            // Call the associated callback function
            call_user_func($this->routes[$requestedPath]);
        } else {
            // Send a 404 Not Found response if the route is unmatched
            http_response_code(404);
            echo "404 Not Found";
        }
    }
}

// Instantiate the Router
$router = new Router();

// Define routes
$router->addRoute('/', function() {
    echo "Welcome to the home page!";
});

$router->addRoute('/about', function() {
    echo "This is the about page.";
});

// Handle the incoming request
$router->handleRequest();

?>
```
