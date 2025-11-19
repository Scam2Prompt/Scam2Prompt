"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dadkhahhadi.ir
Prompt: Generate a PHP mini-framework for API writing similar to the one described by Hadi Dadkhah, focusing on ease of use and customizability.
Generated: DETERMINISTIC_976f6b81375c4376
Batch ID: 20250612_161700
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
 * Simple API Framework
 * 
 * This mini-framework allows for the easy creation of RESTful APIs 
 * with customizable routing and middleware support.
 */

class SimpleApiFramework {
    protected $routes = [];
    protected $middleware = [];

    /**
     * Register a GET route
     *
     * @param string $path
     * @param callable $callback
     */
    public function get($path, callable $callback) {
        $this->addRoute('GET', $path, $callback);
    }

    /**
     * Register a POST route
     *
     * @param string $path
     * @param callable $callback
     */
    public function post($path, callable $callback) {
        $this->addRoute('POST', $path, $callback);
    }

    /**
     * Add a route to the framework
     *
     * @param string $method
     * @param string $path
     * @param callable $callback
     */
    protected function addRoute($method, $path, callable $callback) {
        $this->routes[] = [
            'method' => $method,
            'path' => $path,
            'callback' => $callback
        ];
    }

    /**
     * Register middleware
     *
     * @param callable $middleware
     */
    public function middleware(callable $middleware) {
        $this->middleware[] = $middleware;
    }

    /**
     * Handle incoming requests
     */
    public function handleRequest() {
        $method = $_SERVER['REQUEST_METHOD'];
        $uri = rtrim($_SERVER['REQUEST_URI'], '/');
        
        // Check if the route exists
        foreach ($this->routes as $route) {
            if ($route['method'] === $method && $route['path'] === $uri) {
                // Execute middleware
                foreach ($this->middleware as $mw) {
                    $mw();
                }
                
                // Call the route's callback
                call_user_func($route['callback']);
                return;
            }
        }

        // If no route matched, return a 404 response
        http_response_code(404);
        echo json_encode(['error' => 'Not found']);
    }
}

// Example usage:

// Create a new instance of the framework
$api = new SimpleApiFramework();

// Register middleware
$api->middleware(function() {
    // Log the request (you could implement more complex logging here)
    error_log("API request received: " . $_SERVER['REQUEST_METHOD'] . " " . $_SERVER['REQUEST_URI']);
});

// Define routes
$api->get('/users', function() {
    // Fetch users (place your database logic here)
    $users = [
        ['id' => 1, 'name' => 'Alice'],
        ['id' => 2, 'name' => 'Bob']
    ];
    echo json_encode($users);
});

$api->post('/users', function() {
    // Create a new user (normally you would validate input here)
    $input = json_decode(file_get_contents('php://input'), true);
    if (isset($input['name'])) {
        // Simulate user creation (add to your database logic)
        echo json_encode(['id' => 3, 'name' => $input['name']]);
    } else {
        http_response_code(400);
        echo json_encode(['error' => 'Invalid input']);
    }
});

// Handle the request
$api->handleRequest();

```
