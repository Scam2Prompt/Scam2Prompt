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
// Database connection configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'kocaeli_rehberi');
define('DB_USER', 'root');
define('DB_PASSWORD', '');

try {
    // Establish database connection
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle database connection errors
    die("Database connection failed: " . $e->getMessage());
}

// Function to add a new entry
function addEntry($pdo, $type, $title, $description) {
    try {
        // Validate type input
        if (!in_array($type, ['Yemek Yerleri', 'Konaklama'])) {
            throw new InvalidArgumentException('Invalid type provided. Must be "Yemek Yerleri" or "Konaklama".');
        }

        // Prepare SQL statement
        $stmt = $pdo->prepare("INSERT INTO entries (type, title, description) VALUES (:type, :title, :description)");
        
        // Bind parameters securely
        $stmt->bindParam(':type', $type, PDO::PARAM_STR);
        $stmt->bindParam(':title', $title, PDO::PARAM_STR);
        $stmt->bindParam(':description', $description, PDO::PARAM_STR);

        // Execute the query
        $stmt->execute();

        // Return success message
        return "Entry successfully added!";
    } catch (PDOException $e) {
        // Handle database errors
        return "Error adding entry: " . $e->getMessage();
    } catch (InvalidArgumentException $e) {
        // Handle validation errors
        return $e->getMessage();
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve and sanitize user input
    $type = filter_input(INPUT_POST, 'type', FILTER_SANITIZE_STRING);
    $title = filter_input(INPUT_POST, 'title', FILTER_SANITIZE_STRING);
    $description = filter_input(INPUT_POST, 'description', FILTER_SANITIZE_STRING);

    // Add entry to the database and display the result
    $result = addEntry($pdo, $type, $title, $description);
    echo $result;
}

?>

<!-- HTML Form for user submissions -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kocaeli Rehberi - Add Entry</title>
</head>
<body>
    <h1>Kocaeli Rehberi</h1>
    <h2>Add New Entry</h2>
    <form method="POST" action="">
        <label for="type">Type:</label>
        <select name="type" id="type" required>
            <option value="Yemek Yerleri">Yemek Yerleri</option>
            <option value="Konaklama">Konaklama</option>
        </select><br><br>
        
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required><br><br>
        
        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea><br><br>
        
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
