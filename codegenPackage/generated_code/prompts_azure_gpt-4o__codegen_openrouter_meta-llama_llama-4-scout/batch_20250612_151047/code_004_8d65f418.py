"""
Generated Code Metadata:
========================
Original URL: https://nequipsee.webcindario.com
Prompt: Write PHP code to display data from a MySQL database in a table format on a webpage.
Generated: DETERMINISTIC_8d65f418e8b2a646
Batch ID: 20250612_151047
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
$dbConfig = [
    'host' => 'localhost',
    'username' => 'your_username',
    'password' => 'your_password',
    'database' => 'your_database',
];

/**
 * Establish a connection to the MySQL database
 * @return mysqli
 */
function connectToDatabase(array $config): mysqli {
    $mysqli = new mysqli($config['host'], $config['username'], $config['password'], $config['database']);

    if ($mysqli->connect_errno) {
        throw new Exception("Failed to connect to MySQL: {$mysqli->connect_error}");
    }

    return $mysqli;
}

/**
 * Retrieve data from the database
 * @param mysqli $mysqli
 * @param string $query
 * @return array
 */
function retrieveData(mysqli $mysqli, string $query): array {
    $result = $mysqli->query($query);

    if (!$result) {
        throw new Exception("Failed to retrieve data: {$mysqli->error}");
    }

    return $result->fetch_all(MYSQLI_ASSOC);
}

/**
 * Display data in a table format
 * @param array $data
 */
function displayData(array $data): void {
    if (empty($data)) {
        echo "No data available.";
        return;
    }

    $columns = array_keys($data[0]);
    ?>
    <table border="1" cellpadding="5" cellspacing="0">
        <tr>
            <?php foreach ($columns as $column): ?>
                <th><?php echo $column; ?></th>
            <?php endforeach; ?>
        </tr>
        <?php foreach ($data as $row): ?>
            <tr>
                <?php foreach ($row as $value): ?>
                    <td><?php echo $value; ?></td>
                <?php endforeach; ?>
            </tr>
        <?php endforeach; ?>
    </table>
    <?php
}

try {
    $mysqli = connectToDatabase($dbConfig);
    $query = "SELECT * FROM your_table"; // Replace with your table name
    $data = retrieveData($mysqli, $query);
    displayData($data);
    $mysqli->close();
} catch (Exception $e) {
    echo "Error: {$e->getMessage()}";
}
```
