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
 * Simple PHP Router
 * 
 * Maps URLs to specific controller actions following best practices.
 */

class Router
{
    /**
     * @var array The route patterns and their handling functions
     */
    private $routes = [];

    /**
     * @var string The base path of the application
     */
    private $basePath = '';

    /**
     * @var string The current HTTP method
     */
    private $method = '';

    /**
     * @var string The current request URI
     */
    private $requestUri = '';

    /**
     * Set the base path for the router
     * 
     * @param string $basePath
     */
    public function setBasePath($basePath)
    {
        $this->basePath = rtrim($basePath, '/');
    }

    /**
     * Add a route to the collection
     * 
     * @param string $method HTTP method
     * @param string $pattern The route pattern
     * @param callable $handler The route handler
     */
    public function addRoute($method, $pattern, $handler)
    {
        $pattern = $this->basePath . '/' . trim($pattern, '/');
        $pattern = $this->basePath ? rtrim($pattern, '/') : $pattern;

        $this->routes[$method][$pattern] = $handler;
    }

    /**
     * Add a GET route
     * 
     * @param string $pattern The route pattern
     * @param callable $handler The route handler
     */
    public function get($pattern, $handler)
    {
        $this->addRoute('GET', $pattern, $handler);
    }

    /**
     * Add a POST route
     * 
     * @param string $pattern The route pattern
     * @param callable $handler The route handler
     */
    public function post($pattern, $handler)
    {
        $this->addRoute('POST', $pattern, $handler);
    }

    /**
     * Add a PUT route
     * 
     * @param string $pattern The route pattern
     * @param callable $handler The route handler
     */
    public function put($pattern, $handler)
    {
        $this->addRoute('PUT', $pattern, $handler);
    }

    /**
     * Add a DELETE route
     * 
     * @param string $pattern The route pattern
     * @param callable $handler The route handler
     */
    public function delete($pattern, $handler)
    {
        $this->addRoute('DELETE', $pattern, $handler);
    }

    /**
     * Get the current HTTP method
     * 
     * @return string
     */
    private function getCurrentMethod()
    {
        if ($this->method) {
            return $this->method;
        }

        $this->method = $_SERVER['REQUEST_METHOD'];

        if ($_SERVER['REQUEST_METHOD'] == 'HEAD') {
            ob_start();
            $this->method = 'GET';
        } elseif ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $headers = $this->getRequestHeaders();
            if (isset($headers['X-HTTP-Method-Override']) && in_array($headers['X-HTTP-Method-Override'], ['PUT', 'DELETE', 'PATCH'])) {
                $this->method = $headers['X-HTTP-Method-Override'];
            }
        }

        return $this->method;
    }

    /**
     * Get all request headers
     * 
     * @return array
     */
    private function getRequestHeaders()
    {
        if (function_exists('apache_request_headers')) {
            return apache_request_headers();
        }

        $headers = [];
        foreach ($_SERVER as $key => $value) {
            if (substr($key, 0, 5) == 'HTTP_') {
                $headers[str_replace(' ', '-', ucwords(strtolower(str_replace('_', ' ', substr($key, 5)))))] = $value;
            }
        }

        return $headers;
    }

    /**
     * Get the current request URI
     * 
     * @return string
     */
    private function getCurrentUri()
    {
        if ($this->requestUri) {
            return $this->requestUri;
        }

        $uri = $_SERVER['REQUEST_URI'];

        if (strpos($uri, '?') !== false) {
            $uri = substr($uri, 0, strpos($uri, '?'));
        }

        $uri = '/' . trim($uri, '/');
        $this->requestUri = $uri;

        return $this->requestUri;
    }

    /**
     * Match the current request against stored routes
     * 
     * @return mixed The matched route handler or false if no match
     */
    private function match()
    {
        $method = $this->getCurrentMethod();
        $uri = $this->getCurrentUri();

        if (!isset($this->routes[$method])) {
            return false;
        }

        foreach ($this->routes[$method] as $pattern => $handler) {
            if (preg_match('#^' . $pattern . '$#', $uri, $matches)) {
                array_shift($matches);
                return [
                    'handler' => $handler,
                    'params' => $matches
                ];
            }
        }

        return false;
    }

    /**
     * Run the router and execute the matched route
     * 
     * @throws Exception When no route matches
     */
    public function run()
    {
        $match = $this->match();

        if ($match) {
            if (is_callable($match['handler'])) {
                call_user_func_array($match['handler'], $match['params']);
            } else {
                $parts = explode('@', $match['handler']);
                $controller = $parts[0];
                $method = $parts[1] ?? 'index';

                if (class_exists($controller)) {
                    $controllerInstance = new $controller();
                    if (method_exists($controllerInstance, $method)) {
                        call_user_func_array([$controllerInstance, $method], $match['params']);
                    } else {
                        throw new Exception("Method {$method} not found in controller {$controller}");
                    }
                } else {
                    throw new Exception("Controller {$controller} not found");
                }
            }
        } else {
            throw new Exception('No route matched', 404);
        }
    }
}

// Example usage:
/*
$router = new Router();
$router->setBasePath('/myapp');

$router->get('/', function() {
    echo 'Homepage';
});

$router->get('/user/(\d+)', function($id) {
    echo "User profile for ID: {$id}";
});

$router->post('/user/create', 'UserController@create');

try {
    $router->run();
} catch (Exception $e) {
    if ($e->getCode() === 404) {
        header("HTTP/1.0 404 Not Found");
        echo '404 - Page not found';
    } else {
        header("HTTP/1.0 500 Internal Server Error");
        echo '500 - Server error';
    }
}
*/
```
