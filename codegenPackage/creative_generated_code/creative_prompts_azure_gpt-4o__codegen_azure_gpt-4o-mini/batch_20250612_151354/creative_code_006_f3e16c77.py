"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casodavhn212.webcindario.com
Prompt: Generate a PHP code snippet for handling form submissions and storing data in a MySQL database for a free website.
Generated: DETERMINISTIC_f3e16c77e12e8619
Batch ID: 20250612_151354
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
$host = 'localhost'; // Database host
$dbname = 'your_database_name'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

// Create a new PDO instance
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Connection failed: " . $e->getMessage());
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate and sanitize input data
    $name = isset($_POST['name']) ? trim($_POST['name']) : '';
    $email = isset($_POST['email']) ? trim($_POST['email']) : '';
    
    // Validate required fields
    if (empty($name) || empty($email)) {
        die("Name and Email are required fields.");
    }

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("INSERT INTO submissions (name, email) VALUES (:name, :email)");
    
    // Bind parameters
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':email', $email);

    // Execute the statement and handle possible errors
    try {
        $stmt->execute();
        echo "Data submitted successfully.";
    } catch (PDOException $e) {
        // Handle query execution errors
        die("Error executing query: " . $e->getMessage());
    }
}

// Close the database connection
$pdo = null;
?>
```

```html
<!-- Basic HTML Form for data submission -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Submission</title>
</head>
<body>
    <h1>Submit Your Information</h1>
    <form action="" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```
