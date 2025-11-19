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
 * Core Application Class
 */
class App {
    /**
     * @var array $routes 
     */
    private $routes = [];

    /**
     * @var array $middlewares 
     */
    private $middlewares = [];

    /**
     * Register a new route
     * 
     * @param string $method 
     * @param string $uri 
     * @param callable $callback 
     * @return void
     */
    public function route($method, $uri, $callback) {
        $this->routes[] = [
            'method' => $method,
            'uri' => $uri,
            'callback' => $callback,
        ];
    }

    /**
     * Register a new middleware
     * 
     * @param callable $middleware 
     * @return void
     */
    public function middleware($middleware) {
        $this->middlewares[] = $middleware;
    }

    /**
     * Run the application
     * 
     * @return void
     */
    public function run() {
        $uri = $_SERVER['REQUEST_URI'];
        $method = $_SERVER['REQUEST_METHOD'];

        foreach ($this->middlewares as $middleware) {
            $middleware();
        }

        foreach ($this->routes as $route) {
            if ($route['method'] === $method && $route['uri'] === $uri) {
                call_user_func($route['callback']);
                return;
            }
        }

        http_response_code(404);
        echo 'Route not found';
    }
}

/**
 * Request Helper Class
 */
class Request {
    /**
     * Get all input data
     * 
     * @return array
     */
    public static function all() {
        return array_merge($_GET, $_POST);
    }

    /**
     * Get a specific input value
     * 
     * @param string $key 
     * @param mixed $default 
     * @return mixed
     */
    public static function input($key, $default = null) {
        return self::all()[$key] ?? $default;
    }

    /**
     * Get the request headers
     * 
     * @return array
     */
    public static function headers() {
        $headers = [];
        foreach ($_SERVER as $key => $value) {
            if (strpos($key, 'HTTP_') === 0) {
                $headers[str_replace('HTTP_', '', $key)] = $value;
            }
        }
        return $headers;
    }
}

/**
 * Response Helper Class
 */
class Response {
    /**
     * Send a JSON response
     * 
     * @param mixed $data 
     * @param int $status 
     * @return void
     */
    public static function json($data, $status = 200) {
        http_response_code($status);
        header('Content-Type: application/json');
        echo json_encode($data);
    }

    /**
     * Send a plain text response
     * 
     * @param string $data 
     * @param int $status 
     * @return void
     */
    public static function text($data, $status = 200) {
        http_response_code($status);
        header('Content-Type: text/plain');
        echo $data;
    }
}

// Example usage:

$app = new App();

$app->route('GET', '/', function() {
    Response::json(['message' => 'Hello, World!']);
});

$app->middleware(function() {
    echo 'Middleware executed' . PHP_EOL;
});

$app->run();

```
