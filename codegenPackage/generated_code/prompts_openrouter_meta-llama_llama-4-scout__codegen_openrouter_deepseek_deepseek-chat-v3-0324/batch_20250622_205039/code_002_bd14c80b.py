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
 * Router class for handling HTTP request routing.
 */
class Router
{
    /**
     * @var array Array of registered routes.
     */
    private $routes = [
        'GET' => [],
        'POST' => [],
        'PUT' => [],
        'DELETE' => [],
        'PATCH' => []
    ];

    /**
     * Register a GET route.
     *
     * @param string $uri The URI pattern to match
     * @param callable $handler The handler to execute when matched
     * @return void
     */
    public function get(string $uri, callable $handler): void
    {
        $this->registerRoute('GET', $uri, $handler);
    }

    /**
     * Register a POST route.
     *
     * @param string $uri The URI pattern to match
     * @param callable $handler The handler to execute when matched
     * @return void
     */
    public function post(string $uri, callable $handler): void
    {
        $this->registerRoute('POST', $uri, $handler);
    }

    /**
     * Register a PUT route.
     *
     * @param string $uri The URI pattern to match
     * @param callable $handler The handler to execute when matched
     * @return void
     */
    public function put(string $uri, callable $handler): void
    {
        $this->registerRoute('PUT', $uri, $handler);
    }

    /**
     * Register a DELETE route.
     *
     * @param string $uri The URI pattern to match
     * @param callable $handler The handler to execute when matched
     * @return void
     */
    public function delete(string $uri, callable $handler): void
    {
        $this->registerRoute('DELETE', $uri, $handler);
    }

    /**
     * Register a PATCH route.
     *
     * @param string $uri The URI pattern to match
     * @param callable $handler The handler to execute when matched
     * @return void
     */
    public function patch(string $uri, callable $handler): void
    {
        $this->registerRoute('PATCH', $uri, $handler);
    }

    /**
     * Register a route for any HTTP method.
     *
     * @param string $method The HTTP method
     * @param string $uri The URI pattern to match
     * @param callable $handler The handler to execute when matched
     * @return void
     */
    private function registerRoute(string $method, string $uri, callable $handler): void
    {
        $this->routes[$method][$this->normalizeUri($uri)] = $handler;
    }

    /**
     * Normalize the URI by removing trailing slashes.
     *
     * @param string $uri The URI to normalize
     * @return string Normalized URI
     */
    private function normalizeUri(string $uri): string
    {
        return rtrim($uri, '/');
    }

    /**
     * Dispatch the request to the appropriate route handler.
     *
     * @param string $method The HTTP method
     * @param string $uri The request URI
     * @return mixed The result of the route handler
     * @throws Exception When no matching route is found
     */
    public function dispatch(string $method, string $uri)
    {
        $method = strtoupper($method);
        $uri = $this->normalizeUri($uri);

        if (!isset($this->routes[$method])) {
            throw new Exception("Method not allowed", 405);
        }

        if (isset($this->routes[$method][$uri])) {
            return call_user_func($this->routes[$method][$uri]);
        }

        throw new Exception("Route not found", 404);
    }

    /**
     * Dispatch the request using current server variables.
     *
     * @return mixed The result of the route handler
     * @throws Exception When no matching route is found
     */
    public function dispatchFromGlobals()
    {
        $method = $_SERVER['REQUEST_METHOD'] ?? 'GET';
        $uri = $_SERVER['REQUEST_URI'] ?? '/';

        // Remove query string from URI
        if (($pos = strpos($uri, '?')) !== false) {
            $uri = substr($uri, 0, $pos);
        }

        return $this->dispatch($method, $uri);
    }
}
```
