"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fijimaths.com
Prompt: Create a PHP script that collects and stores the results of the Fiji Mathematics Awards, including student names, categories, and prizes.
Generated: DETERMINISTIC_f31d2bb0604cf757
Batch ID: 20250612_161235
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
 * Fiji Mathematics Awards Results Collection Script
 * 
 * This script collects and stores results for the Fiji Mathematics Awards.
 * It uses a MySQL database to save data including student names, award categories, and prizes.
 * Ensure the database connection settings are configured correctly before running.
 */

// Database configuration
define('DB_HOST', 'localhost'); // Replace with your database host
define('DB_NAME', 'fiji_awards'); // Replace with your database name
define('DB_USER', 'root'); // Replace with your database username
define('DB_PASS', 'password'); // Replace with your database password

/**
 * Establish a connection to the database.
 * 
 * @return PDO The database connection object.
 * @throws Exception if the connection fails.
 */
function getDatabaseConnection()
{
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS, [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
        ]);
        return $pdo;
    } catch (PDOException $e) {
        throw new Exception("Database connection failed: " . $e->getMessage());
    }
}

/**
 * Create the awards table if it doesn't exist.
 * 
 * @param PDO $pdo The database connection object.
 */
function initializeDatabase(PDO $pdo)
{
    $sql = "
        CREATE TABLE IF NOT EXISTS awards (
            id INT AUTO_INCREMENT PRIMARY KEY,
            student_name VARCHAR(255) NOT NULL,
            category VARCHAR(255) NOT NULL,
            prize VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ";
    $pdo->exec($sql);
}

/**
 * Save award results to the database.
 * 
 * @param PDO $pdo The database connection object.
 * @param string $student_name The name of the student.
 * @param string $category The award category.
 * @param string $prize The prize received.
 * @return bool True if the record was saved successfully, false otherwise.
 */
function saveAwardResult(PDO $pdo, $student_name, $category, $prize)
{
    try {
        $sql = "INSERT INTO awards (student_name, category, prize) VALUES (:student_name, :category, :prize)";
        $stmt = $pdo->prepare($sql);
        $stmt->bindParam(':student_name', $student_name);
        $stmt->bindParam(':category', $category);
        $stmt->bindParam(':prize', $prize);
        return $stmt->execute();
    } catch (PDOException $e) {
        error_log("Failed to save award result: " . $e->getMessage());
        return false;
    }
}

/**
 * Main function to handle the script execution.
 */
function main()
{
    // Collect input data (In production, replace this with form inputs or API request handling)
    $student_name = readline("Enter student name: ");
    $category = readline("Enter award category: ");
    $prize = readline("Enter prize: ");

    try {
        // Initialize the database and save results
        $pdo = getDatabaseConnection();
        initializeDatabase($pdo);
        $success = saveAwardResult($pdo, $student_name, $category, $prize);

        if ($success) {
            echo "Award result saved successfully.\n";
        } else {
            echo "Failed to save award result.\n";
        }
    } catch (Exception $e) {
        echo "An error occurred: " . $e->getMessage() . "\n";
    }
}

// Execute the script
main();
?>
```
