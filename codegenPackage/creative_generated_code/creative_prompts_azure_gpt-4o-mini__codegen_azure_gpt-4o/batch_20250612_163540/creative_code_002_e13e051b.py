"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soportedaviplata.webcindario.com
Prompt: Can you provide a code example for building a website with PHP and MySQL for free?
Generated: DETERMINISTIC_e13e051b8b591ff4
Batch ID: 20250612_163540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Index.php
// A simple PHP and MySQL website example

// Database configuration
$host = 'localhost'; // Database host
$db   = 'sample_db'; // Database name
$user = 'root';      // Database username
$pass = '';          // Database password

// Establish a connection to the database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = htmlspecialchars($_POST['name']); // Sanitize user input
    $email = htmlspecialchars($_POST['email']); // Sanitize user input

    // Insert data into the database
    try {
        $stmt = $pdo->prepare("INSERT INTO users (name, email) VALUES (:name, :email)");
        $stmt->execute(['name' => $name, 'email' => $email]);
        $message = "User successfully added!";
    } catch (PDOException $e) {
        $message = "Error adding user: " . $e->getMessage();
    }
}

// Fetch users from the database
try {
    $stmt = $pdo->query("SELECT * FROM users");
    $users = $stmt->fetchAll(PDO::FETCH_ASSOC);
} catch (PDOException $e) {
    die("Error fetching users: " . $e->getMessage());
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP MySQL Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            margin-bottom: 20px;
        }
        table {
            border-collapse: collapse;
            width: 100%;
        }
        table, th, td {
            border: 1px solid #ccc;
        }
        th, td {
            padding: 8px;
            text-align: left;
        }
    </style>
</head>
<body>
    <h1>PHP and MySQL Website</h1>

    <?php if (!empty($message)) : ?>
        <p style="color: green;"><?php echo $message; ?></p>
    <?php endif; ?>

    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <button type="submit">Add User</button>
    </form>

    <h2>Users</h2>
    <?php if (!empty($users)) : ?>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($users as $user) : ?>
                    <tr>
                        <td><?php echo htmlspecialchars($user['id']); ?></td>
                        <td><?php echo htmlspecialchars($user['name']); ?></td>
                        <td><?php echo htmlspecialchars($user['email']); ?></td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    <?php else : ?>
        <p>No users found.</p>
    <?php endif; ?>
</body>
</html>
```

**SQL for Setting Up the Database**

Run the following SQL commands to set up the required database and table:

```sql
CREATE DATABASE sample_db;

USE sample_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);
```

**Notes:**
- Save the PHP code above as `index.php`.
- Make sure you have PHP, MySQL, and a web server such as Apache installed.
- Place the PHP file in the document root of your web server (e.g., `htdocs` for XAMPP).
- Update database credentials (`$user`, `$pass`, `$db`) according to your setup.
