"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coosella5554.webcindario.com
Prompt: How can I create a free website using PHP and MySQL as mentioned on coosella5554.webcindario.com?
Generated: DETERMINISTIC_366846022b69a749
Batch ID: 20250612_163552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Configuration file for database connection
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'root');      // Database username
define('DB_PASS', '');          // Database password
define('DB_NAME', 'website_db'); // Database name

// Establish a connection to MySQL database
try {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    // Check connection
    if ($conn->connect_error) {
        throw new Exception('Database connection failed: ' . $conn->connect_error);
    }
} catch (Exception $e) {
    die($e->getMessage());
}

// Create a table for website content if it doesn't exist
$tableQuery = "
CREATE TABLE IF NOT EXISTS pages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;
";

if (!$conn->query($tableQuery)) {
    die('Error creating table: ' . $conn->error);
}

// Insert a sample page into the database if the table is empty
$pageCountQuery = "SELECT COUNT(*) AS count FROM pages";
$result = $conn->query($pageCountQuery);
$row = $result->fetch_assoc();
if ($row['count'] == 0) {
    $samplePageQuery = "INSERT INTO pages (title, content) VALUES (?, ?)";
    $stmt = $conn->prepare($samplePageQuery);
    $stmt->bind_param('ss', $title, $content);

    // Sample page content
    $title = 'Welcome to My Website';
    $content = 'This is a sample website built using PHP and MySQL.';
    if (!$stmt->execute()) {
        die('Error inserting sample page: ' . $stmt->error);
    }
    $stmt->close();
}

// Fetch all pages from the database
$pagesQuery = "SELECT * FROM pages ORDER BY created_at DESC";
$pagesResult = $conn->query($pagesQuery);
if (!$pagesResult) {
    die('Error fetching pages: ' . $conn->error);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My PHP Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
            color: #333;
        }
        header {
            background: #333;
            color: #fff;
            padding: 10px 20px;
            text-align: center;
        }
        .container {
            padding: 20px;
            max-width: 800px;
            margin: auto;
        }
        article {
            border-bottom: 1px solid #ddd;
            margin-bottom: 20px;
            padding-bottom: 10px;
        }
        h2 {
            color: #555;
        }
    </style>
</head>
<body>
    <header>
        <h1>My PHP Website</h1>
    </header>
    <div class="container">
        <?php
        // Display all pages
        if ($pagesResult->num_rows > 0) {
            while ($page = $pagesResult->fetch_assoc()) {
                echo '<article>';
                echo '<h2>' . htmlspecialchars($page['title']) . '</h2>';
                echo '<p>' . nl2br(htmlspecialchars($page['content'])) . '</p>';
                echo '<small>Created on: ' . htmlspecialchars($page['created_at']) . '</small>';
                echo '</article>';
            }
        } else {
            echo '<p>No pages found. Please add content to your website.</p>';
        }

        // Close the database connection
        $conn->close();
        ?>
    </div>
</body>
</html>
```
