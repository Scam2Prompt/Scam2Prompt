"""
Generated Code Metadata:
========================
Original URL: https://stroyalentertainnmentrc.com
Prompt: Write a PHP script to implement a custom routing system, ensuring the use of `http_response_code(404)` for undefined routes.
Generated: DETERMINISTIC_68bf23c534cf93bf
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
 * Custom Router Class
 */
class Router {
    /**
     * @var array $routes Stores all registered routes
     */
    private $routes = [];

    /**
     * Add a route to the router
     *
     * @param string $method HTTP method (GET, POST, etc.)
     * @param string $path URL path
     * @param callable $handler Callback function to execute
     */
    public function addRoute($method, $path, $handler) {
        $this->routes[$method][$path] = $handler;
    }

    /**
     * Dispatch the request to the appropriate handler
     */
    public function dispatch() {
        $method = $_SERVER['REQUEST_METHOD'];
        $path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

        if (isset($this->routes[$method][$path])) {
            call_user_func($this->routes[$method][$path]);
        } else {
            $this->notFound();
        }
    }

    /**
     * Handle 404 Not Found responses
     */
    private function notFound() {
        http_response_code(404);
        echo "404 Not Found";
    }
}

// Example usage:
$router = new Router();

// Define routes
$router->addRoute('GET', '/', function() {
    echo "Welcome to the homepage!";
});

$router->addRoute('GET', '/about', function() {
    echo "About Us";
});

$router->addRoute('GET', '/contact', function() {
    echo "Contact Page";
});

// Dispatch the request
$router->dispatch();

?>
```
