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
// ClassSchedule.php
// A simple PHP application to view children's class schedules and exam dates

// Enabling error reporting for development
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database connection details
define('DB_HOST', 'localhost');
define('DB_NAME', 'school');
define('DB_USER', 'root');
define('DB_PASS', '');

// Function to establish a database connection
function getDBConnection() {
    try {
        $pdo = new PDO("mysql:host=".DB_HOST.";dbname=".DB_NAME, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        // Handle connection errors
        error_log("Database connection error: " . $e->getMessage());
        die("Could not connect to the database. Please try again later.");
    }
}

// Function to fetch class schedules for a specific student
function getClassSchedule($studentId) {
    $pdo = getDBConnection();
    $sql = "SELECT subject, class_time FROM class_schedule WHERE student_id = :student_id";

    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute(['student_id' => $studentId]);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        error_log("Error fetching class schedule: " . $e->getMessage());
        return [];
    }
}

// Function to fetch exam dates for a specific student
function getExamDates($studentId) {
    $pdo = getDBConnection();
    $sql = "SELECT subject, exam_date FROM exams WHERE student_id = :student_id";

    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute(['student_id' => $studentId]);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        error_log("Error fetching exam dates: " . $e->getMessage());
        return [];
    }
}

// Main script
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['student_id'])) {
    $studentId = htmlspecialchars($_POST['student_id']);

    $classSchedule = getClassSchedule($studentId);
    $examDates = getExamDates($studentId);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Class Schedules and Exam Dates</title>
</head>
<body>
    <h1>View Class Schedules and Exam Dates</h1>

    <form method="post">
        <label for="student_id">Enter Student ID:</label>
        <input type="text" name="student_id" id="student_id" required>
        <button type="submit">View Schedule</button>
    </form>

    <?php if (isset($classSchedule) || isset($examDates)): ?>
        <h2>Class Schedule</h2>
        <table>
            <thead>
                <tr>
                    <th>Subject</th>
                    <th>Class Time</th>
                </tr>
            </thead>
            <tbody>
                <?php if (empty($classSchedule)): ?>
                    <tr><td colspan="2">No class schedule found.</td></tr>
                <?php else: ?>
                    <?php foreach ($classSchedule as $class): ?>
                        <tr>
                            <td><?php echo htmlspecialchars($class['subject']); ?></td>
                            <td><?php echo htmlspecialchars($class['class_time']); ?></td>
                        </tr>
                    <?php endforeach; ?>
                <?php endif; ?>
            </tbody>
        </table>

        <h2>Exam Dates</h2>
        <table>
            <thead>
                <tr>
                    <th>Subject</th>
                    <th>Exam Date</th>
                </tr>
            </thead>
            <tbody>
                <?php if (empty($examDates)): ?>
                    <tr><td colspan="2">No exam dates found.</td></tr>
                <?php else: ?>
                    <?php foreach ($examDates as $exam): ?>
                        <tr>
                            <td><?php echo htmlspecialchars($exam['subject']); ?></td>
                            <td><?php echo htmlspecialchars($exam['exam_date']); ?></td>
                        </tr>
                    <?php endforeach; ?>
                <?php endif; ?>
            </tbody>
        </table>
    <?php endif; ?>
</body>
</html>
```
