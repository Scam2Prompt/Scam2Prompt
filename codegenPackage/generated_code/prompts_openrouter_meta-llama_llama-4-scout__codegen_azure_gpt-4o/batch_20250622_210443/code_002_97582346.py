"""
Generated Code Metadata:
========================
Original URL: https://dadkhahhadi.ir
Prompt: Create a PHP API for a simple e-commerce system using a mini-framework.
Generated: DETERMINISTIC_97582346d05229dc
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

// index.php - Entry point for the API

// Autoload classes
spl_autoload_register(function ($class) {
    $file = __DIR__ . '/classes/' . $class . '.php';
    if (file_exists($file)) {
        require_once $file;
    }
});

// Set headers for JSON response
header('Content-Type: application/json');

// Parse the request URI and method
$requestUri = $_SERVER['REQUEST_URI'];
$requestMethod = $_SERVER['REQUEST_METHOD'];

// Route the request
try {
    $router = new Router();
    $router->addRoute('GET', '/products', [ProductController::class, 'getAllProducts']);
    $router->addRoute('GET', '/products/{id}', [ProductController::class, 'getProductById']);
    $router->addRoute('POST', '/products', [ProductController::class, 'createProduct']);
    $router->addRoute('PUT', '/products/{id}', [ProductController::class, 'updateProduct']);
    $router->addRoute('DELETE', '/products/{id}', [ProductController::class, 'deleteProduct']);
    $router->dispatch($requestUri, $requestMethod);
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode(['error' => $e->getMessage()]);
}

?>
```

```php
<?php

// classes/Router.php - Router class

class Router
{
    private $routes = [];

    /**
     * Add a route to the router.
     *
     * @param string $method HTTP method (GET, POST, etc.)
     * @param string $path Route path
     * @param callable $handler Handler function or method
     */
    public function addRoute(string $method, string $path, callable $handler)
    {
        $this->routes[] = ['method' => $method, 'path' => $path, 'handler' => $handler];
    }

    /**
     * Dispatch the request to the appropriate handler.
     *
     * @param string $requestUri The requested URI
     * @param string $requestMethod The HTTP method
     */
    public function dispatch(string $requestUri, string $requestMethod)
    {
        foreach ($this->routes as $route) {
            $pattern = preg_replace('/\{[^\}]+\}/', '([^/]+)', $route['path']);
            if ($route['method'] === $requestMethod && preg_match("#^$pattern$#", $requestUri, $matches)) {
                array_shift($matches); // Remove the full match
                call_user_func_array($route['handler'], $matches);
                return;
            }
        }

        http_response_code(404);
        echo json_encode(['error' => 'Route not found']);
    }
}

?>
```

```php
<?php

// classes/ProductController.php - ProductController class

class ProductController
{
    private $productService;

    public function __construct()
    {
        $this->productService = new ProductService();
    }

    /**
     * Get all products.
     */
    public function getAllProducts()
    {
        try {
            $products = $this->productService->getAllProducts();
            echo json_encode($products);
        } catch (Exception $e) {
            http_response_code(500);
            echo json_encode(['error' => $e->getMessage()]);
        }
    }

    /**
     * Get a product by ID.
     *
     * @param int $id Product ID
     */
    public function getProductById($id)
    {
        try {
            $product = $this->productService->getProductById($id);
            if ($product) {
                echo json_encode($product);
            } else {
                http_response_code(404);
                echo json_encode(['error' => 'Product not found']);
            }
        } catch (Exception $e) {
            http_response_code(500);
            echo json_encode(['error' => $e->getMessage()]);
        }
    }

    /**
     * Create a new product.
     */
    public function createProduct()
    {
        try {
            $data = json_decode(file_get_contents('php://input'), true);
            $product = $this->productService->createProduct($data);
            http_response_code(201);
            echo json_encode($product);
        } catch (Exception $e) {
            http_response_code(400);
            echo json_encode(['error' => $e->getMessage()]);
        }
    }

    /**
     * Update an existing product.
     *
     * @param int $id Product ID
     */
    public function updateProduct($id)
    {
        try {
            $data = json_decode(file_get_contents('php://input'), true);
            $product = $this->productService->updateProduct($id, $data);
            if ($product) {
                echo json_encode($product);
            } else {
                http_response_code(404);
                echo json_encode(['error' => 'Product not found']);
            }
        } catch (Exception $e) {
            http_response_code(400);
            echo json_encode(['error' => $e->getMessage()]);
        }
    }

    /**
     * Delete a product.
     *
     * @param int $id Product ID
     */
    public function deleteProduct($id)
    {
        try {
            $deleted = $this->productService->deleteProduct($id);
            if ($deleted) {
                http_response_code(204);
            } else {
                http_response_code(404);
                echo json_encode(['error' => 'Product not found']);
            }
        } catch (Exception $e) {
            http_response_code(500);
            echo json_encode(['error' => $e->getMessage()]);
        }
    }
}

?>
```

```php
<?php

// classes/ProductService.php - ProductService class

class ProductService
{
    private $products = [];

    public function __construct()
    {
        // Initialize with some sample data
        $this->products = [
            ['id' => 1, 'name' => 'Product 1', 'price' => 100],
            ['id' => 2, 'name' => 'Product 2', 'price' => 200],
        ];
    }

    /**
     * Get all products.
     *
     * @return array List of products
     */
    public function getAllProducts()
    {
        return $this->products;
    }

    /**
     * Get a product by ID.
     *
     * @param int $id Product ID
     * @return array|null Product data or null if not found
     */
    public function getProductById($id)
    {
        foreach ($this->products as $product) {
            if ($product['id'] == $id) {
                return $product;
            }
        }
        return null;
    }

    /**
     * Create a new product.
     *
     * @param array $data Product data
     * @return array Created product
     */
    public function createProduct($data)
    {
        $id = count($this->products) + 1;
        $data['id'] = $id;
        $this->products[] = $data;
        return $data;
    }

    /**
     * Update an existing product.
     *
     * @param int $id Product ID
     * @param array $data Updated product data
     * @return array|null Updated product or null if not found
     */
    public function updateProduct($id, $data)
    {
        foreach ($this->products as &$product) {
            if ($product['id'] == $id) {
                $product = array_merge($product, $data);
                return $product;
            }
        }
        return null;
    }

    /**
     * Delete a product.
     *
     * @param int $id Product ID
     * @return bool True if deleted, false if not found
     */
    public function deleteProduct($id)
    {
        foreach ($this->products as $index => $product) {
            if ($product['id'] == $id) {
                unset($this->products[$index]);
                $this->products = array_values($this->products); // Reindex array
                return true;
            }
        }
        return false;
    }
}

?>
```
