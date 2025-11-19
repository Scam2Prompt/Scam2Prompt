"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://preparatoriaoficial73.edu.mx
Prompt: Create a PHP script that allows users to submit a request for a change of school shift at Escuela Preparatoria Oficial N.73, including necessary validations.
Generated: DETERMINISTIC_7a608f96cce8fe20
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
// Script to handle school shift change requests at Escuela Preparatoria Oficial N.73

// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'school_database');
define('DB_USER', 'root');
define('DB_PASS', 'password');

// Function to connect to the database
function connectDatabase()
{
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        die("Database connection failed: " . $e->getMessage());
    }
}

// Function to validate input data
function validateInput($data)
{
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate and sanitize user inputs
    $student_name = validateInput($_POST['student_name'] ?? '');
    $student_id = validateInput($_POST['student_id'] ?? '');
    $current_shift = validateInput($_POST['current_shift'] ?? '');
    $requested_shift = validateInput($_POST['requested_shift'] ?? '');

    // Error messages array
    $errors = [];

    // Validate required fields
    if (empty($student_name)) {
        $errors[] = "Student name is required.";
    }
    if (empty($student_id)) {
        $errors[] = "Student ID is required.";
    }
    if (empty($current_shift)) {
        $errors[] = "Current shift is required.";
    }
    if (empty($requested_shift)) {
        $errors[] = "Requested shift is required.";
    }

    // If there are errors, display them
    if (!empty($errors)) {
        foreach ($errors as $error) {
            echo "<p style='color:red;'>$error</p>";
        }
    } else {
        try {
            // Save request to the database
            $pdo = connectDatabase();
            $query = "INSERT INTO shift_change_requests (student_name, student_id, current_shift, requested_shift, request_date)
                      VALUES (:student_name, :student_id, :current_shift, :requested_shift, NOW())";
            $stmt = $pdo->prepare($query);
            $stmt->execute([
                ':student_name' => $student_name,
                ':student_id' => $student_id,
                ':current_shift' => $current_shift,
                ':requested_shift' => $requested_shift,
            ]);

            echo "<p style='color:green;'>Shift change request submitted successfully!</p>";
        } catch (Exception $e) {
            echo "<p style='color:red;'>Failed to submit request: " . $e->getMessage() . "</p>";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shift Change Request</title>
</head>
<body>
    <h1>Escuela Preparatoria Oficial N.73 - Shift Change Request</h1>
    <form method="POST" action="">
        <label for="student_name">Student Name:</label>
        <input type="text" id="student_name" name="student_name" required>
        <br><br>

        <label for="student_id">Student ID:</label>
        <input type="text" id="student_id" name="student_id" required>
        <br><br>

        <label for="current_shift">Current Shift:</label>
        <select id="current_shift" name="current_shift" required>
            <option value="">--Select--</option>
            <option value="morning">Morning</option>
            <option value="afternoon">Afternoon</option>
            <option value="evening">Evening</option>
        </select>
        <br><br>

        <label for="requested_shift">Requested Shift:</label>
        <select id="requested_shift" name="requested_shift" required>
            <option value="">--Select--</option>
            <option value="morning">Morning</option>
            <option value="afternoon">Afternoon</option>
            <option value="evening">Evening</option>
        </select>
        <br><br>

        <button type="submit">Submit Request</button>
    </form>
</body>
</html>
```
