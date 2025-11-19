"""
Generated Code Metadata:
========================
Original URL: https://dadkhahhadi.ir
Prompt: Develop a PHP backend for a virtual number panel media application.
Generated: DETERMINISTIC_250104127d2102c8
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
// Virtual Number Panel Media Application Backend

// Autoload dependencies using Composer
require 'vendor/autoload.php';

use Slim\Factory\AppFactory;
use Psr\Http\Message\ResponseInterface;
use Psr\Http\Message\ServerRequestInterface;
use Psr\Http\Server\RequestHandlerInterface;
use Psr\Http\Server\RequestHandlerInterface;

// Create the application
$app = AppFactory::create();

// Set the base path for the application
$app->setBasePath('/api');

// Middleware to handle JSON responses
$app->add(function (ServerRequestInterface $request, RequestHandlerInterface $handler): ResponseInterface {
    $response = $handler->handle($request);
    return $response->withHeader('Content-Type', 'application/json');
});

// Database connection using PDO
function getDatabaseConnection() {
    $host = 'localhost';
    $db = 'virtual_number_panel';
    $user = 'root';
    $pass = '';
    $charset = 'utf8mb4';

    $dsn = "mysql:host=$host;dbname=$db;charset=$charset";
    $options = [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false,
    ];

    try {
        return new PDO($dsn, $user, $pass, $options);
    } catch (PDOException $e) {
        // Handle connection error
        error_log($e->getMessage());
        throw new Exception('Database connection error.');
    }
}

// Route to get all virtual numbers
$app->get('/numbers', function (ServerRequestInterface $request, ResponseInterface $response) {
    try {
        $db = getDatabaseConnection();
        $stmt = $db->query('SELECT * FROM virtual_numbers');
        $numbers = $stmt->fetchAll();

        $response->getBody()->write(json_encode($numbers));
        return $response->withStatus(200);
    } catch (Exception $e) {
        $response->getBody()->write(json_encode(['error' => $e->getMessage()]));
        return $response->withStatus(500);
    }
});

// Route to add a new virtual number
$app->post('/numbers', function (ServerRequestInterface $request, ResponseInterface $response) {
    $data = json_decode($request->getBody()->getContents(), true);

    // Validate input
    if (empty($data['number'])) {
        $response->getBody()->write(json_encode(['error' => 'Number is required.']));
        return $response->withStatus(400);
    }

    try {
        $db = getDatabaseConnection();
        $stmt = $db->prepare('INSERT INTO virtual_numbers (number) VALUES (:number)');
        $stmt->execute(['number' => $data['number']]);

        $response->getBody()->write(json_encode(['message' => 'Number added successfully.']));
        return $response->withStatus(201);
    } catch (Exception $e) {
        $response->getBody()->write(json_encode(['error' => $e->getMessage()]));
        return $response->withStatus(500);
    }
});

// Route to delete a virtual number
$app->delete('/numbers/{id}', function (ServerRequestInterface $request, ResponseInterface $response, array $args) {
    $id = $args['id'];

    try {
        $db = getDatabaseConnection();
        $stmt = $db->prepare('DELETE FROM virtual_numbers WHERE id = :id');
        $stmt->execute(['id' => $id]);

        if ($stmt->rowCount() === 0) {
            $response->getBody()->write(json_encode(['error' => 'Number not found.']));
            return $response->withStatus(404);
        }

        $response->getBody()->write(json_encode(['message' => 'Number deleted successfully.']));
        return $response->withStatus(200);
    } catch (Exception $e) {
        $response->getBody()->write(json_encode(['error' => $e->getMessage()]));
        return $response->withStatus(500);
    }
});

// Run the application
$app->run();
```

Make sure to create a database named `virtual_number_panel` and a table named `virtual_numbers` with at least an `id` (auto-increment) and `number` (varchar) column for this code to work properly.
