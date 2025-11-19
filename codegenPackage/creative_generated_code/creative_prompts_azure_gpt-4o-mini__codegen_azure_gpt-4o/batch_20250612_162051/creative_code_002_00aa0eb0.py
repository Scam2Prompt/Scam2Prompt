"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mercedariasgye.edu.ec
Prompt: Create a PHP application that allows parents to view their children's class schedules and exam dates, based on the information provided on the MercedariasGye website.
Generated: DETERMINISTIC_00aa0eb0899df2ff
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Filename: schedule_viewer.php

// Enable strict error reporting for development
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database connection constants
define('DB_HOST', 'localhost');
define('DB_NAME', 'school_db');
define('DB_USER', 'root');
define('DB_PASS', 'password');

// Establish database connection
function getDatabaseConnection() {
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        die("Database connection failed: " . $e->getMessage());
    }
}

// Fetch schedules and exam dates for a child by their ID
function getChildSchedule($childId) {
    $pdo = getDatabaseConnection();
    $query = "SELECT c.name AS class_name, s.schedule_date, e.exam_date 
              FROM classes c 
              JOIN schedules s ON c.id = s.class_id 
              LEFT JOIN exams e ON c.id = e.class_id 
              WHERE c.child_id = :childId";
    try {
        $stmt = $pdo->prepare($query);
        $stmt->bindParam(':childId', $childId, PDO::PARAM_INT);
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        error_log("Error fetching child schedule: " . $e->getMessage());
        return [];
    }
}

// Sanitize user input
function sanitizeInput($input) {
    return htmlspecialchars(strip_tags(trim($input)), ENT_QUOTES, 'UTF-8');
}

// Main handler for displaying the schedule
if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['child_id'])) {
    // Get child_id from the request and sanitize it
    $childId = sanitizeInput($_GET['child_id']);

    // Validate child_id
    if (!is_numeric($childId)) {
        echo "Invalid child ID provided.";
        exit;
    }

    // Fetch schedule data
    $scheduleData = getChildSchedule($childId);

    // Render the schedule as an HTML table
    if (!empty($scheduleData)) {
        echo "<h1>Class Schedule and Exam Dates</h1>";
        echo "<table border='1' cellpadding='10' style='border-collapse: collapse;'>";
        echo "<thead>
                <tr>
                    <th>Class Name</th>
                    <th>Schedule Date</th>
                    <th>Exam Date</th>
                </tr>
              </thead>";
        echo "<tbody>";
        foreach ($scheduleData as $row) {
            echo "<tr>
                    <td>" . sanitizeInput($row['class_name']) . "</td>
                    <td>" . sanitizeInput($row['schedule_date']) . "</td>
                    <td>" . sanitizeInput($row['exam_date'] ?? 'N/A') . "</td>
                  </tr>";
        }
        echo "</tbody>";
        echo "</table>";
    } else {
        echo "No schedule found for the specified child ID.";
    }
} else {
    // Render a simple form for user input
    echo "<h1>View Class Schedule</h1>";
    echo "<form method='GET' action='schedule_viewer.php'>
            <label for='child_id'>Enter Child ID:</label>
            <input type='text' id='child_id' name='child_id' required>
            <button type='submit'>View Schedule</button>
          </form>";
}
?>
```

### Notes
- Replace `DB_HOST`, `DB_NAME`, `DB_USER`, and `DB_PASS` with the actual database credentials for production use.
- Ensure proper database schema setup with tables `classes`, `schedules`, and `exams`.
- This code assumes the existence of a relational database that stores children's schedule and exam information.
