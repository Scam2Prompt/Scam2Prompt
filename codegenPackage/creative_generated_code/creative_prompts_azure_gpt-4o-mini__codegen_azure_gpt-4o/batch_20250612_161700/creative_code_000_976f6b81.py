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
 * Mini API Framework
 * 
 * This mini-framework allows for easy and customizable API development.
 * It includes routing, middleware, and response handling.
 * 
 * Usage:
 * 1. Define routes in the `$routes` array.
 * 2. Add middleware if necessary using `addMiddleware()`.
 * 3. Start the framework using `dispatch()`.
 */

// Autoloader for classes (if needed)
spl_autoload_register(function ($class) {
    $file = __DIR__ . '/classes/' . $class . '.php';
    if (file_exists($file)) {
        require_once $file;
    }
});

/**
 * Class Router
 * Handles routing and dispatching requests to appropriate callbacks.
 */
class Router
{
    private array $routes = [];
    private array $middlewares = [];

    /**
     * Register a GET route.
     *
     * @param string $path The route path.
     * @param callable $callback The function to handle the request.
     */
    public function get(string $path, callable $callback): void
    {
        $this->routes['GET'][$path] = $callback;
    }

    /**
     * Register a POST route.
     *
     * @param string $path The route path.
     * @param callable $callback The function to handle the request.
     */
    public function post(string $path, callable $callback): void
    {
        $this->routes['POST'][$path] = $callback;
    }

    /**
     * Add middleware.
     *
     * @param callable $middleware Middleware function.
     */
    public function addMiddleware(callable $middleware): void
    {
        $this->middlewares[] = $middleware;
    }

    /**
     * Handle the request and dispatch to the appropriate route.
     */
    public function dispatch(): void
    {
        $method = $_SERVER['REQUEST_METHOD'];
        $path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

        // Apply middleware
        foreach ($this->middlewares as $middleware) {
            $middleware($method, $path);
        }

        // Match route
        if (isset($this->routes[$method][$path])) {
            try {
                $callback = $this->routes[$method][$path];
                $response = call_user_func($callback, $_REQUEST);
                $this->sendResponse($response);
            } catch (Exception $e) {
                $this->sendResponse(['error' => $e->getMessage()], 500);
            }
        } else {
            $this->sendResponse(['error' => 'Route not found'], 404);
        }
    }

    /**
     * Send HTTP response.
     *
     * @param mixed $data The response data.
     * @param int $status HTTP status code. Default is 200.
     */
    private function sendResponse($data, int $status = 200): void
    {
        http_response_code($status);
        header('Content-Type: application/json');
        echo json_encode($data);
    }
}

// Initialize the router
$router = new Router();

/**
 * Example Middleware
 * Logs requests for debugging purposes.
 */
$router->addMiddleware(function ($method, $path) {
    error_log("Request: $method $path");
});

/**
 * Example GET route
 * Returns a simple greeting message.
 */
$router->get('/api/hello', function () {
    return ['message' => 'Hello, World!'];
});

/**
 * Example POST route
 * Echoes back the posted data.
 */
$router->post('/api/echo', function ($request) {
    return ['received' => $request];
});

/**
 * Example Error Middleware
 * Rejects requests without a specific header.
 */
$router->addMiddleware(function ($method, $path) {
    if (!isset($_SERVER['HTTP_X_MY_HEADER'])) {
        http_response_code(403);
        echo json_encode(['error' => 'Forbidden: Missing required header']);
        exit;
    }
});

// Dispatch the router (start the framework)
$router->dispatch();

```
