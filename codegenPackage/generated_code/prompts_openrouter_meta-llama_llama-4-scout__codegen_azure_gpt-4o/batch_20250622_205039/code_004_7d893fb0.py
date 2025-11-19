"""
Generated Code Metadata:
========================
Original URL: https://stroyalentertainnmentrc.com
Prompt: Generate code for a simple PHP router that can map URLs to specific controller actions, following best practices outlined in the article on building a routing system in PHP.
Generated: DETERMINISTIC_7d893fb085763357
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

// Router.php
class Router
{
    private $routes = [];

    /**
     * Register a GET route.
     *
     * @param string $path The URL path.
     * @param callable $action The action to execute.
     */
    public function get(string $path, callable $action): void
    {
        $this->routes['GET'][$path] = $action;
    }

    /**
     * Register a POST route.
     *
     * @param string $path The URL path.
     * @param callable $action The action to execute.
     */
    public function post(string $path, callable $action): void
    {
        $this->routes['POST'][$path] = $action;
    }

    /**
     * Dispatch the current request to the appropriate route.
     */
    public function dispatch(): void
    {
        $method = $_SERVER['REQUEST_METHOD'];
        $path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

        // Check if the route exists for the current method and path
        if (isset($this->routes[$method][$path])) {
            try {
                // Execute the registered action
                call_user_func($this->routes[$method][$path]);
            } catch (Exception $e) {
                // Handle any exceptions that occur during execution
                http_response_code(500);
                echo "Internal Server Error: " . htmlspecialchars($e->getMessage());
            }
        } else {
            // Return a 404 response if the route is not found
            http_response_code(404);
            echo "404 Not Found";
        }
    }
}

// Example usage:

// Create a new Router instance
$router = new Router();

// Define routes
$router->get('/home', function () {
    echo "Welcome to the home page!";
});

$router->get('/about', function () {
    echo "This is the about page.";
});

$router->post('/submit', function () {
    echo "Form submitted successfully!";
});

// Dispatch the request
$router->dispatch();
```
