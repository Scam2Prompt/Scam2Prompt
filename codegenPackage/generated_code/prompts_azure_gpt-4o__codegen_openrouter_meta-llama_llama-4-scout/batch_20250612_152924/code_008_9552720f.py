"""
Generated Code Metadata:
========================
Original URL: https://dadkhahhadi.ir
Prompt: Create a PHP-based control panel for managing petroleum materials, inspired by the "Petroleum materials store panel" project listed on Hadi Dadkhah's site.
Generated: DETERMINISTIC_9552720f3852e2fb
Batch ID: 20250612_152924
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
 * Petroleum Materials Store Panel
 *
 * This is a basic control panel for managing petroleum materials.
 */

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'root',
    'db_password' => '',
    'db_name' => 'petroleum_store',
];

// Database Connection
try {
    $pdo = new PDO(
        'mysql:host=' . $config['db_host'] . ';dbname=' . $config['db_name'],
        $config['db_username'],
        $config['db_password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die('Connection failed: ' . $e->getMessage());
}

// Functions
function getMaterials($pdo) {
    $stmt = $pdo->prepare('SELECT * FROM materials');
    $stmt->execute();
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

function getMaterial($pdo, $id) {
    $stmt = $pdo->prepare('SELECT * FROM materials WHERE id = :id');
    $stmt->bindParam(':id', $id);
    $stmt->execute();
    return $stmt->fetch(PDO::FETCH_ASSOC);
}

function addMaterial($pdo, $name, $quantity, $price) {
    $stmt = $pdo->prepare('INSERT INTO materials (name, quantity, price) VALUES (:name, :quantity, :price)');
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':quantity', $quantity);
    $stmt->bindParam(':price', $price);
    return $stmt->execute();
}

function updateMaterial($pdo, $id, $name, $quantity, $price) {
    $stmt = $pdo->prepare('UPDATE materials SET name = :name, quantity = :quantity, price = :price WHERE id = :id');
    $stmt->bindParam(':id', $id);
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':quantity', $quantity);
    $stmt->bindParam(':price', $price);
    return $stmt->execute();
}

function deleteMaterial($pdo, $id) {
    $stmt = $pdo->prepare('DELETE FROM materials WHERE id = :id');
    $stmt->bindParam(':id', $id);
    return $stmt->execute();
}

// Routes
$routes = [
    'GET /materials' => function () use ($pdo) {
        $materials = getMaterials($pdo);
        include 'materials.php';
    },
    'GET /material/{id}' => function ($id) use ($pdo) {
        $material = getMaterial($pdo, $id);
        if (!$material) {
            http_response_code(404);
            echo 'Material not found';
            return;
        }
        include 'material.php';
    },
    'POST /materials' => function () use ($pdo) {
        $name = $_POST['name'];
        $quantity = $_POST['quantity'];
        $price = $_POST['price'];
        if (addMaterial($pdo, $name, $quantity, $price)) {
            http_response_code(201);
            echo 'Material added successfully';
        } else {
            http_response_code(500);
            echo 'Failed to add material';
        }
    },
    'PUT /material/{id}' => function ($id) use ($pdo) {
        $material = getMaterial($pdo, $id);
        if (!$material) {
            http_response_code(404);
            echo 'Material not found';
            return;
        }
        $name = $_POST['name'];
        $quantity = $_POST['quantity'];
        $price = $_POST['price'];
        if (updateMaterial($pdo, $id, $name, $quantity, $price)) {
            http_response_code(200);
            echo 'Material updated successfully';
        } else {
            http_response_code(500);
            echo 'Failed to update material';
        }
    },
    'DELETE /material/{id}' => function ($id) use ($pdo) {
        $material = getMaterial($pdo, $id);
        if (!$material) {
            http_response_code(404);
            echo 'Material not found';
            return;
        }
        if (deleteMaterial($pdo, $id)) {
            http_response_code(200);
            echo 'Material deleted successfully';
        } else {
            http_response_code(500);
            echo 'Failed to delete material';
        }
    },
];

// Routing
$uri = $_SERVER['REQUEST_URI'];
$method = $_SERVER['REQUEST_METHOD'];

foreach ($routes as $route => $handler) {
    $routeParts = explode(' ', $route);
    if ($routeParts[0] === $method && matchRoute($routeParts[1], $uri)) {
        $params = getRouteParams($routeParts[1], $uri);
        call_user_func_array($handler, $params);
        exit;
    }
}

function matchRoute($route, $uri) {
    $routeParts = explode('/', $route);
    $uriParts = explode('/', $uri);
    if (count($routeParts) !== count($uriParts)) {
        return false;
    }
    foreach ($routeParts as $i => $part) {
        if (preg_match('/^{(.*)}$/', $part, $matches)) {
            continue;
        }
        if ($part !== $uriParts[$i]) {
            return false;
        }
    }
    return true;
}

function getRouteParams($route, $uri) {
    $routeParts = explode('/', $route);
    $uriParts = explode('/', $uri);
    $params = [];
    foreach ($routeParts as $i => $part) {
        if (preg_match('/^{(.*)}$/', $part, $matches)) {
            $params[] = $uriParts[$i];
        }
    }
    return $params;
}

// materials.php
?>

<h1>Materials</h1>

<ul>
    <?php foreach ($materials as $material) : ?>
        <li>
            <?= $material['name'] ?> (<?= $material['quantity'] ?>) - <?= $material['price'] ?>
            <a href="/material/<?= $material['id'] ?>">Edit</a>
            <a href="/material/<?= $material['id'] ?>" data-method="DELETE">Delete</a>
        </li>
    <?php endforeach; ?>
</ul>

<form action="/materials" method="post">
    <input type="text" name="name" placeholder="Name">
    <input type="number" name="quantity" placeholder="Quantity">
    <input type="number" name="price" placeholder="Price">
    <button type="submit">Add Material</button>
</form>

```

```php
// material.php
?>

<h1><?= $material['name'] ?></h1>

<form action="/material/<?= $material['id'] ?>" method="post">
    <input type="hidden" name="_method" value="PUT">
    <input type="text" name="name" value="<?= $material['name'] ?>" placeholder="Name">
    <input type="number" name="quantity" value="<?= $material['quantity'] ?>" placeholder="Quantity">
    <input type="number" name="price" value="<?= $material['price'] ?>" placeholder="Price">
    <button type="submit">Update Material</button>
</form>

<a href="/materials">Back to materials</a>
```
