"""
Generated Code Metadata:
========================
Original URL: https://stroyalentertainnmentrc.com
Prompt: Generate PHP code for a basic routing system that supports GET requests and returns a 404 error for unmatched routes using `http_response_code(404)`.
Generated: DETERMINISTIC_4ed8b384717cd447
Batch ID: 20250612_150119
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "http://localhost/router.php/contact`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost/router.php/`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost/`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost/router.php/unknown`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost/router.php/about`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php

/**
 * Basic Routing System
 *
 * This script provides a basic routing system that supports GET requests.
 * It returns a 404 error for unmatched routes.
 */

// Define routes
$routes = [
    '/' => function () {
        return 'Welcome to the home page!';
    },
    '/about' => function () {
        return 'This is the about page.';
    },
    '/contact' => function () {
        return 'Get in touch with us on the contact page.';
    },
];

/**
 * Route Request
 *
 * Route the incoming request to the corresponding handler.
 *
 * @param string $method The HTTP request method.
 * @param string $uri    The requested URI.
 */
function routeRequest($method, $uri, $routes) {
    // Check if the request method is supported
    if ($method !== 'GET') {
        http_response_code(405); // Method Not Allowed
        echo 'Method Not Allowed';
        return;
    }

    // Check if the route exists
    if (isset($routes[$uri])) {
        // Execute the route handler
        echo $routes[$uri]();
    } else {
        // Return 404 for unmatched routes
        http_response_code(404);
        echo 'Page Not Found';
    }
}

// Get the current URI
$uri = $_SERVER['REQUEST_URI'];

// Remove query string from URI
$uri = strtok($uri, '?');

// Get the request method
$method = $_SERVER['REQUEST_METHOD'];

// Route the request
routeRequest($method, $uri, $routes);

```

You can run this code by saving it to a PHP file (e.g., `router.php`) and accessing it through a web server. 

To test, you can use the following URLs:

- `http://localhost/router.php/`
- `http://localhost/router.php/about`
- `http://localhost/router.php/contact`
- `http://localhost/router.php/unknown`

Make sure to replace `http://localhost/router.php/` with your actual URL. 

For a production environment, consider using a more robust routing library or framework like Laravel or Symfony. 

Make sure to configure your server to handle URL rewriting if you want to use a cleaner URL structure (e.g., `http://localhost/` instead of `http://localhost/router.php/`). 

For development purposes, you can use the built-in PHP server:

```bash
php -S localhost:8000
```
