"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fijimaths.com
Prompt: Create a PHP script that collects and stores the results of the Fiji Mathematics Awards, including student names, categories, and prizes.
Generated: DETERMINISTIC_f31d2bb0604cf757
Batch ID: 20250612_161235
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
 * Fiji Mathematics Awards Results Collector
 * 
 * This script collects and stores the results of the Fiji Mathematics Awards,
 * including student names, categories, and prizes. It connects to a MySQL database
 * to save the results and handles input validation and error reporting.
 */

// Database configuration
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'username');   // Database user
define('DB_PASS', 'password');   // Database password
define('DB_NAME', 'fiji_math_awards'); // Database name

// Create a connection to the database
$conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

/**
 * Function to sanitize input data to prevent SQL injection
 * 
 * @param string $data Input data to sanitize
 * @return string Sanitized data
 */
function sanitizeInput($data) {
    global $conn;
    return $conn->real_escape_string(trim($data));
}

/**
 * Function to store award results in the database
 * 
 * @param string $studentName Name of the student
 * @param string $category Award category
 * @param string $prize Prize awarded
 * @return void
 */
function storeAwardResult($studentName, $category, $prize) {
    global $conn;

    // Sanitize inputs
    $studentName = sanitizeInput($studentName);
    $category = sanitizeInput($category);
    $prize = sanitizeInput($prize);

    // Prepare and bind
    $stmt = $conn->prepare("INSERT INTO awards (student_name, category, prize) VALUES (?, ?, ?)");
    
    if ($stmt === false) {
        die("Prepare failed: " . $conn->error);
    }

    $stmt->bind_param("sss", $studentName, $category, $prize);

    // Execute the statement
    if (!$stmt->execute()) {
        echo "Error: " . $stmt->error;
    } else {
        echo "Record stored successfully for $studentName.";
    }

    // Close the statement
    $stmt->close();
}

// Example usage
// Collecting data (in practice, this would come from a form submission)
$studentName = "John Doe"; // Replace with actual data
$category = "Best Problem Solver"; // Replace with actual data
$prize = "Gold Medal"; // Replace with actual data

// Store the result
storeAwardResult($studentName, $category, $prize);

// Close the database connection
$conn->close();
?>
```

**Note:** Make sure to replace the database connection parameters (`DB_USER`, `DB_PASS`, and `DB_NAME`) with actual values before running the script. The table `awards` should exist in the database with appropriate columns: `student_name`, `category`, and `prize`.
