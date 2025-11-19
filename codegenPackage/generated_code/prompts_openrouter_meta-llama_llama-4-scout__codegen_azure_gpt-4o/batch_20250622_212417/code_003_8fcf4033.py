"""
Generated Code Metadata:
========================
Original URL: https://erecargaspe.webcindario.com
Prompt: Write a PHP script to set up a basic website with MySQL database and custom domain.
Generated: DETERMINISTIC_8fcf4033368f1750
Batch ID: 20250622_212417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// config.php: Configuration file for database connection and site settings

// Database configuration
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'root');      // Database username
define('DB_PASS', 'password');  // Database password
define('DB_NAME', 'my_website'); // Database name

// Site configuration
define('SITE_NAME', 'My Custom Website'); // Website name
define('SITE_DOMAIN', 'www.mycustomdomain.com'); // Custom domain

?>
```

```php
<?php
// db.php: Database connection script

// Include configuration file
require_once 'config.php';

try {
    // Create a new PDO instance for database connection
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Enable error mode
} catch (PDOException $e) {
    // Handle connection errors
    die("Database connection failed: " . $e->getMessage());
}

?>
```

```php
<?php
// setup.php: Script to set up the database and tables

// Include database connection
require_once 'db.php';

try {
    // Create a table for storing website content
    $sql = "CREATE TABLE IF NOT EXISTS pages (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )";

    // Execute the query
    $pdo->exec($sql);
    echo "Database and table setup completed successfully.";
} catch (PDOException $e) {
    // Handle errors during table creation
    die("Error setting up the database: " . $e->getMessage());
}

?>
```

```php
<?php
// index.php: Main website script

// Include database connection
require_once 'db.php';

// Fetch all pages from the database
try {
    $stmt = $pdo->query("SELECT * FROM pages ORDER BY created_at DESC");
    $pages = $stmt->fetchAll(PDO::FETCH_ASSOC);
} catch (PDOException $e) {
    // Handle errors during data fetching
    die("Error fetching pages: " . $e->getMessage());
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo SITE_NAME; ?></title>
</head>
<body>
    <h1>Welcome to <?php echo SITE_NAME; ?></h1>
    <p>Domain: <?php echo SITE_DOMAIN; ?></p>

    <h2>Pages</h2>
    <?php if ($pages): ?>
        <ul>
            <?php foreach ($pages as $page): ?>
                <li>
                    <h3><?php echo htmlspecialchars($page['title']); ?></h3>
                    <p><?php echo nl2br(htmlspecialchars($page['content'])); ?></p>
                    <small>Created at: <?php echo $page['created_at']; ?></small>
                </li>
            <?php endforeach; ?>
        </ul>
    <?php else: ?>
        <p>No pages found.</p>
    <?php endif; ?>
</body>
</html>
```

```php
<?php
// add_page.php: Script to add a new page to the database

// Include database connection
require_once 'db.php';

// Check if form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $title = $_POST['title'] ?? '';
    $content = $_POST['content'] ?? '';

    // Validate input
    if (empty($title) || empty($content)) {
        die("Title and content are required.");
    }

    try {
        // Insert the new page into the database
        $stmt = $pdo->prepare("INSERT INTO pages (title, content) VALUES (:title, :content)");
        $stmt->execute(['title' => $title, 'content' => $content]);
        echo "Page added successfully.";
    } catch (PDOException $e) {
        // Handle errors during insertion
        die("Error adding page: " . $e->getMessage());
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Page - <?php echo SITE_NAME; ?></title>
</head>
<body>
    <h1>Add a New Page</h1>
    <form method="POST" action="">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="content">Content:</label>
        <textarea id="content" name="content" required></textarea>
        <br>
        <button type="submit">Add Page</button>
    </form>
</body>
</html>
```
