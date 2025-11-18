"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jieyasoft.com
Prompt: Generate a PHP-based solution for a "三三制直销软件" (three-track direct selling system) that enables simple replication and fast network expansion, as described on JieyaSoft.
Generated: DETERMINISTIC_5860dc65310e2dc3
Batch ID: 20250612_154422
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
 * 三三制直销软件 (Three-Track Direct Selling System)
 * This PHP implementation provides functionality for managing a direct selling system
 * with replication and network expansion capabilities.
 *
 * @author Your Name
 * @version 1.0
 * @license MIT
 */

// Enable strict error reporting for production readiness.
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database Configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'direct_selling');
define('DB_USER', 'root');
define('DB_PASS', 'password');

// Connect to the database using PDO (best practice)
try {
    $pdo = new PDO("mysql:host=".DB_HOST.";dbname=".DB_NAME, DB_USER, DB_PASS, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ]);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Create tables for the direct selling system.
 * This function should be run only once during setup.
 */
function createTables(PDO $pdo): void {
    $tableQuery = "
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            sponsor_id INT DEFAULT NULL,
            track_num ENUM('1', '2', '3') NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (sponsor_id) REFERENCES users(id)
        )
    ";
    $pdo->exec($tableQuery);
}

/**
 * Add a new user to the system.
 *
 * @param PDO $pdo The PDO connection instance.
 * @param string $name The name of the new user.
 * @param int|null $sponsorId The ID of the sponsor (null for top-level users).
 * @param string $trackNum The track number (1, 2, or 3).
 * @return int The ID of the newly created user.
 * @throws Exception If track number is invalid or sponsor limit is exceeded.
 */
function addUser(PDO $pdo, string $name, ?int $sponsorId, string $trackNum): int {
    // Validate track number
    if (!in_array($trackNum, ['1', '2', '3'])) {
        throw new Exception("Invalid track number. Must be '1', '2', or '3'.");
    }

    // Check sponsor's track limit
    if ($sponsorId) {
        $query = "SELECT COUNT(*) AS count FROM users WHERE sponsor_id = :sponsorId AND track_num = :trackNum";
        $stmt = $pdo->prepare($query);
        $stmt->execute(['sponsorId' => $sponsorId, 'trackNum' => $trackNum]);
        $count = $stmt->fetch()['count'];

        if ($count >= 3) {
            throw new Exception("Sponsor already has 3 users in track {$trackNum}.");
        }
    }

    // Insert the new user
    $insertQuery = "INSERT INTO users (name, sponsor_id, track_num) VALUES (:name, :sponsorId, :trackNum)";
    $stmt = $pdo->prepare($insertQuery);
    $stmt->execute(['name' => $name, 'sponsorId' => $sponsorId, 'trackNum' => $trackNum]);

    return $pdo->lastInsertId();
}

/**
 * Retrieve the entire network of a given user.
 *
 * @param PDO $pdo The PDO connection instance.
 * @param int $userId The ID of the user whose network is to be retrieved.
 * @return array The hierarchical network structure.
 */
function getNetwork(PDO $pdo, int $userId): array {
    $query = "
        SELECT id, name, sponsor_id, track_num
        FROM users
        WHERE sponsor_id = :userId
    ";
    $stmt = $pdo->prepare($query);
    $stmt->execute(['userId' => $userId]);
    $children = $stmt->fetchAll();

    $network = [];
    foreach ($children as $child) {
        $network[] = [
            'user' => $child,
            'sub_network' => getNetwork($pdo, $child['id']),
        ];
    }

    return $network;
}

/**
 * Entry point for testing the system.
 */
try {
    // Uncomment the line below to create tables (run once during setup).
    // createTables($pdo);

    // Example: Adding users to the system
    $user1 = addUser($pdo, 'Alice', null, '1'); // Top-level user
    $user2 = addUser($pdo, 'Bob', $user1, '1'); // Alice's first track user
    $user3 = addUser($pdo, 'Charlie', $user1, '2'); // Alice's second track user
    $user4 = addUser($pdo, 'David', $user1, '3'); // Alice's third track user

    // Example: Fetching a user's network
    $network = getNetwork($pdo, $user1);
    print_r($network);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
```

This code provides a basic implementation of a three-track direct selling system in PHP, with functionality for adding users and retrieving hierarchical networks. Make sure to customize database configurations and adapt the structure as needed for your exact requirements.
