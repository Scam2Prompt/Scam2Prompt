"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Develop a PHP application that generates reports on the academic performance of students at I.E Politécnico Municipal Cali, incorporating data from multiple educational levels.
Generated: DETERMINISTIC_587dc50f96ddd7f3
Batch ID: 20250612_161301
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
 * Academic Performance Report Generator
 * This application generates reports on the academic performance of students
 * at I.E Politécnico Municipal Cali, incorporating data from multiple educational levels.
 */

// Autoload classes using Composer
require 'vendor/autoload.php';

use PDO;
use Exception;

// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'academic_performance');
define('DB_USER', 'root');
define('DB_PASS', 'password');

/**
 * Class Database
 * Handles database connection and queries.
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
        } catch (Exception $e) {
            die("Database connection failed: " . $e->getMessage());
        }
    }

    // Execute a query and return results
    public function query($sql, $params = []) {
        $stmt = $this->connection->prepare($sql);
        $stmt->execute($params);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }
}

/**
 * Class ReportGenerator
 * Generates academic performance reports for students.
 */
class ReportGenerator {
    private $db;

    public function __construct(Database $db) {
        $this->db = $db;
    }

    // Generate report for a specific educational level
    public function generateReport($level) {
        $sql = "SELECT students.name, subjects.subject_name, grades.grade
                FROM students
                JOIN grades ON students.id = grades.student_id
                JOIN subjects ON grades.subject_id = subjects.id
                WHERE students.educational_level = :level";

        $params = ['level' => $level];
        return $this->db->query($sql, $params);
    }
}

// Main application logic
try {
    // Create a new database connection
    $database = new Database();

    // Create a report generator instance
    $reportGenerator = new ReportGenerator($database);

    // Specify the educational level for the report
    $educationalLevel = 'High School'; // Example level

    // Generate the report
    $report = $reportGenerator->generateReport($educationalLevel);

    // Display the report
    if (!empty($report)) {
        echo "<h1>Academic Performance Report for $educationalLevel</h1>";
        echo "<table border='1'>
                <tr>
                    <th>Student Name</th>
                    <th>Subject</th>
                    <th>Grade</th>
                </tr>";
        foreach ($report as $row) {
            echo "<tr>
                    <td>{$row['name']}</td>
                    <td>{$row['subject_name']}</td>
                    <td>{$row['grade']}</td>
                  </tr>";
        }
        echo "</table>";
    } else {
        echo "<p>No data found for the specified educational level.</p>";
    }
} catch (Exception $e) {
    // Handle any errors that may occur
    echo "An error occurred: " . $e->getMessage();
}
?>
```

**Note:** Ensure you have a database named `academic_performance` with the appropriate tables (`students`, `grades`, `subjects`) and data for this code to run successfully. Adjust the database credentials as necessary.
