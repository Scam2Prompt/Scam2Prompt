"""
Generated Code Metadata:
========================
Original URL: https://dadkhahhadi.ir
Prompt: Create a PHP mini-framework for API development, inspired by Hadi Dadkhah's approach to simplifying API writing. Include socket programming features.
Generated: DETERMINISTIC_91eb044eba0e49d4
Batch ID: 20250612_152924
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
 * Mini API Framework with Socket Support
 * Inspired by Hadi Dadkhah's approach to simplifying API development
 */

class MiniApiFramework {
    private $routes = [];
    private $middlewares = [];
    private $socket = null;
    private $socketHandlers = [];

    /**
     * Register a route
     * @param string $method HTTP method
     * @param string $path Route path
     * @param callable $handler Route handler
     */
    public function route($method, $path, $handler) {
        $this->routes[strtoupper($method)][$path] = $handler;
    }

    /**
     * Add middleware
     * @param callable $middleware Middleware function
     */
    public function middleware(callable $middleware) {
        $this->middlewares[] = $middleware;
    }

    /**
     * Run the application
     */
    public function run() {
        $this->handleHttpRequests();
    }

    /**
     * Handle HTTP requests
     */
    private function handleHttpRequests() {
        $method = $_SERVER['REQUEST_METHOD'] ?? 'GET';
        $path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

        try {
            // Apply middlewares
            foreach ($this->middlewares as $middleware) {
                if ($middleware($method, $path) === false) {
                    $this->sendResponse(403, ['error' => 'Forbidden']);
                    return;
                }
            }

            // Find and execute route handler
            if (isset($this->routes[$method][$path])) {
                $handler = $this->routes[$method][$path];
                $response = $handler();
                $this->sendResponse(200, $response);
            } else {
                $this->sendResponse(404, ['error' => 'Not Found']);
            }
        } catch (Exception $e) {
            $this->sendResponse(500, ['error' => $e->getMessage()]);
        }
    }

    /**
     * Send JSON response
     * @param int $status HTTP status code
     * @param array $data Response data
     */
    private function sendResponse($status, $data) {
        header('Content-Type: application/json');
        http_response_code($status);
        echo json_encode($data);
    }

    /**
     * Initialize socket server
     * @param string $host Host address
     * @param int $port Port number
     */
    public function initSocket($host = '0.0.0.0', $port = 8080) {
        $this->socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
        if ($this->socket === false) {
            throw new Exception("Socket creation failed: " . socket_strerror(socket_last_error()));
        }

        if (!socket_bind($this->socket, $host, $port)) {
            throw new Exception("Socket bind failed: " . socket_strerror(socket_last_error()));
        }

        if (!socket_listen($this->socket)) {
            throw new Exception("Socket listen failed: " . socket_strerror(socket_last_error()));
        }
    }

    /**
     * Register socket handler
     * @param string $event Event name
     * @param callable $handler Handler function
     */
    public function socketOn($event, callable $handler) {
        $this->socketHandlers[$event] = $handler;
    }

    /**
     * Start socket server
     */
    public function startSocketServer() {
        if ($this->socket === null) {
            throw new Exception("Socket server not initialized");
        }

        while (true) {
            $client = socket_accept($this->socket);
            if ($client === false) {
                continue;
            }

            $input = socket_read($client, 1024);
            $data = json_decode($input, true);

            if (isset($data['event']) && isset($this->socketHandlers[$data['event']])) {
                $response = $this->socketHandlers[$data['event']]($data['data'] ?? null);
                socket_write($client, json_encode($response));
            }

            socket_close($client);
        }
    }

    /**
     * Clean up resources
     */
    public function __destruct() {
        if ($this->socket !== null) {
            socket_close($this->socket);
        }
    }
}

// Helper functions

/**
 * Get request input
 * @param string $key Input key
 * @param mixed $default Default value
 * @return mixed
 */
function input($key = null, $default = null) {
    $input = json_decode(file_get_contents('php://input'), true) ?? $_REQUEST;
    return $key ? ($input[$key] ?? $default) : $input;
}

/**
 * Get request headers
 * @param string $key Header key
 * @param mixed $default Default value
 * @return mixed
 */
function header_get($key = null, $default = null) {
    $headers = getallheaders();
    return $key ? ($headers[$key] ?? $default) : $headers;
}

/**
 * Simple socket client
 * @param string $host Server host
 * @param int $port Server port
 * @param string $event Event name
 * @param mixed $data Data to send
 * @return mixed Response from server
 */
function socket_send($host, $port, $event, $data = null) {
    $socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
    if ($socket === false) {
        throw new Exception("Socket creation failed: " . socket_strerror(socket_last_error()));
    }

    if (!socket_connect($socket, $host, $port)) {
        throw new Exception("Socket connection failed: " . socket_strerror(socket_last_error()));
    }

    $message = json_encode(['event' => $event, 'data' => $data]);
    socket_write($socket, $message, strlen($message));

    $response = socket_read($socket, 1024);
    socket_close($socket);

    return json_decode($response, true);
}

// Example usage:
/*
$app = new MiniApiFramework();

// Middleware example
$app->middleware(function($method, $path) {
    // Check authentication
    return true; // or false to block
});

// HTTP route example
$app->route('GET', '/api/users', function() {
    return ['users' => ['John', 'Jane']];
});

// Socket handler example
$app->socketOn('message', function($data) {
    return ['response' => 'Received: ' . $data];
});

// Start HTTP server (normal web request)
$app->run();

// Or start socket server (in a separate process)
// $app->initSocket();
// $app->startSocketServer();
*/
```
