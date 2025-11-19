"""
Generated Code Metadata:
========================
Original URL: https://seriesflix2tv.live
Prompt: Create a code snippet in PHP that interacts with the SeriesFlix database to retrieve all series available under the 'Terror' category.
Generated: DETERMINISTIC_d3170467b759f8ee
Batch ID: 20250612_155531
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
 * Class SeriesFlixDatabase
 * This class handles interactions with the SeriesFlix database.
 */
class SeriesFlixDatabase {
    private $pdo;

    /**
     * Constructor to initialize the PDO connection.
     *
     * @param string $host Database host
     * @param string $db Database name
     * @param string $user Database user
     * @param string $pass Database password
     */
    public function __construct($host, $db, $user, $pass) {
        $dsn = "mysql:host=$host;dbname=$db;charset=utf8mb4";
        try {
            $this->pdo = new PDO($dsn, $user, $pass);
            $this->pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $e) {
            // Handle connection error
            die("Database connection failed: " . $e->getMessage());
        }
    }

    /**
     * Retrieve all series in the 'Terror' category.
     *
     * @return array List of series in the 'Terror' category
     */
    public function getTerrorSeries() {
        $sql = "SELECT * FROM series WHERE category = :category";
        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute(['category' => 'Terror']);
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            // Handle query error
            die("Query failed: " . $e->getMessage());
        }
    }
}

// Usage example
try {
    // Database credentials
    $host = 'localhost';
    $db = 'SeriesFlix';
    $user = 'your_username';
    $pass = 'your_password';

    // Create an instance of the database class
    $database = new SeriesFlixDatabase($host, $db, $user, $pass);

    // Retrieve and display series in the 'Terror' category
    $terrorSeries = $database->getTerrorSeries();
    foreach ($terrorSeries as $series) {
        echo "Title: " . htmlspecialchars($series['title']) . "<br>";
        echo "Description: " . htmlspecialchars($series['description']) . "<br><br>";
    }
} catch (Exception $e) {
    // Handle any unexpected errors
    die("An unexpected error occurred: " . $e->getMessage());
}
?>
```
