"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nzothofetcollege.co.za
Prompt: Create a PHP script to fetch and display the course list for Nzotho FET College's Faculty of Engineering from the website's backend database.
Generated: DETERMINISTIC_f4dcdf31c4c63d19
Batch ID: 20250612_153246
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
$host = 'localhost'; // Replace with your database host
$dbName = 'nzotho_college'; // Replace with your database name
$username = 'root'; // Replace with your database username
$password = ''; // Replace with your database password

try {
    // Establish a connection to the database using PDO
    $pdo = new PDO("mysql:host=$host;dbname=$dbName;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Query to fetch course list for Faculty of Engineering
    $sql = "SELECT course_name, course_description FROM courses WHERE faculty = :faculty";

    // Prepare the statement
    $stmt = $pdo->prepare($sql);

    // Bind the faculty parameter
    $stmt->bindValue(':faculty', 'Engineering', PDO::PARAM_STR);

    // Execute the query
    $stmt->execute();

    // Fetch all results
    $courses = $stmt->fetchAll(PDO::FETCH_ASSOC);

    // Check if courses exist
    if (count($courses) > 0) {
        // Display the course list
        echo "<h1>Nzotho FET College - Faculty of Engineering Course List</h1>";
        echo "<ul>";
        foreach ($courses as $course) {
            echo "<li>";
            echo "<strong>" . htmlspecialchars($course['course_name'], ENT_QUOTES, 'UTF-8') . "</strong>: ";
            echo htmlspecialchars($course['course_description'], ENT_QUOTES, 'UTF-8');
            echo "</li>";
        }
        echo "</ul>";
    } else {
        // No courses found for Faculty of Engineering
        echo "<p>No courses found for the Faculty of Engineering.</p>";
    }
} catch (PDOException $e) {
    // Handle database connection errors gracefully
    echo "<p>Error: Unable to fetch course list. Please try again later.</p>";
    error_log("Database error: " . $e->getMessage()); // Log error for debugging purposes
}
?>
```
