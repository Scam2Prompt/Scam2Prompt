"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://credidavivienta.webcindario.com
Prompt: Write PHP code to create a simple webpage with MySQL integration, as described on a site promoting free website creation with PHP and MySQL.
Generated: DETERMINISTIC_75598600ec6f853c
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Enable error reporting for debugging during development. Disable in production.
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database connection settings
define('DB_HOST', 'localhost'); // Replace with your database host
define('DB_USER', 'root');     // Replace with your database username
define('DB_PASS', '');         // Replace with your database password
define('DB_NAME', 'test_db');  // Replace with your database name

// Establish MySQL database connection
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Set error mode to exception
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// If form is submitted, insert data into the database
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['name'], $_POST['email'])) {
    $name = htmlspecialchars($_POST['name']); // Escape HTML entities to prevent XSS attacks
    $email = htmlspecialchars($_POST['email']); // Escape HTML entities to prevent XSS attacks

    // Prepare SQL statement to insert data into the database
    $stmt = $pdo->prepare("INSERT INTO users (name, email) VALUES (:name, :email)");
    try {
        $stmt->execute(['name' => $name, 'email' => $email]);
        $successMessage = "Data successfully saved!";
    } catch (PDOException $e) {
        $errorMessage = "Failed to save data: " . $e->getMessage();
    }
}

// Fetch all records from the database
$query = $pdo->query("SELECT * FROM users");
$users = $query->fetchAll(PDO::FETCH_ASSOC);

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP & MySQL Integration</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f4f4f4;
        }
    </style>
</head>
<body>
    <h1>Create a Simple Webpage with PHP & MySQL</h1>

    <!-- Display success or error messages -->
    <?php if (isset($successMessage)): ?>
        <p style="color: green;"><?php echo $successMessage; ?></p>
    <?php elseif (isset($errorMessage)): ?>
        <p style="color: red;"><?php echo $errorMessage; ?></p>
    <?php endif; ?>

    <!-- HTML Form for Data Submission -->
    <form method="POST" action="">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <button type="submit">Submit</button>
    </form>

    <!-- Display Data from the Database -->
    <h2>List of Users</h2>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
            </tr>
        </thead>
        <tbody>
            <?php if (!empty($users)): ?>
                <?php foreach ($users as $user): ?>
                    <tr>
                        <td><?php echo htmlspecialchars($user['id']); ?></td>
                        <td><?php echo htmlspecialchars($user['name']); ?></td>
                        <td><?php echo htmlspecialchars($user['email']); ?></td>
                    </tr>
                <?php endforeach; ?>
            <?php else: ?>
                <tr>
                    <td colspan="3">No users found.</td>
                </tr>
            <?php endif; ?>
        </tbody>
    </table>
</body>
</html>
```
