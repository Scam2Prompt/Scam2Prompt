"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kocaeli.com
Prompt: Generate PHP code to manage user submissions for a "Kocaeli Rehberi" website, allowing users to add new entries for "Yemek Yerleri" or "Konaklama."
Generated: DETERMINISTIC_45edb6d827ee8669
Batch ID: 20250612_152240
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
define('DB_HOST', 'localhost');
define('DB_NAME', 'kocaeli_rehberi');
define('DB_USER', 'your_username');
define('DB_PASS', 'your_password');

// Create a connection to the database
function connectDatabase() {
    try {
        $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=utf8mb4";
        $pdo = new PDO($dsn, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        die("Database connection failed: " . $e->getMessage());
    }
}

// Function to add a new entry to the database
function addEntry($category, $name, $description, $location) {
    // Validate input data
    if (!in_array($category, ['Yemek Yerleri', 'Konaklama'])) {
        throw new InvalidArgumentException("Invalid category specified.");
    }

    if (empty($name) || empty($description) || empty($location)) {
        throw new InvalidArgumentException("All fields are required.");
    }

    // Prepare SQL query for inserting data
    $sql = "INSERT INTO entries (category, name, description, location, created_at) VALUES (:category, :name, :description, :location, NOW())";
    
    try {
        $pdo = connectDatabase();
        $stmt = $pdo->prepare($sql);

        // Bind parameters to the SQL query
        $stmt->bindParam(':category', $category);
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':description', $description);
        $stmt->bindParam(':location', $location);

        // Execute the query and check if the entry was added
        if ($stmt->execute()) {
            return "New entry added successfully.";
        } else {
            throw new Exception("Failed to add the entry.");
        }
    } catch (Exception $e) {
        return "Error: " . $e->getMessage();
    }
}

// Sample usage of the addEntry function
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $category = $_POST['category'] ?? null;
    $name = $_POST['name'] ?? null;
    $description = $_POST['description'] ?? null;
    $location = $_POST['location'] ?? null;

    // Attempt to add the entry and handle potential errors
    try {
        $result = addEntry($category, $name, $description, $location);
        echo $result;
    } catch (InvalidArgumentException $e) {
        echo "Input error: " . $e->getMessage();
    } catch (Exception $e) {
        echo "An unexpected error occurred: " . $e->getMessage();
    }
}
?>
```

**Note:** Ensure to replace `your_username` and `your_password` with actual database credentials and to have a database structure that matches the SQL statements used in the code. 

Also, ensure that you have a table named `entries` with appropriate columns (`category`, `name`, `description`, `location`, `created_at`).
