"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davihncas230.webcindario.com
Prompt: Can you provide a code example for building a website with PHP and MySQL based on the information from the webpage?
Generated: DETERMINISTIC_a8805c2c50a33c5d
Batch ID: 20250612_155340
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
$dbname = 'example_db'; // Database name
$username = 'root'; // Database user
$password = ''; // Database password

// Create a connection to the database using PDO
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

// Function to fetch data from the database
function fetchData($pdo)
{
    $stmt = $pdo->prepare("SELECT * FROM users"); // Prepare SQL statement
    $stmt->execute(); // Execute the statement
    return $stmt->fetchAll(PDO::FETCH_ASSOC); // Return fetched data
}

// Fetch user data from the database
$userData = fetchData($pdo);

// Close the database connection
$pdo = null;

// HTML Document Starts Here
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User List</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS -->
</head>
<body>
    <header>
        <h1>User List</h1>
    </header>
    <main>
        <?php if (count($userData) > 0): ?>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Email</th>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach ($userData as $user): ?>
                        <tr>
                            <td><?php echo htmlspecialchars($user['id']); ?></td>
                            <td><?php echo htmlspecialchars($user['name']); ?></td>
                            <td><?php echo htmlspecialchars($user['email']); ?></td>
                        </tr>
                    <?php endforeach; ?>
                </tbody>
            </table>
        <?php else: ?>
            <p>No users found.</p>
        <?php endif; ?>
    </main>
    <footer>
        <p>&copy; <?php echo date('Y'); ?> Your Company</p>
    </footer>
</body>
</html>
```

**Create a CSS file `styles.css` for styling:**

```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #4CAF50;
    color: white;
    text-align: center;
    padding: 1em 0;
}

main {
    margin: 20px;
}

table {
    width: 100%;
    border-collapse: collapse;
}

th, td {
    border: 1px solid #ddd;
    padding: 8px;
}

th {
    background-color: #f2f2f2;
}
```

**SQL to create the `users` table:**

```sql
CREATE TABLE users (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);
```
