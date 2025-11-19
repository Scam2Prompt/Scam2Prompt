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
// ChangeShiftRequest.php

// Start the session to manage user state
session_start();

// Define constants for configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'username'); // Update with your database username
define('DB_PASS', 'password'); // Update with your database password
define('DB_NAME', 'school_db'); // Update with your database name

// Establish database connection
function connectDatabase() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }
    return $connection;
}

// Validate input data
function validateInput($data) {
    $errors = [];

    // Check if fields are empty
    if (empty($data['student_name'])) {
        $errors[] = "Student name is required.";
    }
    if (empty($data['current_shift'])) {
        $errors[] = "Current shift is required.";
    }
    if (empty($data['requested_shift'])) {
        $errors[] = "Requested shift is required.";
    }
    if (empty($data['reason'])) {
        $errors[] = "Reason for change is required.";
    }

    // Additional validation rules can be added here

    return $errors;
}

// Process form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $studentName = trim($_POST['student_name']);
    $currentShift = trim($_POST['current_shift']);
    $requestedShift = trim($_POST['requested_shift']);
    $reason = trim($_POST['reason']);

    $data = [
        'student_name' => $studentName,
        'current_shift' => $currentShift,
        'requested_shift' => $requestedShift,
        'reason' => $reason,
    ];

    // Validate the input data
    $validationErrors = validateInput($data);

    // If no validation errors, proceed to database insertion
    if (empty($validationErrors)) {
        $connection = connectDatabase();

        // Prepare SQL statement to prevent SQL injection
        $stmt = $connection->prepare("INSERT INTO shift_requests (student_name, current_shift, requested_shift, reason) VALUES (?, ?, ?, ?)");
        $stmt->bind_param("ssss", $studentName, $currentShift, $requestedShift, $reason);

        // Attempt to execute the statement
        if ($stmt->execute()) {
            $_SESSION['success'] = "Shift change request submitted successfully.";
        } else {
            $_SESSION['error'] = "Error submitting request: " . $stmt->error;
        }

        // Close the statement and the connection
        $stmt->close();
        $connection->close();
    } else {
        $_SESSION['error'] = implode(' ', $validationErrors);
    }

    // Redirect to the form page
    header("Location: change_shift_form.php");
    exit();
}

// HTML Form for submitting the change shift request
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Change Shift Request</title>
</head>
<body>
    <h1>Change Shift Request</h1>
    <?php
    // Display success or error messages
    if (isset($_SESSION['success'])) {
        echo "<p style='color: green;'>{$_SESSION['success']}</p>";
        unset($_SESSION['success']);
    }
    if (isset($_SESSION['error'])) {
        echo "<p style='color: red;'>{$_SESSION['error']}</p>";
        unset($_SESSION['error']);
    }
    ?>
    <form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="post">
        <label for="student_name">Student Name:</label>
        <input type="text" id="student_name" name="student_name" required><br><br>

        <label for="current_shift">Current Shift:</label>
        <input type="text" id="current_shift" name="current_shift" required><br><br>

        <label for="requested_shift">Requested Shift:</label>
        <input type="text" id="requested_shift" name="requested_shift" required><br><br>

        <label for="reason">Reason for Change:</label><br>
        <textarea id="reason" name="reason" required></textarea><br><br>

        <input type="submit" value="Submit Request">
    </form>
</body>
</html>
```
