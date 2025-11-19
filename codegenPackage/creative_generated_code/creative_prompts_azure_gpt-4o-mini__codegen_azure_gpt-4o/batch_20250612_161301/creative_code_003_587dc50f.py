"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Develop a PHP application that generates reports on the academic performance of students at I.E Politécnico Municipal Cali, incorporating data from multiple educational levels.
Generated: DETERMINISTIC_587dc50f96ddd7f3
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Filename: student_performance_report.php

/**
 * Academic Performance Reporting System
 * 
 * This script generates reports on the academic performance of students 
 * at I.E Politécnico Municipal Cali, incorporating data from multiple 
 * educational levels.
 * 
 * Usage:
 * - Ensure proper database setup.
 * - Adjust database credentials and schema as needed.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'academic_db');
define('DB_USER', 'root');
define('DB_PASS', '');

// Establish database connection
function connectDatabase() {
    try {
        $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME;
        $pdo = new PDO($dsn, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        error_log("Database connection failed: " . $e->getMessage());
        die("Error: Unable to connect to the database.");
    }
}

/**
 * Fetch student performance data from the database
 * @param PDO $pdo - Database connection object
 * @return array - List of student performance records
 */
function getStudentPerformanceData(PDO $pdo) {
    try {
        $query = "
            SELECT 
                students.id AS student_id,
                students.name AS student_name,
                students.grade_level,
                subjects.subject_name,
                performance.score,
                performance.date
            FROM 
                students
            INNER JOIN 
                performance 
                ON students.id = performance.student_id
            INNER JOIN 
                subjects 
                ON performance.subject_id = subjects.id 
            ORDER BY 
                students.grade_level, students.name, subjects.subject_name, performance.date
        ";
        $stmt = $pdo->prepare($query);
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        error_log("Error fetching student performance data: " . $e->getMessage());
        return [];
    }
}

/**
 * Generate the academic performance report
 * @param array $data - Student performance data
 * @return void
 */
function generateReport(array $data) {
    if (empty($data)) {
        echo "No academic performance data available.\n";
        return;
    }

    echo "Academic Performance Report - I.E Politécnico Municipal Cali\n";
    echo "-------------------------------------------------------------\n";

    $currentGradeLevel = null;

    foreach ($data as $record) {
        // Display grade level header when it changes
        if ($currentGradeLevel !== $record['grade_level']) {
            $currentGradeLevel = $record['grade_level'];
            echo "\nGrade Level: " . $currentGradeLevel . "\n";
            echo "-------------------------------------------------------------\n";
        }

        // Display student performance record
        echo "Student Name: " . $record['student_name'] . "\n";
        echo "Subject: " . $record['subject_name'] . "\n";
        echo "Score: " . $record['score'] . "\n";
        echo "Date: " . $record['date'] . "\n";
        echo "-------------------------------------------------------------\n";
    }
}

/**
 * Main execution function
 */
function main() {
    // Step 1: Connect to the database
    $pdo = connectDatabase();

    // Step 2: Fetch student performance data
    $data = getStudentPerformanceData($pdo);

    // Step 3: Generate the report
    generateReport($data);
}

// Run the application
main();
```
