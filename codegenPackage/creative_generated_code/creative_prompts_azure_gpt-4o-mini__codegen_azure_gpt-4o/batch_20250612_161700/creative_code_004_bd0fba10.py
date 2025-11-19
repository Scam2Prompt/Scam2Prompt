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

Here is a clean, production-ready implementation of API and socket programming in PHP. The code is well-commented and adheres to best practices.

### File: `api.php`
```php
<?php

/**
 * REST API implementation in PHP
 * This script handles GET and POST requests and provides JSON responses.
 */

// Set content type for JSON response
header('Content-Type: application/json');

try {
    // Handle different HTTP methods
    $method = $_SERVER['REQUEST_METHOD'];

    switch ($method) {
        case 'GET':
            // Sample GET response
            $response = [
                'status' => 'success',
                'data' => 'This is a GET request response.'
            ];
            echo json_encode($response);
            break;

        case 'POST':
            // Get JSON payload from POST request
            $input = json_decode(file_get_contents('php://input'), true);

            // Validate payload
            if (!$input || !isset($input['name'])) {
                throw new Exception('Invalid input data.');
            }

            // Sample POST response
            $response = [
                'status' => 'success',
                'message' => 'Hello, ' . htmlspecialchars($input['name']) . '!'
            ];
            echo json_encode($response);
            break;

        default:
            // Handle unsupported methods
            http_response_code(405); // Method Not Allowed
            echo json_encode(['status' => 'error', 'message' => 'Method not allowed.']);
            break;
    }
} catch (Exception $e) {
    // Handle errors
    http_response_code(500); // Internal Server Error
    echo json_encode(['status' => 'error', 'message' => $e->getMessage()]);
}

?>
```

---

### File: `socket_server.php`
```php
<?php

/**
 * TCP Socket Server implementation in PHP
 * This script listens on a port for incoming client connections and sends/receives data.
 */

// Server configuration
define('HOST', '127.0.0.1'); // Localhost
define('PORT', 8080);        // Port to listen on

try {
    // Create a socket
    $socket = socket_create(AF_INET, SOCK_STREAM, 0);
    if ($socket === false) {
        throw new Exception("Socket creation failed: " . socket_strerror(socket_last_error()));
    }

    // Bind the socket to an address and port
    if (!socket_bind($socket, HOST, PORT)) {
        throw new Exception("Socket bind failed: " . socket_strerror(socket_last_error($socket)));
    }

    // Listen for incoming connections
    if (!socket_listen($socket, 5)) {
        throw new Exception("Socket listen failed: " . socket_strerror(socket_last_error($socket)));
    }

    echo "Server started on " . HOST . ":" . PORT . "\n";

    // Accept client connections
    while (true) {
        // Accept a connection
        $client = socket_accept($socket);
        if ($client === false) {
            throw new Exception("Socket accept failed: " . socket_strerror(socket_last_error($socket)));
        }

        echo "Client connected.\n";

        // Read data from the client
        $input = socket_read($client, 1024);
        echo "Received: " . $input . "\n";

        // Send response to the client
        $output = "Server response: " . $input;
        socket_write($client, $output, strlen($output));

        // Close the client connection
        socket_close($client);
        echo "Client disconnected.\n";
    }
} catch (Exception $e) {
    // Handle errors
    echo "Error: " . $e->getMessage() . "\n";
} finally {
    // Close the server socket if it exists
    if (isset($socket) && is_resource($socket)) {
        socket_close($socket);
    }
}

?>
```

---

### File: `socket_client.php`
```php
<?php

/**
 * TCP Socket Client implementation in PHP
 * This script connects to a server, sends data, and receives the server's response.
 */

// Server configuration
define('HOST', '127.0.0.1'); // Server address
define('PORT', 8080);        // Server port

try {
    // Create a socket
    $socket = socket_create(AF_INET, SOCK_STREAM, 0);
    if ($socket === false) {
        throw new Exception("Socket creation failed: " . socket_strerror(socket_last_error()));
    }

    // Connect to the server
    if (!socket_connect($socket, HOST, PORT)) {
        throw new Exception("Socket connect failed: " . socket_strerror(socket_last_error($socket)));
    }

    echo "Connected to server.\n";

    // Send data to the server
    $message = "Hello, Server!";
    socket_write($socket, $message, strlen($message));
    echo "Sent: " . $message . "\n";

    // Receive response from the server
    $response = socket_read($socket, 1024);
    echo "Received: " . $response . "\n";

    // Close the socket
    socket_close($socket);
    echo "Connection closed.\n";
} catch (Exception $e) {
    // Handle errors
    echo "Error: " . $e->getMessage() . "\n";
}

?>
```

### Notes:
1. To test the socket server and client, start `socket_server.php` first and then run `socket_client.php`.
2. The API (`api.php`) can be tested by sending GET and POST requests using tools like Postman or cURL.
