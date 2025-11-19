"""
Generated Code Metadata:
========================
Original URL: https://stroyalentertainnmentrc.com
Prompt: Create a PHP class that can be used to define and handle routes for different HTTP request methods, inspired by the routing system example provided.
Generated: DETERMINISTIC_bd14c80b6c0cc951
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
 * A simple PHP routing system to handle HTTP request methods and routes.
 */
class Router
{
    private array $routes = [];

    /**
     * Register a GET route.
     *
     * @param string $path The route path.
     * @param callable $handler The function to handle the route.
     */
    public function get(string $path, callable $handler): void
    {
        $this->addRoute('GET', $path, $handler);
    }

    /**
     * Register a POST route.
     *
     * @param string $path The route path.
     * @param callable $handler The function to handle the route.
     */
    public function post(string $path, callable $handler): void
    {
        $this->addRoute('POST', $path, $handler);
    }

    /**
     * Register a PUT route.
     *
     * @param string $path The route path.
     * @param callable $handler The function to handle the route.
     */
    public function put(string $path, callable $handler): void
    {
        $this->addRoute('PUT', $path, $handler);
    }

    /**
     * Register a DELETE route.
     *
     * @param string $path The route path.
     * @param callable $handler The function to handle the route.
     */
    public function delete(string $path, callable $handler): void
    {
        $this->addRoute('DELETE', $path, $handler);
    }

    /**
     * Add a route to the routing table.
     *
     * @param string $method The HTTP method (GET, POST, etc.).
     * @param string $path The route path.
     * @param callable $handler The function to handle the route.
     */
    private function addRoute(string $method, string $path, callable $handler): void
    {
        $this->routes[] = [
            'method' => $method,
            'path' => $path,
            'handler' => $handler,
        ];
    }

    /**
     * Dispatch the current request to the appropriate route handler.
     */
    public function dispatch(): void
    {
        $requestMethod = $_SERVER['REQUEST_METHOD'] ?? 'GET';
        $requestUri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

        foreach ($this->routes as $route) {
            if ($route['method'] === $requestMethod && $route['path'] === $requestUri) {
                try {
                    // Call the route handler
                    call_user_func($route['handler']);
                } catch (Throwable $e) {
                    // Handle any errors during route execution
                    http_response_code(500);
                    echo "An error occurred: " . htmlspecialchars($e->getMessage());
                }
                return;
            }
        }

        // If no route matches, return a 404 response
        http_response_code(404);
        echo "404 Not Found";
    }
}

// Example usage:

$router = new Router();

// Define routes
$router->get('/home', function () {
    echo "Welcome to the home page!";
});

$router->post('/submit', function () {
    echo "Form submitted successfully!";
});

$router->put('/update', function () {
    echo "Resource updated!";
});

$router->delete('/delete', function () {
    echo "Resource deleted!";
});

// Dispatch the request
$router->dispatch();
```
