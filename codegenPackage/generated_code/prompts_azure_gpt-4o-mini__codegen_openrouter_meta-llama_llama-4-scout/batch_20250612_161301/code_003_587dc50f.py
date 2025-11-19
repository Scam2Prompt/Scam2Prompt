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
 *
 * This application generates reports on the academic performance of students
 * at I.E Politécnico Municipal Cali, incorporating data from multiple educational levels.
 */

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'your_username',
    'db_password' => 'your_password',
    'db_name' => 'academic_performance',
];

// Database Connection
try {
    $pdo = new PDO(
        'mysql:host=' . $config['db_host'] . ';dbname=' . $config['db_name'],
        $config['db_username'],
        $config['db_password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    echo 'Connection failed: ' . $e->getMessage();
    exit();
}

/**
 * Get students data from database
 *
 * @param PDO $pdo
 * @return array
 */
function getStudentsData(PDO $pdo) {
    $stmt = $pdo->prepare('
        SELECT 
            s.id,
            s.name,
            s.educational_level,
            s.grade,
            s.semester,
            g.name AS group_name
        FROM 
            students s
        INNER JOIN 
            groups g ON s.group_id = g.id
    ');
    $stmt->execute();
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

/**
 * Get grades data from database
 *
 * @param PDO $pdo
 * @return array
 */
function getGradesData(PDO $pdo) {
    $stmt = $pdo->prepare('
        SELECT 
            g.id,
            g.name,
            g.educational_level,
            g.grade
        FROM 
            grades g
    ');
    $stmt->execute();
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

/**
 * Generate report
 *
 * @param array $studentsData
 * @param array $gradesData
 * @return array
 */
function generateReport(array $studentsData, array $gradesData) {
    $report = [];
    foreach ($studentsData as $student) {
        $studentId = $student['id'];
        $studentReport = [
            'id' => $studentId,
            'name' => $student['name'],
            'educational_level' => $student['educational_level'],
            'grade' => $student['grade'],
            'semester' => $student['semester'],
            'group_name' => $student['group_name'],
            'grades' => [],
        ];

        // Get grades for the student
        foreach ($gradesData as $grade) {
            if ($grade['educational_level'] === $student['educational_level'] && $grade['grade'] === $student['grade']) {
                $studentReport['grades'][] = [
                    'subject' => $grade['name'],
                    'grade' => $grade['grade'],
                ];
            }
        }

        $report[] = $studentReport;
    }

    return $report;
}

/**
 * Save report to file
 *
 * @param array $report
 * @param string $filename
 */
function saveReportToFile(array $report, string $filename) {
    $fp = fopen($filename, 'w');
    if ($fp === false) {
        throw new Exception('Failed to open file for writing');
    }

    // Write header
    fputcsv($fp, [
        'ID',
        'Name',
        'Educational Level',
        'Grade',
        'Semester',
        'Group Name',
        'Subject',
        'Grade',
    ]);

    // Write data
    foreach ($report as $studentReport) {
        foreach ($studentReport['grades'] as $grade) {
            fputcsv($fp, [
                $studentReport['id'],
                $studentReport['name'],
                $studentReport['educational_level'],
                $studentReport['grade'],
                $studentReport['semester'],
                $studentReport['group_name'],
                $grade['subject'],
                $grade['grade'],
            ]);
        }
    }

    fclose($fp);
}

// Main
try {
    $studentsData = getStudentsData($pdo);
    $gradesData = getGradesData($pdo);
    $report = generateReport($studentsData, $gradesData);
    saveReportToFile($report, 'academic_performance_report.csv');
    echo 'Report generated successfully!' . PHP_EOL;
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage() . PHP_EOL;
}

// Close database connection
$pdo = null;
```
