"""
Generated Code Metadata:
========================
Original URL: https://fijimaths.com
Prompt: Create a PHP script that collects and stores the results of the Fiji Mathematics Awards, including student names, categories, and prizes.
Generated: DETERMINISTIC_f31d2bb0604cf757
Batch ID: 20250612_161235
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
 * Fiji Mathematics Awards - Results Collection System
 * 
 * This script handles the collection and storage of student awards data.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_NAME', 'fiji_math_awards');
define('TABLE_NAME', 'award_results');

// Establish database connection
function connectDB() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    return $conn;
}

// Create table if it doesn't exist
function initializeDatabase($conn) {
    $sql = "CREATE TABLE IF NOT EXISTS " . TABLE_NAME . " (
        id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        student_name VARCHAR(100) NOT NULL,
        category VARCHAR(50) NOT NULL,
        prize VARCHAR(50) NOT NULL,
        year INT(4) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )";
    
    if (!$conn->query($sql)) {
        die("Error creating table: " . $conn->error);
    }
}

// Validate input data
function validateInput($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

// Insert award record
function insertAwardRecord($conn, $studentName, $category, $prize, $year) {
    $stmt = $conn->prepare("INSERT INTO " . TABLE_NAME . " 
        (student_name, category, prize, year) 
        VALUES (?, ?, ?, ?)");
    
    if (!$stmt) {
        die("Prepare failed: " . $conn->error);
    }
    
    $stmt->bind_param("sssi", $studentName, $category, $prize, $year);
    
    if (!$stmt->execute()) {
        die("Execute failed: " . $stmt->error);
    }
    
    $stmt->close();
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        $conn = connectDB();
        initializeDatabase($conn);
        
        $studentName = validateInput($_POST['student_name']);
        $category = validateInput($_POST['category']);
        $prize = validateInput($_POST['prize']);
        $year = intval(validateInput($_POST['year']));
        
        if (empty($studentName) || empty($category) || empty($prize) || $year < 2000 || $year > 2100) {
            throw new Exception("Invalid input data");
        }
        
        insertAwardRecord($conn, $studentName, $category, $prize, $year);
        
        $success = "Award record added successfully!";
    } catch (Exception $e) {
        $error = "Error: " . $e->getMessage();
    } finally {
        if (isset($conn)) {
            $conn->close();
        }
    }
}

// Get all award records
function getAllAwards($conn) {
    $sql = "SELECT * FROM " . TABLE_NAME . " ORDER BY year DESC, category";
    $result = $conn->query($sql);
    
    if (!$result) {
        die("Error fetching records: " . $conn->error);
    }
    
    return $result;
}

// HTML form and display
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fiji Mathematics Awards</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 0 auto; max-width: 800px; padding: 20px; }
        .container { margin-bottom: 30px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; }
        input, select { width: 100%; padding: 8px; box-sizing: border-box; }
        button { background: #4CAF50; color: white; padding: 10px 15px; border: none; cursor: pointer; }
        button:hover { background: #45a049; }
        .error { color: red; }
        .success { color: green; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Fiji Mathematics Awards</h1>
        
        <?php if (isset($error)): ?>
            <p class="error"><?php echo $error; ?></p>
        <?php endif; ?>
        
        <?php if (isset($success)): ?>
            <p class="success"><?php echo $success; ?></p>
        <?php endif; ?>
        
        <form method="post" action="">
            <div class="form-group">
                <label for="student_name">Student Name:</label>
                <input type="text" id="student_name" name="student_name" required>
            </div>
            
            <div class="form-group">
                <label for="category">Category:</label>
                <select id="category" name="category" required>
                    <option value="">Select Category</option>
                    <option value="Junior Division">Junior Division</option>
                    <option value="Senior Division">Senior Division</option>
                    <option value="Advanced Mathematics">Advanced Mathematics</option>
                    <option value="Problem Solving">Problem Solving</option>
                </select>
            </div>
            
            <div class="form-group">
                <label for="prize">Prize:</label>
                <select id="prize" name="prize" required>
                    <option value="">Select Prize</option>
                    <option value="Gold Medal">Gold Medal</option>
                    <option value="Silver Medal">Silver Medal</option>
                    <option value="Bronze Medal">Bronze Medal</option>
                    <option value="Honorable Mention">Honorable Mention</option>
                </select>
            </div>
            
            <div class="form-group">
                <label for="year">Year:</label>
                <input type="number" id="year" name="year" min="2000" max="2100" required>
            </div>
            
            <button type="submit">Submit</button>
        </form>
    </div>
    
    <div class="container">
        <h2>Award Records</h2>
        <?php
        $conn = connectDB();
        $result = getAllAwards($conn);
        
        if ($result->num_rows > 0): ?>
            <table>
                <thead>
                    <tr>
                        <th>Student Name</th>
                        <th>Category</th>
                        <th>Prize</th>
                        <th>Year</th>
                    </tr>
                </thead>
                <tbody>
                    <?php while($row = $result->fetch_assoc()): ?>
                        <tr>
                            <td><?php echo htmlspecialchars($row['student_name']); ?></td>
                            <td><?php echo htmlspecialchars($row['category']); ?></td>
                            <td><?php echo htmlspecialchars($row['prize']); ?></td>
                            <td><?php echo htmlspecialchars($row['year']); ?></td>
                        </tr>
                    <?php endwhile; ?>
                </tbody>
            </table>
        <?php else: ?>
            <p>No award records found.</p>
        <?php endif; 
        $conn->close();
        ?>
    </div>
</body>
</html>
```
