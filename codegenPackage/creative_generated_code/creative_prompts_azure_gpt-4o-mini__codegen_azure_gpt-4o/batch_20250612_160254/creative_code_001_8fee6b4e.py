"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chainlink.webcindario.com
Prompt: What are the steps to set up a website with PHP and MySQL for free?
Generated: DETERMINISTIC_8fee6b4e37d7a9d3
Batch ID: 20250612_160254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Step 1: Configuration for the database connection
// Ensure you have MySQL installed and running locally or remotely.
$servername = "localhost"; // Change to your server address if not localhost
$username = "root";        // Replace with your MySQL username
$password = "";            // Replace with your MySQL password
$dbname = "my_website";    // The name of your database

// Step 2: Establish a connection to the MySQL database
try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception for better error handling.
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Database connection successful!";
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Step 3: Create a table (if it doesn’t exist)
try {
    $table_sql = "CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )";

    $conn->exec($table_sql);
    echo "Table 'users' has been created or already exists.";
} catch (PDOException $e) {
    die("Table creation failed: " . $e->getMessage());
}

// Step 4: Insert sample data into the table
try {
    $insert_sql = "INSERT INTO users (username, password) VALUES (:username, :password)";
    $stmt = $conn->prepare($insert_sql);

    $hashed_password = password_hash("password123", PASSWORD_DEFAULT); // Always hash passwords!
    $stmt->bindParam(':username', $username_value);
    $stmt->bindParam(':password', $password_value);

    // Example data
    $username_value = "admin";
    $password_value = $hashed_password;

    $stmt->execute();
    echo "Sample user data inserted successfully.";
} catch (PDOException $e) {
    echo "Data insertion failed: " . $e->getMessage();
}

// Step 5: Create a simple webpage for user display
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP and MySQL Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <h2>User List</h2>
    <table>
        <tr>
            <th>ID</th>
            <th>Username</th>
            <th>Created At</th>
        </tr>
        <?php
        // Step 6: Fetch and display data from the database
        try {
            $select_sql = "SELECT id, username, created_at FROM users";
            $stmt = $conn->query($select_sql);

            while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                echo "<tr>";
                echo "<td>" . htmlspecialchars($row['id']) . "</td>";
                echo "<td>" . htmlspecialchars($row['username']) . "</td>";
                echo "<td>" . htmlspecialchars($row['created_at']) . "</td>";
                echo "</tr>";
            }
        } catch (PDOException $e) {
            echo "<tr><td colspan='3'>Error fetching data: " . $e->getMessage() . "</td></tr>";
        }
        ?>
    </table>
</body>
</html>
```

Notes (in code comments):
- Make sure you have PHP installed (e.g., XAMPP, MAMP, or your hosting server).
- Set up MySQL and create a database named `my_website` before running this code.
- Update `$servername`, `$username`, `$password`, and `$dbname` as per your setup.
- Passwords for users should always be hashed using a secure method, as demonstrated above.
