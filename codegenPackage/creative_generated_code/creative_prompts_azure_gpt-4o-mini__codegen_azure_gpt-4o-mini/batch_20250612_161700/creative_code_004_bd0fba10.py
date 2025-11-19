"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dadkhahhadi.ir
Prompt: Explain how to implement API and socket programming in PHP, referencing the techniques used by Hadi Dadkhah in his projects.
Generated: DETERMINISTIC_bd0fba101b754e60
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Simple API implementation using PHP
 * 
 * This API allows basic CRUD operations on a resource called "items".
 * It responds to GET, POST, PUT, and DELETE requests.
 */

// Set the content type to application/json
header("Content-Type: application/json");

// Database connection parameters
$host = 'localhost';
$db = 'test_db';
$user = 'root';
$pass = '';

// Create a new PDO instance for database operations
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    // Set PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle database connection errors
    echo json_encode(['error' => 'Database connection failed: ' . $e->getMessage()]);
    exit();
}

// Define a function to handle API requests
function handleRequest($pdo) {
    $method = $_SERVER['REQUEST_METHOD'];
    $input = json_decode(file_get_contents('php://input'), true);
    $response = [];

    switch ($method) {
        case 'GET':
            $response = getItems($pdo);
            break;
        case 'POST':
            $response = createItem($pdo, $input);
            break;
        case 'PUT':
            $response = updateItem($pdo, $input);
            break;
        case 'DELETE':
            $response = deleteItem($pdo, $input);
            break;
        default:
            http_response_code(405);
            $response = ['error' => 'Method Not Allowed'];
            break;
    }

    echo json_encode($response);
}

// Get all items from the database
function getItems($pdo) {
    $stmt = $pdo->query("SELECT * FROM items");
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Create a new item in the database
function createItem($pdo, $input) {
    if (!isset($input['name'])) {
        http_response_code(400);
        return ['error' => 'Missing required field: name'];
    }

    $stmt = $pdo->prepare("INSERT INTO items (name) VALUES (:name)");
    $stmt->bindParam(':name', $input['name']);

    if ($stmt->execute()) {
        return ['success' => 'Item created', 'id' => $pdo->lastInsertId()];
    } else {
        http_response_code(500);
        return ['error' => 'Failed to create item'];
    }
}

// Update an existing item in the database
function updateItem($pdo, $input) {
    if (!isset($input['id']) || !isset($input['name'])) {
        http_response_code(400);
        return ['error' => 'Missing required fields: id, name'];
    }

    $stmt = $pdo->prepare("UPDATE items SET name = :name WHERE id = :id");
    $stmt->bindParam(':name', $input['name']);
    $stmt->bindParam(':id', $input['id']);

    if ($stmt->execute()) {
        return ['success' => 'Item updated'];
    } else {
        http_response_code(500);
        return ['error' => 'Failed to update item'];
    }
}

// Delete an item from the database
function deleteItem($pdo, $input) {
    if (!isset($input['id'])) {
        http_response_code(400);
        return ['error' => 'Missing required field: id'];
    }

    $stmt = $pdo->prepare("DELETE FROM items WHERE id = :id");
    $stmt->bindParam(':id', $input['id']);

    if ($stmt->execute()) {
        return ['success' => 'Item deleted'];
    } else {
        http_response_code(500);
        return ['error' => 'Failed to delete item'];
    }
}

// Handle the incoming API request
handleRequest($pdo);
```

```php
<?php
/**
 * Simple Socket Server Implementation in PHP
 * 
 * This server listens for incoming connections and echoes back any messages it receives.
 */

// Set the address and port
$address = '127.0.0.1';
$port = 8080;

// Create a TCP/IP socket
$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
if (!$socket) {
    die('Could not create socket: ' . socket_strerror(socket_last_error()));
}

// Bind the socket to the address and port
if (!socket_bind($socket, $address, $port)) {
    die('Could not bind socket: ' . socket_strerror(socket_last_error($socket)));
}

// Start listening for connections
if (!socket_listen($socket, 5)) {
    die('Could not listen on socket: ' . socket_strerror(socket_last_error($socket)));
}

// Main loop to accept and handle connections
do {
    // Accept a connection
    $client = socket_accept($socket);
    if ($client === false) {
        echo 'Could not accept connection: ' . socket_strerror(socket_last_error($socket));
        break;
    }

    // Read the message from the client
    $message = '';
    while ($buf = socket_read($client, 2048, PHP_NORMAL_READ)) {
        $message .= $buf;
    }

    // Echo the message back to the client
    socket_write($client, "Server received: " . $message, strlen("Server received: " . $message));

    // Close the client connection
    socket_close($client);
} while (true);

// Clean up the main socket
socket_close($socket);
?>
```
