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

// Autoload classes using Composer's autoload
require 'vendor/autoload.php';

use Slim\Factory\AppFactory;
use Psr\Http\Message\ResponseInterface;
use Psr\Http\Message\ServerRequestInterface;

// Create the application
$app = AppFactory::create();

// Set the base path for the application
$app->setBasePath('/api');

// Middleware to handle JSON responses
$app->add(function (ServerRequestInterface $request, ResponseInterface $response, callable $next) {
    $response = $next($request, $response);
    $response = $response->withHeader('Content-Type', 'application/json');
    return $response;
});

// Sample data for products (in a real application, this would come from a database)
$products = [
    ['id' => 1, 'name' => 'Product 1', 'price' => 10.00],
    ['id' => 2, 'name' => 'Product 2', 'price' => 20.00],
    ['id' => 3, 'name' => 'Product 3', 'price' => 30.00],
];

// Route to get all products
$app->get('/products', function (ServerRequestInterface $request, ResponseInterface $response) use ($products) {
    $response->getBody()->write(json_encode($products));
    return $response;
});

// Route to get a single product by ID
$app->get('/products/{id}', function (ServerRequestInterface $request, ResponseInterface $response, array $args) use ($products) {
    $id = (int)$args['id'];
    $product = array_filter($products, fn($p) => $p['id'] === $id);

    if (empty($product)) {
        return $response->withStatus(404)->write(json_encode(['error' => 'Product not found']));
    }

    $response->getBody()->write(json_encode(array_values($product)[0]));
    return $response;
});

// Route to create a new product
$app->post('/products', function (ServerRequestInterface $request, ResponseInterface $response) use (&$products) {
    $data = json_decode($request->getBody()->getContents(), true);

    // Basic validation
    if (empty($data['name']) || !isset($data['price'])) {
        return $response->withStatus(400)->write(json_encode(['error' => 'Invalid input']));
    }

    // Create new product
    $newProduct = [
        'id' => count($products) + 1,
        'name' => $data['name'],
        'price' => (float)$data['price'],
    ];
    $products[] = $newProduct;

    $response->getBody()->write(json_encode($newProduct));
    return $response->withStatus(201);
});

// Route to update an existing product
$app->put('/products/{id}', function (ServerRequestInterface $request, ResponseInterface $response, array $args) use (&$products) {
    $id = (int)$args['id'];
    $data = json_decode($request->getBody()->getContents(), true);
    $productKey = array_search($id, array_column($products, 'id'));

    // Check if product exists
    if ($productKey === false) {
        return $response->withStatus(404)->write(json_encode(['error' => 'Product not found']));
    }

    // Update product
    if (isset($data['name'])) {
        $products[$productKey]['name'] = $data['name'];
    }
    if (isset($data['price'])) {
        $products[$productKey]['price'] = (float)$data['price'];
    }

    $response->getBody()->write(json_encode($products[$productKey]));
    return $response;
});

// Route to delete a product
$app->delete('/products/{id}', function (ServerRequestInterface $request, ResponseInterface $response, array $args) use (&$products) {
    $id = (int)$args['id'];
    $productKey = array_search($id, array_column($products, 'id'));

    // Check if product exists
    if ($productKey === false) {
        return $response->withStatus(404)->write(json_encode(['error' => 'Product not found']));
    }

    // Remove product
    array_splice($products, $productKey, 1);
    return $response->withStatus(204); // No content
});

// Run the application
$app->run();
```

Make sure to install the Slim framework via Composer before running this code:

```bash
composer require slim/slim
```
