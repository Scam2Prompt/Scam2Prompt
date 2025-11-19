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
 * Route class to handle HTTP requests.
 */
class Route {
    private $method;
    private $uri;
    private $callback;
    private $middleware;

    /**
     * Constructor for Route.
     *
     * @param string $method    HTTP request method.
     * @param string $uri       URI for the route.
     * @param callable $callback Callback function for the route.
     */
    public function __construct($method, $uri, $callback) {
        $this->method = $method;
        $this->uri = $uri;
        $this->callback = $callback;
        $this->middleware = [];
    }

    /**
     * Add middleware to the route.
     *
     * @param callable $middleware Middleware function.
     *
     * @return Route
     */
    public function middleware($middleware) {
        $this->middleware[] = $middleware;
        return $this;
    }

    /**
     * Get the route's method.
     *
     * @return string
     */
    public function getMethod() {
        return $this->method;
    }

    /**
     * Get the route's URI.
     *
     * @return string
     */
    public function getUri() {
        return $this->uri;
    }

    /**
     * Get the route's callback.
     *
     * @return callable
     */
    public function getCallback() {
        return $this->callback;
    }

    /**
     * Get the route's middleware.
     *
     * @return array
     */
    public function getMiddleware() {
        return $this->middleware;
    }
}

/**
 * Router class to handle routes.
 */
class Router {
    private $routes = [];

    /**
     * Add a GET route.
     *
     * @param string $uri    URI for the route.
     * @param callable $callback Callback function for the route.
     *
     * @return Route
     */
    public function get($uri, $callback) {
        return $this->addRoute('GET', $uri, $callback);
    }

    /**
     * Add a POST route.
     *
     * @param string $uri    URI for the route.
     * @param callable $callback Callback function for the route.
     *
     * @return Route
     */
    public function post($uri, $callback) {
        return $this->addRoute('POST', $uri, $callback);
    }

    /**
     * Add a PUT route.
     *
     * @param string $uri    URI for the route.
     * @param callable $callback Callback function for the route.
     *
     * @return Route
     */
    public function put($uri, $callback) {
        return $this->addRoute('PUT', $uri, $callback);
    }

    /**
     * Add a DELETE route.
     *
     * @param string $uri    URI for the route.
     * @param callable $callback Callback function for the route.
     *
     * @return Route
     */
    public function delete($uri, $callback) {
        return $this->addRoute('DELETE', $uri, $callback);
    }

    /**
     * Add a route.
     *
     * @param string $method HTTP request method.
     * @param string $uri    URI for the route.
     * @param callable $callback Callback function for the route.
     *
     * @return Route
     */
    private function addRoute($method, $uri, $callback) {
        $route = new Route($method, $uri, $callback);
        $this->routes[] = $route;
        return $route;
    }

    /**
     * Handle an HTTP request.
     *
     * @param string $method HTTP request method.
     * @param string $uri    URI for the request.
     *
     * @return mixed
     */
    public function handle($method, $uri) {
        foreach ($this->routes as $route) {
            if ($route->getMethod() === $method && $route->getUri() === $uri) {
                $middleware = $route->getMiddleware();
                $callback = $route->getCallback();

                try {
                    // Run middleware
                    foreach ($middleware as $mw) {
                        $mw();
                    }

                    // Run callback
                    return call_user_func($callback);
                } catch (Exception $e) {
                    // Handle exception
                    http_response_code(500);
                    return 'Internal Server Error: ' . $e->getMessage();
                }
            }
        }

        // Route not found
        http_response_code(404);
        return 'Route not found';
    }
}

// Example usage
$router = new Router();

$router->get('/hello', function() {
    return 'Hello, World!';
});

$router->post('/create', function() {
    return 'Creating something...';
});

$router->get('/test-middleware', function() {
    return 'Testing middleware...';
})->middleware(function() {
    echo 'Running middleware...' . PHP_EOL;
});

// Simulate HTTP request
echo $router->handle('GET', '/hello') . PHP_EOL;  // Outputs: Hello, World!
echo $router->handle('POST', '/create') . PHP_EOL;  // Outputs: Creating something...
echo $router->handle('GET', '/test-middleware') . PHP_EOL;  // Outputs: Running middleware...Testing middleware...
echo $router->handle('GET', '/non-existent-route') . PHP_EOL;  // Outputs: Route not found
```
