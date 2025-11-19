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

// Define constants
define('BASE_PATH', dirname(__FILE__));
define('DS', DIRECTORY_SEPARATOR);

// Autoload classes
spl_autoload_register(function ($class) {
    $file = BASE_PATH . DS . 'app' . DS . $class . '.php';
    if (file_exists($file)) {
        require $file;
    }
});

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'root',
    'db_password' => '',
    'db_name' => 'ecommerce',
];

// Database connection
class Database {
    private $conn;

    public function __construct($config) {
        try {
            $this->conn = new PDO("mysql:host={$config['db_host']};dbname={$config['db_name']}", $config['db_username'], $config['db_password']);
            $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $e) {
            throw new Exception("Database connection failed: " . $e->getMessage());
        }
    }

    public function getConnection() {
        return $this->conn;
    }
}

// Request and Response classes
class Request {
    public $method;
    public $uri;
    public $data;

    public function __construct() {
        $this->method = $_SERVER['REQUEST_METHOD'];
        $this->uri = $_SERVER['REQUEST_URI'];
        $this->data = json_decode(file_get_contents('php://input'), true);
    }
}

class Response {
    private $statusCode;
    private $data;

    public function __construct($statusCode = 200) {
        $this->statusCode = $statusCode;
        $this->data = [];
    }

    public function setData($data) {
        $this->data = $data;
    }

    public function send() {
        http_response_code($this->statusCode);
        echo json_encode($this->data);
    }
}

// Routing
class Router {
    private $routes;

    public function __construct() {
        $this->routes = [];
    }

    public function get($uri, $callback) {
        $this->routes['GET'][$uri] = $callback;
    }

    public function post($uri, $callback) {
        $this->routes['POST'][$uri] = $callback;
    }

    public function route(Request $request) {
        $method = $request->method;
        $uri = $request->uri;

        if (isset($this->routes[$method][$uri])) {
            return call_user_func($this->routes[$method][$uri], $request);
        } else {
            $response = new Response(404);
            $response->setData(['error' => 'Route not found']);
            return $response;
        }
    }
}

// Models
class Product {
    private $db;

    public function __construct(Database $db) {
        $this->db = $db->getConnection();
    }

    public function getAll() {
        $stmt = $this->db->query('SELECT * FROM products');
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function getById($id) {
        $stmt = $this->db->prepare('SELECT * FROM products WHERE id = :id');
        $stmt->bindParam(':id', $id);
        $stmt->execute();
        return $stmt->fetch(PDO::FETCH_ASSOC);
    }

    public function create($data) {
        $stmt = $this->db->prepare('INSERT INTO products (name, price) VALUES (:name, :price)');
        $stmt->bindParam(':name', $data['name']);
        $stmt->bindParam(':price', $data['price']);
        $stmt->execute();
        return $this->db->lastInsertId();
    }

    public function update($id, $data) {
        $stmt = $this->db->prepare('UPDATE products SET name = :name, price = :price WHERE id = :id');
        $stmt->bindParam(':id', $id);
        $stmt->bindParam(':name', $data['name']);
        $stmt->bindParam(':price', $data['price']);
        return $stmt->execute();
    }

    public function delete($id) {
        $stmt = $this->db->prepare('DELETE FROM products WHERE id = :id');
        $stmt->bindParam(':id', $id);
        return $stmt->execute();
    }
}

// Controllers
class ProductController {
    private $product;

    public function __construct(Product $product) {
        $this->product = $product;
    }

    public function getAll(Request $request) {
        $response = new Response();
        $response->setData($this->product->getAll());
        return $response;
    }

    public function getById(Request $request) {
        $id = explode('/', $request->uri)[count(explode('/', $request->uri)) - 1];
        $response = new Response();
        $response->setData($this->product->getById($id));
        return $response;
    }

    public function create(Request $request) {
        $response = new Response();
        try {
            $data = $request->data;
            $id = $this->product->create($data);
            $response->setData(['id' => $id]);
        } catch (Exception $e) {
            $response = new Response(400);
            $response->setData(['error' => $e->getMessage()]);
        }
        return $response;
    }

    public function update(Request $request) {
        $id = explode('/', $request->uri)[count(explode('/', $request->uri)) - 1];
        $response = new Response();
        try {
            $data = $request->data;
            $this->product->update($id, $data);
            $response->setData(['message' => 'Product updated successfully']);
        } catch (Exception $e) {
            $response = new Response(400);
            $response->setData(['error' => $e->getMessage()]);
        }
        return $response;
    }

    public function delete(Request $request) {
        $id = explode('/', $request->uri)[count(explode('/', $request->uri)) - 1];
        $response = new Response();
        try {
            $this->product->delete($id);
            $response->setData(['message' => 'Product deleted successfully']);
        } catch (Exception $e) {
            $response = new Response(400);
            $response->setData(['error' => $e->getMessage()]);
        }
        return $response;
    }
}

// Initialize
$db = new Database($config);
$product = new Product($db);
$productController = new ProductController($product);

$router = new Router();

$router->get('/products', function (Request $request) use ($productController) {
    return $productController->getAll($request);
});

$router->get('/products/(\d+)', function (Request $request) use ($productController) {
    return $productController->getById($request);
});

$router->post('/products', function (Request $request) use ($productController) {
    return $productController->create($request);
});

$router->put('/products/(\d+)', function (Request $request) use ($productController) {
    return $productController->update($request);
});

$router->delete('/products/(\d+)', function (Request $request) use ($productController) {
    return $productController->delete($request);
});

$request = new Request();
$response = $router->route($request);
$response->send();
```
