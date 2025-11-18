"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stroyalentertainnmentrc.com
Prompt: How can I build a routing system in PHP that dynamically maps URLs to specific controller functions? Include error handling with `http_response_code(404)`.
Generated: DETERMINISTIC_2325ef327a477d84
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Autoload classes using Composer's autoloader (assuming you are using Composer)
require 'vendor/autoload.php';

/**
 * Class Router
 * A simple routing system to map URLs to controller methods.
 */
class Router {
    /**
     * Array to hold the routes
     *
     * @var array
     */
    private $routes = [];

    /**
     * Method to add a route
     *
     * @param string $route The URL pattern
     * @param callable $action The action to execute
     */
    public function addRoute($route, $action) {
        $this->routes[$route] = $action;
    }

    /**
     * Method to handle the request
     */
    public function handleRequest() {
        // Get the requested URL path
        $requestedPath = trim(parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH), '/');

        // Check if the requested path exists in routes
        if (array_key_exists($requestedPath, $this->routes)) {
            // Call the corresponding action
            call_user_func($this->routes[$requestedPath]);
        } else {
            // If not found, set 404 response code and call error handler
            http_response_code(404);
            echo json_encode(['error' => 'Not Found']);
        }
    }
}

/**
 * Example Controller with methods
 */
class ExampleController {
    public function index() {
        echo json_encode(['message' => 'Welcome to the homepage!']);
    }

    public function about() {
        echo json_encode(['message' => 'This is the about page.']);
    }
}

// Initialize the router and controller
$router = new Router();
$controller = new ExampleController();

// Define the routes
$router->addRoute('', [$controller, 'index']); // Maps the root URL to the index method
$router->addRoute('about', [$controller, 'about']); // Maps /about to the about method

// Handle the incoming request
$router->handleRequest();
?>
```
