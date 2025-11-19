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
 * Mini PHP Framework for API Development
 * Author: [Your Name]
 * Description: A lightweight framework for building APIs with ease and customizability.
 * Version: 1.0.0
 */

// Autoloader for classes
spl_autoload_register(function ($class) {
    $file = __DIR__ . '/classes/' . $class . '.php';
    if (file_exists($file)) {
        require_once $file;
    }
});

// Error handling
set_exception_handler(function ($exception) {
    http_response_code(500);
    echo json_encode([
        'error' => true,
        'message' => $exception->getMessage(),
    ]);
});

set_error_handler(function ($errno, $errstr, $errfile, $errline) {
    http_response_code(500);
    echo json_encode([
        'error' => true,
        'message' => $errstr,
        'file' => $errfile,
        'line' => $errline,
    ]);
});

// Core Router Class
class Router
{
    private $routes = [];

    /**
     * Register a GET route
     * @param string $path
     * @param callable $callback
     */
    public function get($path, $callback)
    {
        $this->routes['GET'][$path] = $callback;
    }

    /**
     * Register a POST route
     * @param string $path
     * @param callable $callback
     */
    public function post($path, $callback)
    {
        $this->routes['POST'][$path] = $callback;
    }

    /**
     * Dispatch the request to the appropriate route
     */
    public function dispatch()
    {
        $method = $_SERVER['REQUEST_METHOD'];
        $path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

        if (isset($this->routes[$method][$path])) {
            try {
                echo json_encode($this->routes[$method][$path]());
            } catch (Exception $e) {
                http_response_code(500);
                echo json_encode(['error' => true, 'message' => $e->getMessage()]);
            }
        } else {
            http_response_code(404);
            echo json_encode(['error' => true, 'message' => 'Route not found']);
        }
    }
}

// Core Response Class
class Response
{
    /**
     * Send a JSON response
     * @param array $data
     * @param int $statusCode
     */
    public static function json(array $data, int $statusCode = 200)
    {
        http_response_code($statusCode);
        header('Content-Type: application/json');
        echo json_encode($data);
    }
}

// Core Request Class
class Request
{
    /**
     * Get all request data
     * @return array
     */
    public static function all()
    {
        return array_merge($_GET, $_POST, json_decode(file_get_contents('php://input'), true) ?? []);
    }

    /**
     * Get a specific request parameter
     * @param string $key
     * @param mixed $default
     * @return mixed
     */
    public static function input($key, $default = null)
    {
        $data = self::all();
        return $data[$key] ?? $default;
    }
}

// Initialize the Router
$router = new Router();

// Define routes
$router->get('/api/hello', function () {
    return ['message' => 'Hello, World!'];
});

$router->post('/api/echo', function () {
    $data = Request::all();
    return ['received' => $data];
});

// Dispatch the request
$router->dispatch();

?>
```
