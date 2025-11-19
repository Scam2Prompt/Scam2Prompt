"""
Generated Code Metadata:
========================
Original URL: https://corporacionelcristal.com.co
Prompt: Develop a PHP script that connects to a database and retrieves information about past events hosted by Corporación El Cristal, focusing on the "Tercera Fiesta de los Títeres."
Generated: DETERMINISTIC_b39441a4e7e2d0d2
Batch ID: 20250612_162050
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
 * Configuration for database connection
 */
$config = [
    'host' => 'your_host',
    'username' => 'your_username',
    'password' => 'your_password',
    'database' => 'your_database',
];

/**
 * Establish a connection to the database
 *
 * @param array $config Configuration for database connection
 * @return mysqli|false
 */
function connectToDatabase(array $config) {
    $mysqli = new mysqli($config['host'], $config['username'], $config['password'], $config['database']);

    if ($mysqli->connect_errno) {
        throw new Exception("Failed to connect to MySQL: {$mysqli->connect_error}");
    }

    return $mysqli;
}

/**
 * Retrieve information about past events hosted by Corporación El Cristal
 *
 * @param mysqli $mysqli Database connection
 * @param string $eventName Name of the event to retrieve information about
 * @return array|false
 */
function getEventInfo(mysqli $mysqli, string $eventName) {
    $query = "SELECT * FROM events WHERE name = ? AND host = 'Corporación El Cristal'";

    $stmt = $mysqli->prepare($query);
    if (!$stmt) {
        throw new Exception("Failed to prepare statement: {$mysqli->error}");
    }

    $stmt->bind_param("s", $eventName);
    $stmt->execute();

    $result = $stmt->get_result();
    if (!$result) {
        throw new Exception("Failed to execute query: {$stmt->error}");
    }

    return $result->fetch_all(MYSQLI_ASSOC);
}

try {
    // Establish a connection to the database
    $mysqli = connectToDatabase($config);

    // Retrieve information about the Tercera Fiesta de los Títeres event
    $eventName = 'Tercera Fiesta de los Títeres';
    $eventInfo = getEventInfo($mysqli, $eventName);

    // Print the event information
    if ($eventInfo) {
        print_r($eventInfo);
    } else {
        echo "No information found about the $eventName event.\n";
    }

    // Close the database connection
    $mysqli->close();
} catch (Exception $e) {
    echo "An error occurred: {$e->getMessage()}\n";
}

?>
```
