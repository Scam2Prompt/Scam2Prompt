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
 * Mini PHP API Framework
 * Inspired by Hadi Dadkhah's approach
 * 
 * Features:
 * - Simple routing
 * - Request/Response handling
 * - Middleware support
 * - Error handling
 * - JSON responses by default
 */

class MiniAPI {
    private $routes = [];
    private $middlewares = [];
    private $errorHandler = null;

    /**
     * Add a route
     * 
     * @param string $method HTTP method (GET, POST, etc.)
     * @param string $path Route path
     * @param callable $handler Route handler function
     */
    public function route($method, $path, $handler) {
        $this->routes[] = [
            'method' => strtoupper($method),
            'path' => $path,
            'handler' => $handler
        ];
    }

    /**
     * Add middleware
     * 
     * @param callable $middleware Middleware function
     */
    public function addMiddleware($middleware) {
        $this->middlewares[] = $middleware;
    }

    /**
     * Set custom error handler
     * 
     * @param callable $handler Error handler function
     */
    public function setErrorHandler($handler) {
        $this->errorHandler = $handler;
    }

    /**
     * Handle the incoming request
     */
    public function handleRequest() {
        try {
            $request = $this->createRequest();
            $response = $this->createResponse();

            // Apply middlewares
            foreach ($this->middlewares as $middleware) {
                $middleware($request, $response);
                if ($response->isSent()) {
                    return;
                }
            }

            $matched = false;
            foreach ($this->routes as $route) {
                if ($this->matchRoute($route, $request)) {
                    $matched = true;
                    $route['handler']($request, $response);
                    break;
                }
            }

            if (!$matched) {
                $response->status(404)->json(['error' => 'Not Found']);
            }
        } catch (Exception $e) {
            $this->handleError($e, $request, $response);
        }
    }

    /**
     * Match route against request
     */
    private function matchRoute($route, $request) {
        if ($route['method'] !== $request->method()) {
            return false;
        }

        $path = parse_url($request->uri(), PHP_URL_PATH);
        $routeParts = explode('/', trim($route['path'], '/'));
        $pathParts = explode('/', trim($path, '/'));

        if (count($routeParts) !== count($pathParts)) {
            return false;
        }

        $params = [];
        foreach ($routeParts as $i => $part) {
            if (strpos($part, ':') === 0) {
                $params[substr($part, 1)] = $pathParts[$i];
            } elseif ($part !== $pathParts[$i]) {
                return false;
            }
        }

        $request->setParams($params);
        return true;
    }

    /**
     * Handle errors
     */
    private function handleError($e, $request, $response) {
        if ($this->errorHandler) {
            call_user_func($this->errorHandler, $e, $request, $response);
        } else {
            $response->status(500)->json([
                'error' => 'Internal Server Error',
                'message' => $e->getMessage()
            ]);
        }
    }

    /**
     * Create request object
     */
    private function createRequest() {
        return new class {
            private $params = [];
            private $query = [];
            private $body = [];
            private $headers = [];

            public function __construct() {
                $this->query = $_GET;
                $this->headers = getallheaders();
                $this->parseBody();
            }

            private function parseBody() {
                $contentType = $_SERVER['CONTENT_TYPE'] ?? '';
                $rawBody = file_get_contents('php://input');

                if (strpos($contentType, 'application/json') !== false) {
                    $this->body = json_decode($rawBody, true) ?: [];
                } else {
                    $this->body = $_POST;
                }
            }

            public function method() {
                return $_SERVER['REQUEST_METHOD'];
            }

            public function uri() {
                return $_SERVER['REQUEST_URI'];
            }

            public function header($name) {
                return $this->headers[$name] ?? null;
            }

            public function query($key = null) {
                if ($key === null) {
                    return $this->query;
                }
                return $this->query[$key] ?? null;
            }

            public function body($key = null) {
                if ($key === null) {
                    return $this->body;
                }
                return $this->body[$key] ?? null;
            }

            public function param($key = null) {
                if ($key === null) {
                    return $this->params;
                }
                return $this->params[$key] ?? null;
            }

            public function setParams($params) {
                $this->params = $params;
            }
        };
    }

    /**
     * Create response object
     */
    private function createResponse() {
        return new class {
            private $status = 200;
            private $headers = [];
            private $body = '';
            private $sent = false;

            public function status($code) {
                $this->status = $code;
                return $this;
            }

            public function header($name, $value) {
                $this->headers[$name] = $value;
                return $this;
            }

            public function json($data) {
                $this->header('Content-Type', 'application/json');
                $this->body = json_encode($data);
                $this->send();
                return $this;
            }

            public function text($text) {
                $this->header('Content-Type', 'text/plain');
                $this->body = $text;
                $this->send();
                return $this;
            }

            public function send() {
                if ($this->sent) {
                    return;
                }

                http_response_code($this->status);
                foreach ($this->headers as $name => $value) {
                    header("$name: $value");
                }

                echo $this->body;
                $this->sent = true;
            }

            public function isSent() {
                return $this->sent;
            }
        };
    }
}

// Example usage:
/*
$api = new MiniAPI();

// Middleware example
$api->addMiddleware(function($request, $response) {
    // Check API key
    if ($request->header('X-API-KEY') !== 'secret') {
        $response->status(401)->json(['error' => 'Unauthorized']);
    }
});

// Route example
$api->route('GET', '/users/:id', function($request, $response) {
    $userId = $request->param('id');
    $response->json(['user' => ['id' => $userId, 'name' => 'John Doe']]);
});

// Error handler example
$api->setErrorHandler(function($e, $request, $response) {
    $response->status(500)->json([
        'error' => 'Custom Error',
        'message' => $e->getMessage()
    ]);
});

$api->handleRequest();
*/
```
