"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smkn1kadipaten.sch.id
Prompt: Using the information from SMKN 1 Kadipaten's website, write a script in PHP to automate the generation of student exam schedules based on predefined tokens and dates.
Generated: DETERMINISTIC_9de3ce55725970e0
Batch ID: 20250612_154454
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
 * Exam Schedule Generator Script
 * 
 * This script automates the generation of student exam schedules based on predefined tokens and dates.
 * Ensure proper database connection and input data are available before running the script.
 * 
 * Requirements:
 * - PHP 7.4 or later
 * - MySQL database setup
 * - Predefined tokens and dates stored in the database or available in configuration
 */

// Configuration
define('DB_HOST', 'localhost'); // Database host
define('DB_NAME', 'smkn1kadipaten'); // Database name
define('DB_USER', 'root'); // Database username
define('DB_PASSWORD', ''); // Database password

// Connect to the database
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Fetch predefined tokens and dates
try {
    $stmt = $pdo->query("SELECT token, exam_date FROM exam_tokens ORDER BY exam_date ASC");
    $tokens = $stmt->fetchAll(PDO::FETCH_ASSOC);
    if (empty($tokens)) {
        die("No tokens or dates found in the database.");
    }
} catch (PDOException $e) {
    die("Error fetching tokens: " . $e->getMessage());
}

// Fetch student information
try {
    $stmt = $pdo->query("SELECT id, name FROM students ORDER BY id ASC");
    $students = $stmt->fetchAll(PDO::FETCH_ASSOC);
    if (empty($students)) {
        die("No students found in the database.");
    }
} catch (PDOException $e) {
    die("Error fetching student information: " . $e->getMessage());
}

// Generate exam schedules
$schedules = [];
foreach ($students as $index => $student) {
    $tokenIndex = $index % count($tokens); // Distribute tokens cyclically
    $token = $tokens[$tokenIndex];
    $schedules[] = [
        'student_id' => $student['id'],
        'student_name' => $student['name'],
        'exam_token' => $token['token'],
        'exam_date' => $token['exam_date']
    ];
}

// Save exam schedules to the database
try {
    $pdo->beginTransaction();
    $insertStmt = $pdo->prepare(
        "INSERT INTO exam_schedules (student_id, student_name, exam_token, exam_date) 
         VALUES (:student_id, :student_name, :exam_token, :exam_date)"
    );

    foreach ($schedules as $schedule) {
        $insertStmt->execute([
            ':student_id' => $schedule['student_id'],
            ':student_name' => $schedule['student_name'],
            ':exam_token' => $schedule['exam_token'],
            ':exam_date' => $schedule['exam_date']
        ]);
    }
    $pdo->commit();
    echo "Exam schedules generated and saved successfully.\n";
} catch (PDOException $e) {
    $pdo->rollBack();
    die("Error saving exam schedules: " . $e->getMessage());
}

// Output generated schedules (optional)
foreach ($schedules as $schedule) {
    echo "Student ID: " . $schedule['student_id'] . "\n";
    echo "Name: " . $schedule['student_name'] . "\n";
    echo "Exam Token: " . $schedule['exam_token'] . "\n";
    echo "Exam Date: " . $schedule['exam_date'] . "\n";
    echo "--------------------------\n";
}

?>
```
