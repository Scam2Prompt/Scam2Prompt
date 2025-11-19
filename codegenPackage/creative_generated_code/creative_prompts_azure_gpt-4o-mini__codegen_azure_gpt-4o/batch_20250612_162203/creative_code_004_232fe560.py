"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghmc.edu.au
Prompt: Design a web service in PHP that lists all available online courses at Global Healthcare Management College and their respective durations and fees.
Generated: DETERMINISTIC_232fe5600ab0385d
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File: courses_service.php

// Enable error reporting for debugging purposes (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Define a function to establish database connection
function getDatabaseConnection() {
    $host = 'localhost'; // Database host
    $dbname = 'college_db'; // Database name
    $username = 'root'; // Database username
    $password = ''; // Database password

    try {
        // Create a new PDO instance for database connection
        $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Enable exception handling
        return $pdo;
    } catch (PDOException $e) {
        // Handle connection errors
        http_response_code(500);
        echo json_encode(['error' => 'Database connection failed: ' . $e->getMessage()]);
        exit;
    }
}

// Define a function to fetch courses from the database
function fetchCourses() {
    try {
        $pdo = getDatabaseConnection();
        // Prepare SQL query to fetch all courses
        $query = "SELECT course_name, duration, fee FROM courses WHERE is_online = 1";
        $stmt = $pdo->prepare($query);
        $stmt->execute();

        // Fetch all courses as an associative array
        $courses = $stmt->fetchAll(PDO::FETCH_ASSOC);
        return $courses;
    } catch (PDOException $e) {
        // Handle query errors
        http_response_code(500);
        echo json_encode(['error' => 'Failed to fetch courses: ' . $e->getMessage()]);
        exit;
    }
}

// Main entry point for the service
header('Content-Type: application/json'); // Set the response type to JSON

try {
    // Fetch courses
    $courses = fetchCourses();

    // Respond with the list of courses
    echo json_encode(['status' => 'success', 'data' => $courses]);
} catch (Exception $e) {
    // Handle unexpected errors
    http_response_code(500);
    echo json_encode(['error' => 'An unexpected error occurred: ' . $e->getMessage()]);
}
?>
```

---

**Notes for Deployment**:
1. Replace the database credentials (`host`, `dbname`, `username`, `password`) with the appropriate values for your setup.
2. Ensure the database table `courses` exists with the fields `course_name`, `duration`, `fee`, and `is_online`.
3. Disable error reporting (`error_reporting` and `ini_set`) in production for security purposes.
