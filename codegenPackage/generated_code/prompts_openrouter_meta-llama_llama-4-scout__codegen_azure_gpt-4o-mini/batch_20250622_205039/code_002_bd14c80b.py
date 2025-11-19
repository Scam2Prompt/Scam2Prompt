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
 * A simple routing class to handle HTTP requests for different methods.
 */
class Router
{
    // Array to hold routes
    private $routes = [];

    /**
     * Add a route to the router.
     *
     * @param string $method The HTTP method (GET, POST, etc.)
     * @param string $path The path for the route
     * @param callable $handler The handler function for the route
     */
    public function addRoute(string $method, string $path, callable $handler)
    {
        // Normalize method to uppercase
        $method = strtoupper($method);
        
        // Validate method
        if (!in_array($method, ['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])) {
            throw new InvalidArgumentException("Invalid HTTP method: $method");
        }

        // Store the route
        $this->routes[$method][$path] = $handler;
    }

    /**
     * Handle the incoming request.
     *
     * @param string $method The HTTP method of the request
     * @param string $path The path of the request
     * @return void
     * @throws Exception If the route is not found
     */
    public function handleRequest(string $method, string $path)
    {
        // Normalize method to uppercase
        $method = strtoupper($method);

        // Check if the route exists
        if (isset($this->routes[$method][$path])) {
            // Call the handler
            call_user_func($this->routes[$method][$path]);
        } else {
            // Route not found, throw an exception
            throw new Exception("Route not found for $method $path", 404);
        }
    }
}

// Example usage
try {
    $router = new Router();

    // Define routes
    $router->addRoute('GET', '/home', function() {
        echo "Welcome to the home page!";
    });

    $router->addRoute('POST', '/submit', function() {
        echo "Form submitted!";
    });

    // Simulate a request
    $router->handleRequest('GET', '/home'); // Outputs: Welcome to the home page!
    $router->handleRequest('POST', '/submit'); // Outputs: Form submitted!

    // Uncommenting the following line will throw an exception
    // $router->handleRequest('GET', '/nonexistent');

} catch (Exception $e) {
    // Handle exceptions gracefully
    http_response_code($e->getCode());
    echo $e->getMessage();
}
```
