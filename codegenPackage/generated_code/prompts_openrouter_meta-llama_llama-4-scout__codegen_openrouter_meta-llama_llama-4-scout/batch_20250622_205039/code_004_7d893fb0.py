"""
Generated Code Metadata:
========================
Original URL: https://stroyalentertainnmentrc.com
Prompt: Generate code for a simple PHP router that can map URLs to specific controller actions, following best practices outlined in the article on building a routing system in PHP.
Generated: DETERMINISTIC_7d893fb085763357
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
 * Router class to map URLs to specific controller actions.
 */
class Router
{
    /**
     * @var array Routes storage.
     */
    private $routes = [];

    /**
     * @var string Current URL.
     */
    private $currentUrl;

    /**
     * @var string Current method.
     */
    private $currentMethod;

    /**
     * Initialize the router.
     *
     * @param string $currentUrl Current URL.
     * @param string $currentMethod Current HTTP method.
     */
    public function __construct($currentUrl, $currentMethod)
    {
        $this->currentUrl = $currentUrl;
        $this->currentMethod = $currentMethod;
    }

    /**
     * Add a new route.
     *
     * @param string $method HTTP method.
     * @param string $uri URI.
     * @param callable $action Controller action.
     *
     * @return void
     */
    public function addRoute($method, $uri, $action)
    {
        $this->routes[] = [
            'method' => $method,
            'uri' => $uri,
            'action' => $action,
        ];
    }

    /**
     * Route the current request.
     *
     * @return mixed Controller action response.
     *
     * @throws Exception If no route found.
     */
    public function route()
    {
        foreach ($this->routes as $route) {
            if ($route['method'] === $this->currentMethod && $route['uri'] === $this->currentUrl) {
                return call_user_func($route['action']);
            }
        }

        throw new Exception('No route found for ' . $this->currentUrl);
    }
}

/**
 * Controller class with example actions.
 */
class Controller
{
    /**
     * Index action.
     *
     * @return string
     */
    public function index()
    {
        return 'Welcome to the index page!';
    }

    /**
     * Hello action.
     *
     * @param string $name Name.
     *
     * @return string
     */
    public function hello($name)
    {
        return 'Hello, ' . $name . '!';
    }
}

// Create a new router instance.
$router = new Router($_SERVER['REQUEST_URI'], $_SERVER['REQUEST_METHOD']);

// Create a new controller instance.
$controller = new Controller();

// Add routes.
$router->addRoute('GET', '/', [$controller, 'index']);
$router->addRoute('GET', '/hello/world', [$controller, 'hello']);

// Try to route the current request.
try {
    echo $router->route();
} catch (Exception $e) {
    http_response_code(404);
    echo 'Error: ' . $e->getMessage();
}
```
