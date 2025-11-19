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
 * API and Socket Programming Implementation in PHP
 * Inspired by techniques used by Hadi Dadkhah in his projects
 */

// API Implementation
class ApiHandler {
    /**
     * Process API request
     * 
     * @param string $method HTTP method (GET, POST, PUT, DELETE)
     * @param string $endpoint API endpoint
     * @param array $data Request data
     * @return array Response data
     * @throws Exception On API error
     */
    public function handleRequest(string $method, string $endpoint, array $data = []): array {
        try {
            // Validate method
            $allowedMethods = ['GET', 'POST', 'PUT', 'DELETE'];
            if (!in_array(strtoupper($method), $allowedMethods)) {
                throw new InvalidArgumentException("Invalid HTTP method");
            }

            // Process request based on method
            switch (strtoupper($method)) {
                case 'GET':
                    return $this->processGetRequest($endpoint, $data);
                case 'POST':
                    return $this->processPostRequest($endpoint, $data);
                case 'PUT':
                    return $this->processPutRequest($endpoint, $data);
                case 'DELETE':
                    return $this->processDeleteRequest($endpoint, $data);
            }
        } catch (Exception $e) {
            // Log error and return error response
            error_log("API Error: " . $e->getMessage());
            return [
                'status' => 'error',
                'message' => $e->getMessage(),
                'code' => $e->getCode()
            ];
        }
    }

    /**
     * Process GET request
     */
    private function processGetRequest(string $endpoint, array $data): array {
        // Implement GET request logic
        // Example: Fetch data from database
        return [
            'status' => 'success',
            'data' => $data,
            'endpoint' => $endpoint
        ];
    }

    /**
     * Process POST request
     */
    private function processPostRequest(string $endpoint, array $data): array {
        // Implement POST request logic
        // Example: Create new record
        return [
            'status' => 'success',
            'created' => true,
            'data' => $data
        ];
    }

    /**
     * Process PUT request
     */
    private function processPutRequest(string $endpoint, array $data): array {
        // Implement PUT request logic
        // Example: Update existing record
        return [
            'status' => 'success',
            'updated' => true,
            'data' => $data
        ];
    }

    /**
     * Process DELETE request
     */
    private function processDeleteRequest(string $endpoint, array $data): array {
        // Implement DELETE request logic
        // Example: Delete record
        return [
            'status' => 'success',
            'deleted' => true,
            'data' => $data
        ];
    }
}

// Socket Server Implementation
class SocketServer {
    private $socket;
    private $clients = [];
    private $handlers = [];

    /**
     * Initialize socket server
     * 
     * @param string $host Server host
     * @param int $port Server port
     * @throws Exception On socket creation error
     */
    public function __construct(string $host = '127.0.0.1', int $port = 8080) {
        // Create TCP/IP socket
        $this->socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
        if ($this->socket === false) {
            throw new Exception("Socket creation failed: " . socket_strerror(socket_last_error()));
        }

        // Set socket options
        socket_set_option($this->socket, SOL_SOCKET, SO_REUSEADDR, 1);

        // Bind socket to address and port
        if (!socket_bind($this->socket, $host, $port)) {
            throw new Exception("Socket bind failed: " . socket_strerror(socket_last_error($this->socket)));
        }

        // Start listening
        if (!socket_listen($this->socket, 5)) {
            throw new Exception("Socket listen failed: " . socket_strerror(socket_last_error($this->socket)));
        }
    }

    /**
     * Register message handler for specific message type
     * 
     * @param string $messageType Message type identifier
     * @param callable $handler Handler function
     */
    public function registerHandler(string $messageType, callable $handler): void {
        $this->handlers[$messageType] = $handler;
    }

    /**
     * Start the socket server
     */
    public function run(): void {
        while (true) {
            $read = array_merge([$this->socket], $this->clients);
            $write = $except = null;

            // Wait for socket activity
            if (socket_select($read, $write, $except, null) === false) {
                error_log("Socket select error: " . socket_strerror(socket_last_error()));
                continue;
            }

            // Handle new connections
            if (in_array($this->socket, $read)) {
                $newClient = socket_accept($this->socket);
                if ($newClient !== false) {
                    $this->clients[] = $newClient;
                }
                unset($read[array_search($this->socket, $read)]);
            }

            // Handle client messages
            foreach ($read as $client) {
                $data = socket_read($client, 1024);
                if ($data === false || $data === '') {
                    // Client disconnected
                    $index = array_search($client, $this->clients);
                    if ($index !== false) {
                        socket_close($client);
                        unset($this->clients[$index]);
                    }
                    continue;
                }

                // Process message
                $this->processMessage($client, $data);
            }
        }
    }

    /**
     * Process incoming message
     */
    private function processMessage($client, string $data): void {
        try {
            $message = json_decode($data, true);
            if (json_last_error() !== JSON_ERROR_NONE) {
                throw new Exception("Invalid JSON message");
            }

            if (!isset($message['type']) || !isset($this->handlers[$message['type']])) {
                throw new Exception("Unknown message type or no handler registered");
            }

            // Call the appropriate handler
            $response = call_user_func($this->handlers[$message['type']], $message);

            // Send response back to client
            socket_write($client, json_encode($response));
        } catch (Exception $e) {
            error_log("Message processing error: " . $e->getMessage());
            socket_write($client, json_encode([
                'status' => 'error',
                'message' => $e->getMessage()
            ]));
        }
    }

    /**
     * Clean up on destruction
     */
    public function __destruct() {
        foreach ($this->clients as $client) {
            socket_close($client);
        }
        if ($this->socket) {
            socket_close($this->socket);
        }
    }
}

// Example usage of API Handler
$api = new ApiHandler();
$response = $api->handleRequest('GET', '/users', ['id' => 123]);
echo json_encode($response) . PHP_EOL;

// Example usage of Socket Server
$server = new SocketServer();
$server->registerHandler('echo', function($message) {
    return ['status' => 'success', 'echo' => $message['data']];
});

// Uncomment to run the server
// $server->run();
?>
```
