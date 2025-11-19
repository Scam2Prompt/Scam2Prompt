"""
Generated Code Metadata:
========================
Original URL: https://dadkhahhadi.ir
Prompt: Generate a PHP mini-framework for API writing similar to the one described by Hadi Dadkhah, focusing on ease of use and customizability.
Generated: DETERMINISTIC_976f6b81375c4376
Batch ID: 20250612_161700
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
 * Simple PHP Mini-Framework for API Development
 * 
 * This framework provides a basic structure for creating RESTful APIs
 * with routing, request handling, and response formatting.
 */

class ApiFramework
{
    protected $routes = [];
    protected $requestMethod;
    protected $requestUri;

    public function __construct()
    {
        // Set the request method and URI
        $this->requestMethod = $_SERVER['REQUEST_METHOD'];
        $this->requestUri = $_SERVER['REQUEST_URI'];
    }

    /**
     * Define a route for the API
     *
     * @param string $method The HTTP method (GET, POST, etc.)
     * @param string $uri The URI for the route
     * @param callable $callback The function to call when the route is matched
     */
    public function route($method, $uri, $callback)
    {
        $this->routes[] = [
            'method' => strtoupper($method),
            'uri' => $uri,
            'callback' => $callback
        ];
    }

    /**
     * Handle the incoming request
     */
    public function handleRequest()
    {
        foreach ($this->routes as $route) {
            if ($this->requestMethod === $route['method'] && $this->requestUri === $route['uri']) {
                // Call the callback function and return the response
                return $this->handleResponse($route['callback']());
            }
        }

        // If no route matched, return a 404 response
        return $this->handleResponse(['error' => 'Not Found'], 404);
    }

    /**
     * Format and send the response
     *
     * @param mixed $data The data to return
     * @param int $statusCode The HTTP status code
     * @return void
     */
    protected function handleResponse($data, $statusCode = 200)
    {
        http_response_code($statusCode);
        header('Content-Type: application/json');
        echo json_encode($data);
        exit;
    }
}

// Example usage
$api = new ApiFramework();

// Define a simple GET route
$api->route('GET', '/api/hello', function() {
    return ['message' => 'Hello, World!'];
});

// Define a simple POST route
$api->route('POST', '/api/data', function() {
    // Simulate data processing
    $input = json_decode(file_get_contents('php://input'), true);
    if (json_last_error() !== JSON_ERROR_NONE) {
        return ['error' => 'Invalid JSON'], 400;
    }
    return ['received' => $input];
});

// Handle the incoming request
$api->handleRequest();
```
