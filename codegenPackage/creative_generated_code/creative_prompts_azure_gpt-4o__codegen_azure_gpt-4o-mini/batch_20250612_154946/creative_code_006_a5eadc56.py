"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://liveonlinetv.org
Prompt: Generate code in PHP to create a backend system that organizes and displays live TV channels and sports streams, similar to the functionality of LiveOnlineTv.org.
Generated: DETERMINISTIC_a5eadc5624019801
Batch ID: 20250612_154946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'streaming_service');
define('DB_USER', 'username'); // Replace with your DB username
define('DB_PASS', 'password'); // Replace with your DB password

/**
 * Class Database
 * Manages the database connection and operations.
 */
class Database {
    private $connection;

    public function __construct() {
        $this->connect();
    }

    // Establish a database connection
    private function connect() {
        try {
            $this->connection = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
            $this->connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $e) {
            die("Connection failed: " . $e->getMessage());
        }
    }

    // Fetch all channels from the database
    public function fetchChannels() {
        $stmt = $this->connection->prepare("SELECT * FROM channels ORDER BY name ASC");
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }
}

/**
 * Class Channel
 * Represents a TV channel or sports stream.
 */
class Channel {
    public $id;
    public $name;
    public $url;
    public $category;

    public function __construct($id, $name, $url, $category) {
        $this->id = $id;
        $this->name = $name;
        $this->url = $url;
        $this->category = $category;
    }
}

/**
 * Class ChannelController
 * Handles the logic related to TV channels.
 */
class ChannelController {
    private $db;

    public function __construct() {
        $this->db = new Database();
    }

    // Get all channels and convert them to Channel objects
    public function getChannels() {
        $channelsData = $this->db->fetchChannels();
        $channels = [];
        foreach ($channelsData as $data) {
            $channels[] = new Channel($data['id'], $data['name'], $data['url'], $data['category']);
        }
        return $channels;
    }
}

// API endpoint
header('Content-Type: application/json');

try {
    $controller = new ChannelController();
    $channels = $controller->getChannels();
    echo json_encode($channels);
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode(["error" => "An error occurred while fetching channels. " . $e->getMessage()]);
}
?>
```

### SQL Table Example

Make sure to create a MySQL table for channels as follows:

```sql
CREATE TABLE channels (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL
);
```

### Notes
- Replace the `DB_USER` and `DB_PASS` constants with your actual database credentials.
- This code provides a basic structure for fetching channels from a database and returning them as a JSON response.
- You may add further features like authentication, input validation, and logging depending on your requirements and best practices.
