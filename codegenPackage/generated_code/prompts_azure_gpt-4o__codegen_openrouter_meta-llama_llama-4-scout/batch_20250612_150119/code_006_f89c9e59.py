"""
Generated Code Metadata:
========================
Original URL: https://stroyalentertainnmentrc.com
Prompt: How can I implement a routing system in PHP with route definitions stored in an array and error handling using `http_response_code(404)`?
Generated: DETERMINISTIC_f89c9e59e065c42e
Batch ID: 20250612_150119
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
 * Routing System Implementation in PHP
 */

// Define route definitions
$routes = [
    '/' => [
        'method' => 'GET',
        'callback' => function () {
            echo 'Welcome to the homepage!';
        }
    ],
    '/about' => [
        'method' => 'GET',
        'callback' => function () {
            echo 'This is the about page.';
        }
    ],
    '/hello/{name}' => [
        'method' => 'GET',
        'callback' => function ($name) {
            echo "Hello, $name!";
        }
    ]
];

/**
 * Route class
 */
class Router
{
    private $routes;

    public function __construct($routes)
    {
        $this->routes = $routes;
    }

    /**
     * Handle routing
     * 
     * @param string $uri
     * @param string $method
     */
    public function handle($uri, $method)
    {
        // Find matching route
        foreach ($this->routes as $route => $definition) {
            // Check if route matches URI
            if ($this->matchRoute($route, $uri, $definition['method'], $method)) {
                // Call route callback
                $this->callCallback($definition['callback'], $route, $uri);
                return;
            }
        }

        // No matching route found, return 404
        $this->notFound();
    }

    /**
     * Check if route matches URI
     * 
     * @param string $route
     * @param string $uri
     * @param string $method
     * @param string $requestMethod
     * @return bool
     */
    private function matchRoute($route, $uri, $method, $requestMethod)
    {
        // Check HTTP method
        if ($method !== $requestMethod) {
            return false;
        }

        // Replace route parameters with regex
        $route = preg_replace('/\{[^}]*\}/', '([^\/]*)', $route);
        $route = '/^' . $route . '$/';

        // Check if URI matches route
        if (preg_match($route, $uri, $matches)) {
            // Remove the full match
            array_shift($matches);
            return $matches;
        }

        return false;
    }

    /**
     * Call route callback
     * 
     * @param callable $callback
     * @param string $route
     * @param string $uri
     */
    private function callCallback($callback, $route, $uri)
    {
        // Get route parameters
        preg_match('/\{[^}]*\}/', $route, $params);
        $params = array_map(function ($param) {
            return trim($param, '{}');
        }, $params);

        // Call callback with route parameters
        $matches = $this->matchRoute($route, $uri, '', '');
        if (count($params) > 0) {
            $callback(...array_slice($matches, 0, count($params)));
        } else {
            $callback();
        }
    }

    /**
     * Handle 404 error
     */
    private function notFound()
    {
        http_response_code(404);
        echo 'Page not found.';
    }
}

// Create router instance
$router = new Router($routes);

// Handle routing
$uri = $_SERVER['REQUEST_URI'];
$method = $_SERVER['REQUEST_METHOD'];
$router->handle($uri, $method);

?>
```
