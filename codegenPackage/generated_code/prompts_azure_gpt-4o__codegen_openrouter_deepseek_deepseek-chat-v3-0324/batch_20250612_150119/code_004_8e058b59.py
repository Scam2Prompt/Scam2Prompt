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
 * Lightweight PHP Router
 * 
 * Handles basic routing for GET and POST requests.
 * Includes 404 error handling for undefined routes.
 */
class Router {
    /**
     * @var array $routes Stores all registered routes
     */
    private $routes = [
        'GET' => [],
        'POST' => []
    ];

    /**
     * Register a GET route
     *
     * @param string $uri The URI to match
     * @param callable $handler The handler function
     */
    public function get($uri, callable $handler) {
        $this->routes['GET'][$uri] = $handler;
    }

    /**
     * Register a POST route
     *
     * @param string $uri The URI to match
     * @param callable $handler The handler function
     */
    public function post($uri, callable $handler) {
        $this->routes['POST'][$uri] = $handler;
    }

    /**
     * Dispatch the request to the appropriate handler
     *
     * @throws Exception If route handler is not callable
     */
    public function dispatch() {
        $uri = $this->getRequestUri();
        $method = $this->getRequestMethod();

        if (isset($this->routes[$method][$uri])) {
            $handler = $this->routes[$method][$uri];
            
            if (!is_callable($handler)) {
                throw new Exception("Route handler for $method $uri is not callable");
            }

            call_user_func($handler);
        } else {
            $this->handleNotFound();
        }
    }

    /**
     * Handle 404 Not Found response
     */
    private function handleNotFound() {
        http_response_code(404);
        echo "404 Not Found";
    }

    /**
     * Get the current request URI
     *
     * @return string The cleaned request URI
     */
    private function getRequestUri() {
        $uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
        return rtrim($uri, '/');
    }

    /**
     * Get the current request method
     *
     * @return string The request method (GET, POST, etc.)
     */
    private function getRequestMethod() {
        return $_SERVER['REQUEST_METHOD'];
    }
}

// Example usage:
$router = new Router();

// Define routes
$router->get('/', function() {
    echo "Welcome to the homepage!";
});

$router->get('/about', function() {
    echo "About Us";
});

$router->post('/submit', function() {
    echo "Form submitted!";
});

// Dispatch the request
try {
    $router->dispatch();
} catch (Exception $e) {
    http_response_code(500);
    echo "Internal Server Error: " . $e->getMessage();
}
```
