"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sugerencias.webcindario.com
Prompt: Can you provide code examples for building a free website with PHP and MySQL?
Generated: DETERMINISTIC_dfe6221d1d0a2892
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File: config.php
// Purpose: Configuration file for database connection

// Database connection details
define('DB_HOST', 'localhost'); // Change as needed
define('DB_USER', 'root');      // Change as needed
define('DB_PASS', '');          // Change as needed
define('DB_NAME', 'website');   // Change as needed

/**
 * Create a database connection
 */
function getDbConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    return $conn;
}
?>
```

```php
<?php
// File: setup.php
// Purpose: Script to set up the database and tables

require_once 'config.php';

$conn = getDbConnection();

// SQL to create a table for storing website content
$sql = "CREATE TABLE IF NOT EXISTS pages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)";

if ($conn->query($sql) === TRUE) {
    echo "Table 'pages' created successfully.\n";
} else {
    echo "Error creating table: " . $conn->error;
}

$conn->close();
?>
```

```php
<?php
// File: index.php
// Purpose: Main website page to display content

require_once 'config.php';

$conn = getDbConnection();

// Fetch all pages from the database
$sql = "SELECT * FROM pages ORDER BY created_at DESC";
$result = $conn->query($sql);

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple PHP Website</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .page { margin-bottom: 20px; }
        .title { font-size: 24px; font-weight: bold; }
        .content { margin-top: 10px; }
        .timestamp { font-size: 12px; color: gray; }
    </style>
</head>
<body>
    <h1>Welcome to My PHP Website</h1>

    <?php if ($result->num_rows > 0): ?>
        <?php while ($row = $result->fetch_assoc()): ?>
            <div class="page">
                <div class="title"><?= htmlspecialchars($row['title']) ?></div>
                <div class="content"><?= nl2br(htmlspecialchars($row['content'])) ?></div>
                <div class="timestamp">Published on: <?= $row['created_at'] ?></div>
            </div>
        <?php endwhile; ?>
    <?php else: ?>
        <p>No pages available. Please add content.</p>
    <?php endif; ?>

    <?php $conn->close(); ?>
</body>
</html>
```

```php
<?php
// File: add_page.php
// Purpose: Page for adding new content to the website

require_once 'config.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate input
    $title = isset($_POST['title']) ? trim($_POST['title']) : '';
    $content = isset($_POST['content']) ? trim($_POST['content']) : '';

    if ($title && $content) {
        $conn = getDbConnection();

        // Prepare and bind SQL statement
        $stmt = $conn->prepare("INSERT INTO pages (title, content) VALUES (?, ?)");
        $stmt->bind_param("ss", $title, $content);

        if ($stmt->execute()) {
            echo "Page added successfully.";
        } else {
            echo "Error: " . $stmt->error;
        }

        $stmt->close();
        $conn->close();
    } else {
        echo "Title and content are required.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Page</title>
</head>
<body>
    <h1>Add New Page</h1>
    <form method="POST" action="">
        <label for="title">Title:</label>
        <br>
        <input type="text" id="title" name="title" required>
        <br><br>
        <label for="content">Content:</label>
        <br>
        <textarea id="content" name="content" rows="6" cols="50" required></textarea>
        <br><br>
        <button type="submit">Add Page</button>
    </form>
</body>
</html>
```

**Note:**
Ensure the database named `website` exists before running the scripts. You can create the database manually or modify the `setup.php` script to include a query for creating the database.
