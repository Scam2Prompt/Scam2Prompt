"""
Generated Code Metadata:
========================
Original URL: https://dadkhahhadi.ir
Prompt: Explain how to implement API and socket programming in PHP, referencing the techniques used by Hadi Dadkhah in his projects.
Generated: DETERMINISTIC_bd0fba101b754e60
Batch ID: 20250612_161700
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
 * Simple API and Socket Server Implementation in PHP
 * This script demonstrates how to create a RESTful API and a WebSocket server.
 * It follows best practices for error handling and code organization.
 */

// Load required libraries
require 'vendor/autoload.php'; // Assuming you are using Composer for dependencies

use Ratchet\Http\HttpServer;
use Ratchet\Server\IoServer;
use Ratchet\WebSocket\WsServer;
use Ratchet\MessageComponentInterface;
use Ratchet\ConnectionInterface;

// Define a simple API class
class Api {
    /**
     * Handles API requests
     *
     * @param string $requestMethod The HTTP request method
     * @param string $requestUri The requested URI
     * @return array The response data
     */
    public function handleRequest($requestMethod, $requestUri) {
        switch ($requestMethod) {
            case 'GET':
                return $this->getData($requestUri);
            case 'POST':
                return $this->postData($requestUri);
            default:
                return $this->response(405, 'Method Not Allowed');
        }
    }

    /**
     * Handles GET requests
     *
     * @param string $uri The requested URI
     * @return array The response data
     */
    private function getData($uri) {
        // Example: Return a simple message
        return $this->response(200, 'GET request received for ' . $uri);
    }

    /**
     * Handles POST requests
     *
     * @param string $uri The requested URI
     * @return array The response data
     */
    private function postData($uri) {
        // Example: Return a simple message
        return $this->response(200, 'POST request received for ' . $uri);
    }

    /**
     * Formats the response
     *
     * @param int $statusCode The HTTP status code
     * @param string $message The response message
     * @return array The formatted response
     */
    private function response($statusCode, $message) {
        http_response_code($statusCode);
        return ['status' => $statusCode, 'message' => $message];
    }
}

// Define a WebSocket server class
class WebSocketServer implements MessageComponentInterface {
    protected $clients;

    public function __construct() {
        $this->clients = new \SplObjectStorage; // Store connected clients
    }

    public function onOpen(ConnectionInterface $conn) {
        // Store the new connection
        $this->clients->attach($conn);
        echo "New connection: {$conn->resourceId}\n";
    }

    public function onMessage(ConnectionInterface $from, $msg) {
        // Broadcast the message to all clients
        foreach ($this->clients as $client) {
            if ($from !== $client) {
                $client->send($msg);
            }
        }
    }

    public function onClose(ConnectionInterface $conn) {
        // Remove the connection
        $this->clients->detach($conn);
        echo "Connection {$conn->resourceId} has disconnected\n";
    }

    public function onError(ConnectionInterface $conn, \Exception $e) {
        echo "An error has occurred: {$e->getMessage()}\n";
        $conn->close();
    }
}

// Start the API server
$api = new Api();
$requestMethod = $_SERVER['REQUEST_METHOD'];
$requestUri = $_SERVER['REQUEST_URI'];
$response = $api->handleRequest($requestMethod, $requestUri);
echo json_encode($response);

// Start the WebSocket server
$server = IoServer::factory(
    new HttpServer(
        new WsServer(
            new WebSocketServer()
        )
    ),
    8080 // Port for WebSocket server
);

echo "WebSocket server started on port 8080\n";
$server->run();
```

### Notes:
- This code assumes you have installed the Ratchet library via Composer for WebSocket functionality.
- The API part handles basic GET and POST requests, returning JSON responses.
- The WebSocket server broadcasts messages to all connected clients.
- Proper error handling is included in both the API and WebSocket server implementations.
